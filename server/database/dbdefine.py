import redis
from abc import ABC, abstractmethod

class ObjectStorage(ABC):
    name: str
    host: str
    port: int

    @abstractmethod
    def put(self, key, value):
        ...

    @abstractmethod
    def get(self, key):
        ...
    @abstractmethod
    def ping(self):
        ...

    @abstractmethod
    def set_map(self, key, map: dict):
        ...

    @abstractmethod
    def get_map(self, key):
        ...



class ObjectStorageRedis(ObjectStorage):

    def __init__(self,  name= "redis", host: str = "localhost", port: int = 6379):
        self.name = name
        self.host = host
        self.port = port
        self.client = self.create_client()

    def create_client(self):
        return redis.Redis(self.host, self.port, decode_responses=True)
                                                                                                                                                    
    def ping(self):
        return self.client.ping()
    
    def get(self, key):
        return self.client.get(key)

    def put(self, key, value):
        return self.client.set(key, value)
    
    def set_map(self, key, map: dict):
        return self.client.hset(key, mapping=map)

    def get_map(self, key):
        return self.client.hgetall(key)

    def delete(self, key: str):
        return self.client.delete(key)