from os.path import split, abspath, isfile, exists
from os import remove, mkdir
from json import load, dumps
from glob import glob


class LocalStorage:

    __version__ = "1.1.0"
    __pathname = None
    __filename = None
    __regex = None
    length = 0

    def __init__(self):
        # Getting PATH of file
        self.__pathname, _ = split(abspath(__file__))
        self.__pathname += "/data"
        if not exists(self.__pathname):
            mkdir(self.__pathname)
        self.__filename = self.__pathname + "/{}.json"
        self.list_json = lambda: glob(self.__pathname + "/*.json")
        self.length = len(self.list_json())

    def setItem(self, key, value):
        try:
            value_str = dumps(value)
            with open(self.__filename.format(key), "w") as file:
                print(value_str, file=file)
            self.length = len(self.list_json())
        except:
            raise WriteStorageError

    def getItem(self, key):
        fname = self.__filename.format(key)
        if isfile(fname):
            with open(fname) as file:
                return load(file)

    def removeItem(self, key):
        fname = self.__filename.format(key)
        if isfile(fname):
            remove(fname)
        self.length = len(self.list_json())

    def clear(self):
        for fname in self.list_json():
            remove(fname)
        self.length = len(self.list_json())

    def key(self, index):
        if 0 <= index < self.length:
            _, key = split(self.list_json()[index])
            return key.replace(".json", "")


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class WriteStorageError(BaseError):
    message = "Could not serialize the data"
