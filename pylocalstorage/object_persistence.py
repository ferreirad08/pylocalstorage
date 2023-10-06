import os

from pickle import dump, load


class ObjectPersistence:

    __path = __file__.replace("newfile.py", "buffer/")
    os.system(f"mkdir -p {__path}")

    def setItem(self, key, arg):
        self.removeItem(key)

        with open(f"{self.__path}{key}.pkl", "wb") as pklfile:
            dump(arg, pklfile)

    def getItem(self, key):
        fname = f"{self.__path}{key}.pkl"

        if os.path.exists(fname):
            with open(fname, "rb") as pklfile:
                return load(pklfile)

    def removeItem(self, key):
        os.system(f"rm -f {self.__path}{key}.pkl")

    def clear(self):
        os.system(f"rm -rf {self.__path} && mkdir {self.__path}")


if __name__ == "__main__":
    op = ObjectPersistence()

    op.setItem("test", 1.2)
    op.clear()
    op.setItem("test", "Hello")
    print(op.getItem("test"))

    op.removeItem("test")
    print(op.getItem("test"))
