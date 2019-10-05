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
        self.dataFlag = Event()

        self.dataProcess = Process(target=self._telloDataThread,args=(self.exitFlag,self.dataFlag,self.dataQueue,))
        self.cmdProcess = Process(target=self._telloCmdThread,args=(self.exitFlag,self.cmdQueue,))
        sleep(1)

    def start(self):
        self.dataProcess.start()
        self.cmdProcess.start()
        sleep(1)
        return True if self.dataProcess.is_alive() and self.cmdProcess.is_alive() else False

    def stop(self):
        self.exitFlag.set()
        self.dataProcess.join()
        self.cmdQueue.put('Process End')
        self.cmdProcess.join()
        return True

    def _telloDataThread(self,exitFlag,getDataFlag,dataQueue):
        sockData = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockData.bind(('', 8890))
        sockData.setblocking(False)
        data = {}
        while not exitFlag.is_set():
            try:
                recv = sockData.recvfrom(4096)
                data[recv[1][0]] = (recv[0].decode('utf-8'),time())
            except:
                pass

            if getDataFlag.is_set():
                dataQueue.put(data)
                getDataFlag.clear()

        sockData.close()

    def _telloCmdThread(self,exitFlag,cmdQueue):
        sockCmd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockCmd.bind(('', 8889))
        sockCmd.settimeout(3)

        while not exitFlag.is_set():
            cmd = cmdQueue.get()
            if cmd == 'Process End':
                break
            sockCmd.sendto(cmd[0].encode('utf-8'), (cmd[1], 8889))
            try:
                recv = sockCmd.recvfrom(4096)
            except:
                recv = False
            cmdQueue.put(recv)

        sockCmd.close()


    def threadAlive(self):
        return self.dataProcess.is_alive(),self.cmdProcess.is_alive()

    def getData(self):
        self.dataFlag.set()
        try:
            return self.dataQueue.get(timeout=3)
        except:
            return False

    def sendCommand(self,ip,command):
        self.cmdQueue.put((command,ip))
        try:
            data = self.cmdQueue.get(timeout=3)
        except:
            return False

        if data == False:
            return False
        else:
            return data[0].decode('utf-8'),data[1][0]
