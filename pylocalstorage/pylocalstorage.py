import os
import pickle


class LocalStorage:
    __version__ = "1.4.0"

    path = __file__.replace("main.py", "buffer/")

    def __init__(self) -> None:
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def setItem(self, key, value) -> None:
        try:
            with open(f"{self.path}{key}.p", "wb") as pfile:
                pickle.dump(value, pfile)
        except:
            raise WriteStorageError

    def getItem(self, key):
        fname = f"{self.path}{key}.p"

        if os.path.isfile(fname):
            with open(fname, "rb") as pfile:
                return pickle.load(pfile)

    def removeItem(self, key) -> None:
        fname = f"{self.path}{key}.p"

        if os.path.isfile(fname):
            os.remove(fname)

    def clear(self) -> None:
        for name in os.listdir(self.path):
            os.remove(f"{self.path}{name}")

    def key(self, index: int) -> str:
        if isinstance(index, int) and 0 <= index < self.length:
            return os.listdir(self.path)[index][:-2]

    @property
    def length(self):
        return len(os.listdir(self.path))


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class WriteStorageError(BaseError):
    message = "Could not serialize the data"
