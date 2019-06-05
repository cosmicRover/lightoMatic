# data model for our bulb. Only holds a few properties


class BulbModel:

    def __init__(self, ip: str, port: int, status: str):
        self.ip = ip
        self.port = port
        self.status = status
