import socket


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
