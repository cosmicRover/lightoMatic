import os

class NetworkMod:

    def __init__(self, hostName):
        self.hostName = hostName

    def checkForIpOnNetwork(self) -> bool:

        response = os.system("ping -c 1 " + self.hostName)

        return True if response == 0 else False
            




