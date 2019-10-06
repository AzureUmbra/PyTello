from telloUDP import TelloUDP,TelloError
from time import time

class PyTello():
    def __init__(self,ip,timeout=30):
        """
        An extension of TelloUDP for ease of use.
        :param ip: str- The ip of the Tello
        :param timeout: int (default 30)- Timeout on waiting for a response from the Tello
        """
        self.timeout = timeout
        self.ip = ip
        self.tello = TelloUDP()

    def start(self):
        """
        Starts the TelloUDP instance.
        :return: bool- Did TelloUDP start correctly
        """
        return self.tello.start()

    def stop(self):
        """
        Cleanly exits the TelloUDP instance.
        :return: bool- Did TelloUDP exit correctly
        """
        del self.tello
        return True

    def sendCommand(self,command):
        """
        Sends a command to the tello and waits for a response.
        :param command: str- A command from Tello SDK 2.0
        :return: tuple- (message from tello, ip of tello, time received)
        """
        cmd = self.tello.sendCommand(self.ip,command)
        if cmd is not type(TelloError):
            flag = time()
            while time()-flag <= self.timeout:
                data = self.tello.getCommand()
                if data != []:
                    return data
            return TelloError(3)
        else:
            return cmd

    def sendCommandNoWait(self,command):
        """
        Sends a command to the tello and does not wait for a response.
        :param command: str- A command from Tello SDK 2.0
        :return: bool- Did the message send
        """
        return self.tello.sendCommand(self.ip, command)

    def getCommandResponse(self):
        """
        Request all previously unread messages from the tello.
        :return: list- contains tuples: (message from tello, ip of tello, time received)
        """
        cmd = self.tello.getCommand()
        if cmd != []:
            return cmd
        else:
            return False


class PyTelloSwarm():
    def __init__(self, ipDict, timeout=30):
        """
        An extension of TelloUDP for ease of use, directed at managing multiple tello aircraft at once.
        :param ipDict: dict- key:str=aircraft id, value:str=ip address
        :param timeout: int (default 30)- Timeout on waiting for a response from the Tello
        """
        self.timeout = timeout
        self.ip = ipDict
        self.tello = TelloUDP()

    def start(self):
        """
        Starts the TelloUDP instance.
        :return: bool- Did TelloUDP start correctly
        """
        return self.tello.start()

    def stop(self):
        """
        Cleanly exits the TelloUDP instance.
        :return: bool- Did TelloUDP exit correctly
        """
        del self.tello
        return True

    def sendCommand(self, command, aircraft):
        """
        Sends a command to the tello(s) and waits for a response.
        :param command: str- A command from Tello SDK 2.0
        :param aircraft: str or list- The id of the specific tello(s)
        :return: tuple or dict AND list- (message from tello, ip of tello, time received); key:str=aircraft id, value:bool= did the message send AND list:tuple
        """
        if type(aircraft) is str:
            if aircraft in self.ip.keys():
                cmd = self.tello.sendCommand(self.ip, command)
                if cmd is not type(TelloError):
                    flag = time()
                    while time() - flag <= self.timeout:
                        data = self.tello.getCommand()
                        if data != []:
                            return data
                    return TelloError(3)
                else:
                    return cmd
            else:
                return TelloError(4,'"{}" is an unknown aircraft'.format(aircraft))

        if type(aircraft) is list:
            unknownAircraft = []
            for i in aircraft:
                if i not in self.ip.keys():
                    unknownAircraft.append(i)

            if len(unknownAircraft) == 0:
                responses = {}
                for i in aircraft:
                    responses[i] = self.tello.sendCommand(self.ip[i],command)

                goodResponses = 0
                for i in responses.values():
                    if type(i) is not TelloError:
                        goodResponses += 1
                if goodResponses > 0:
                    flag = time()
                    replies = []
                    while time() - flag <= self.timeout:
                        data = self.tello.getCommand()
                        if  data != []:
                            replies.append(data)
                        if len(replies) == goodResponses:
                            return responses, replies
                    for i in range(goodResponses - len(replies)):
                        replies.append(TelloError(3))
                    return responses, replies
                else:
                    return responses
            else:
                return TelloError(4, '"{}" is an unknown aircraft'.format(str(unknownAircraft)))

    def sendCommandNoWait(self, command, aircraft):
        """
        Sends a command to the tello(s) and does not wait for a response.
        command: str- A command from Tello SDK 2.0
        :param aircraft: str or list- The id of the specific tello(s)
        :return: bool or dict- Did the message send; key:str=aircraft id, value:bool
        """
        if type(aircraft) is str:
            if aircraft in self.ip.keys():
                return self.tello.sendCommand(self.ip[aircraft], command)
            else:
                return TelloError(4,'"{}" is an unknown aircraft'.format(aircraft))

        if type(aircraft) is list:
            unknownAircraft = []
            for i in aircraft:
                if i not in self.ip.keys():
                    unknownAircraft.append(i)

            if len(unknownAircraft) == 0:
                responses = {}
                for i in aircraft:
                    responses[i] = self.tello.sendCommand(self.ip[i],command)
                return responses
            else:
                return TelloError(4, '"{}" is an unknown aircraft'.format(str(unknownAircraft)))

    def getCommandResponse(self):
        """
        Request all previously unread messages from the tello(s).
        :return: list- contains tuples: (message from tello, ip of tello, time received)
        """
        cmd = self.tello.getCommand()
        if cmd != []:
            return cmd
        else:
            return False