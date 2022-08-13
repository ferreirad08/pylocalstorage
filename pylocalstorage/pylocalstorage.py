from os.path import split, abspath, isfile
from json import load, dumps
from glob import glob
from os import remove


class LocalStorage:

    __version__ = "1.1.0"
    __pathname = None
    __filename = None
    __regex = None
    length = 0

    def __init__(self):
        # Getting PATH of file
        self.__pathname, _ = split(abspath(__file__))
        self.__filename = self.__pathname + "/{}.json"
        self.__regex = self.__pathname + "/*.json"
        self.length = len(glob(self.__regex))

    def setItem(self, key, value):
        try:
            value_str = dumps(value)
            with open(self.__filename.format(key), "w") as file:
                print(value_str, file=file)
            self.length = len(glob(self.__regex))
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
        self.length = len(glob(self.__regex))

    def clear(self):
        for fname in glob(self.__regex):
            remove(fname)
        self.length = len(glob(self.__regex))

    def key(self, index):
        if 0 <= index < self.length:
            _, key = split(glob(self.__regex)[index])
            return key.replace(".json", "")


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class WriteStorageError(BaseError):
    message = "Unable to save data"
