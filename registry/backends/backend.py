from abc import ABC, abstractmethod


class Backend(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read') and
                callable(subclass.read) and
                hasattr(subclass, 'write') and
                callable(subclass.write) or
                NotImplemented)


    @abstractmethod
    def read(self, path: str, file_name: str):
        """Read data from backend"""
        raise NotImplementedError


    @abstractmethod
    def write(self, full_file_path: str):
        """Write data to backend"""
        raise NotImplementedError
