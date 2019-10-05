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
        self.cmdQueue = Queue()
        self.dataQueue = Queue()
        self.cmdResponseQueue = Queue()

        self.dataProcess = Process(target=self._telloDataThread,args=(self.exitFlag,self.dataQueue,))
        self.cmdProcess = Process(target=self._telloCmdThread,args=(self.exitFlag,self.cmdQueue,))
        self.cmdRetProcess = Process(target=self._telloCmdRetThread,args=(self.exitFlag,self.cmdResponseQueue,))
        sleep(1)

    def start(self):
        #self.dataProcess.start()
        self.cmdProcess.start()
        #self.cmdRetProcess.start()
        sleep(1)
        return True if self.dataProcess.is_alive() and self.cmdProcess.is_alive() and self.cmdRetProcess.is_alive() else False

    def stop(self):
        self.exitFlag.set()
        #self.dataProcess.join()
        #self.cmdRetProcess.join()
        self.cmdQueue.put('Process End')
        self.cmdProcess.join()
        return True

    def _telloDataThread(self,exitFlag,dataQueue):
        sockData = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockData.bind(('', 8890))
        while not exitFlag.is_set():
            recv = sockData.recvfrom(4096)
            dataQueue.put((recv[0].decode('utf-8'),time()))

        sockData.close()

    def _telloCmdThread(self,exitFlag,cmdQueue):
        sockCmd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while not exitFlag.is_set():
            cmd = cmdQueue.get()
            if cmd == 'Process End':
                break
            sockCmd.sendto(cmd[0].encode('utf-8'), (cmd[1], 8889))

        sockCmd.close()

    def _telloCmdRetThread(self,exitFlag,cmdReturn):
        sockCmdRet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockCmdRet.bind(('', 8889))

        while not exitFlag.is_set():
            print('recv')
            recv = sockCmdRet.recvfrom(4096)
            cmdReturn.put((recv[0].decode('utf-8'),recv[1][0],time()))

        sockCmdRet.close()

    def threadAlive(self):
        return self.dataProcess.is_alive(),self.cmdProcess.is_alive()

    def getData(self):
        data = []
        while not self.dataQueue.empty():
            data.append(self.dataQueue.get(timeout=3))
        return data

    def sendCommand(self,ip,command):
        self.cmdQueue.put((command,ip))
        return True

    def getCommand(self):
        data = []
        while not self.dataQueue.empty():
            data.append(self.cmdResponseQueue.get(timeout=3))
        return data
