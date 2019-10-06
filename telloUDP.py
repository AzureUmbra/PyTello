import socket
from multiprocessing import Process, Queue, Event
from time import sleep, time


class SimpleTelloUDP():
    def __init__(self,ip,startWithData=True,timeout=1):
        self.dataLink = startWithData

        if startWithData:
            self.sockData = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.sockData.bind(('',8890))
            self.sockData.setblocking(False)

        self.sockCmd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sockCmd.bind(('', 8889))
        self.sockCmd.settimeout(timeout)

        self.telloIP = ip

    def send(self,cmd):
        self.sockCmd.sendto(cmd.encode('utf-8'),(self.telloIP,8889))
        try:
            return self.sockCmd.recvfrom(4096)
        except:
            return False

    def recv(self):
        if self.dataLink:
            try:
                return self.sockData.recvfrom(1024)
            except:
                return False
        else:
            return False

    def exit(self):
        self.sockData.close()
        self.sockCmd.close()


class TelloUDP():
    def __init__(self):
        self.exitFlag = Event()
        self.commandQueue = Queue()
        self.dataQueue = Queue()
        self.commandResponseQueue = Queue()

        self.commandSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.commandSocket.bind(('', 8889))
        #self.dataSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.dataSocket.bind(('', 8890))

        self.dataProcess = Process(target=self._telloDataThread, args=(self.exitFlag,self.dataQueue,self.dataSocket,))
        self.commandProcess = Process(target=self._telloCommandThread, args=(self.exitFlag, self.commandQueue, self.commandSocket,))
        self.commandReturnProcess = Process(target=self._telloCommandReturnThread, args=(self.exitFlag, self.commandResponseQueue, self.commandSocket,))
        sleep(1)

    def start(self):
        #self.dataProcess.start()
        self.commandProcess.start()
        self.commandReturnProcess.start()
        sleep(1)
        #return True if self.dataProcess.is_alive() and self.commandProcess.is_alive() and self.commandReturnProcess.is_alive() else TelloError(2)
        return True if self.commandProcess.is_alive() and self.commandReturnProcess.is_alive() else TelloError(2)

    def stop(self):
        self.exitFlag.set()
        #self.dataProcess.join()
        self.commandReturnProcess.join()
        self.commandQueue.put('Process End')
        self.commandProcess.join()
        return True

    def _telloDataThread(self, exitFlag, dataQueue, dataSocket):
        while not exitFlag.is_set():
            recv = dataSocket.recvfrom(4096)
            dataQueue.put((recv[0].decode('utf-8'),time()))

        dataSocket.close()

    def _telloCommandThread(self, exitFlag, commandQueue, commandSocket):
        while not exitFlag.is_set():
            cmd = commandQueue.get()
            if cmd == 'Process End':
                break
            commandSocket.sendto(cmd[0].encode('utf-8'), (cmd[1], 8889))

        commandSocket.close()

    def _telloCommandReturnThread(self,exitFlag,cmdReturn,sockCmdRet):
        while not exitFlag.is_set():
            recv = sockCmdRet.recvfrom(4096)
            cmdReturn.put((recv[0].decode('utf-8'),recv[1][0],time()))

        sockCmdRet.close()

    def threadAlive(self):
        #return self.dataProcess.is_alive(),self.commandProcess.is_alive()
        return self.commandProcess.is_alive()

    def getData(self):
        data = []
        while not self.dataQueue.empty():
            try:
                data.append(self.dataQueue.get(timeout=3))
            except:
                return TelloError(0)
        return data

    def sendCommand(self,ip,command):
        try:
            self.commandQueue.put((command, ip),timeout=3)
            return True
        except:
            return TelloError(1)

    def getCommand(self):
        data = []
        while not self.commandResponseQueue.empty():
            try:
                data.append(self.commandResponseQueue.get(timeout=3))
            except:
                return TelloError(0)
        return data

class TelloError():
    def __init__(self,error,info=None):
        self.error = error
        self.errorList = {0:'Timeout on Read',1:'Timeout on Write',2:'Failure to Start Thread',3:'Timeout on Receiving Data',4:'Unknown Tello'}
        self.additionalInfo = info

    def __str__(self):
        return "Error Code {}: {}\n{}".format(self.error,self.errorList[self.error],self.additionalInfo)
