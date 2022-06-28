from os import path
from json import load, dumps


class LocalStorage:

    __version__ = "1.0.0"
    fname = None
    length = 0

    def __init__(self):
        # Getting PATH of file
        pathname, _ = path.split(path.abspath(__file__))
        self.fname = path.join(pathname, "localstorage.json")
        if not path.isfile(self.fname):
            self.write_json({})

    def setItem(self, key, value):
        data = self.read_json()
        data[key] = value
        self.write_json(data)

    def getItem(self, key):
        data = self.read_json()
        return data.get(key)

    def removeItem(self, key):
        data = self.read_json()
        del data[key]
        self.write_json(data)

    def clear(self):
        self.write_json({})

    def key(self, index):
    	data = self.read_json()
    	return list(data.keys())[index]

    def read_json(self):
        with open(self.fname, "r") as file:
            return load(file)

    def write_json(self, data):
        with open(self.fname, "w") as file:
            print(dumps(data), file=file)
        self.length = len(data)
