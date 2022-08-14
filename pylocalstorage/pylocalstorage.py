from os.path import split, abspath, isfile, exists
from os import remove, mkdir
from json import load, dumps
from glob import glob


class LocalStorage:

    __version__ = "1.1.0"
    __filename = None
    length = 0

    def __init__(self):
        # Getting PATH of file
        pathname, _ = split(abspath(__file__))
        pathname += "/data"
        if not exists(pathname):
            mkdir(pathname)
        self.__filename = pathname + "/{}.json"
        self.list_json = lambda: glob(pathname + "/*.json")
        self.update_length = lambda: len(self.list_json())
        self.length = self.update_length()

    def setItem(self, key, value):
        try:
            value_str = dumps(value)
            with open(self.__filename.format(key), "w") as file:
                print(value_str, file=file)
            self.length = self.update_length()
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
        self.length = self.update_length()

    def clear(self):
        for fname in self.list_json():
            remove(fname)
        self.length = self.update_length()

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
