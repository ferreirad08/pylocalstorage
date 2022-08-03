from os import path
from json import load, dumps


class LocalStorage:

    __version__ = "1.0.2"
    __fname = None
    length = 0

    def __init__(self):
        # Getting PATH of file
        pathname, _ = path.split(path.abspath(__file__))
        self.__fname = path.join(pathname, "localstorage.json")
        if not path.isfile(self.__fname):
            self.__write_json({})
        else:
            self.length = len(self.__read_json())

    def setItem(self, key, value):
        data = self.__read_json()
        data[key] = value
        self.__write_json(data)

    def getItem(self, key):
        data = self.__read_json()
        return data.get(key)

    def removeItem(self, key):
        data = self.__read_json()
        if key in data:
            del data[key]
            self.__write_json(data)

    def clear(self):
        self.__write_json({})

    def key(self, index):
    	data = self.__read_json()
    	return list(data.keys())[index]

    def __read_json(self):
        try:
            with open(self.__fname, "r") as file:
                return load(file)
        except:
            raise ReadStorageError

    def __write_json(self, data):
        try:
            data_str = dumps(data)
            with open(self.__fname, "w") as file:
                print(data_str, file=file)
            self.length = len(data)
        except:
            raise WriteStorageError


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class ReadStorageError(BaseError):
    message = "Unable to recover data"


class WriteStorageError(BaseError):
    message = "Unable to save data"
