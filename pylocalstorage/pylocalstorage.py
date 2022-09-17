from os.path import split, abspath
from sqlalchemy import create_engine
from json import dumps, loads


class LocalStorage:

    __version__ = "1.2.0"
    __engine = None
    length = 0

    def __init__(self) -> None:
        # Getting PATH of file
        pathname, _ = split(abspath(__file__))
        self.__engine = create_engine(f"sqlite:///{pathname}/localStorage.db")
        self.__engine.execute("""
        CREATE TABLE IF NOT EXISTS LocalStorage (
            key TEXT UNIQUE,
            value TEXT
        );
        """)
        self.length = self.__get_length()

    def setItem(self, key, value) -> None:
        try:
            value_str = dumps(value)
            self.__engine.execute(f"""
            INSERT INTO LocalStorage (key, value)
            VALUES ('{key}','{value_str}')
            ON CONFLICT(key) DO UPDATE SET value = '{value_str}';
            """)
            self.length = self.__get_length()
        except:
            raise WriteStorageError

    def getItem(self, key):
        result = list(self.__engine.execute(f"""
        SELECT value
        FROM LocalStorage
        WHERE key = '{key}';
        """))
        if result:
            return loads(result[0][0])

    def removeItem(self, key) -> None:
        self.__engine.execute(f"""
        DELETE FROM LocalStorage
        WHERE key = '{key}';
        """)
        self.length = self.__get_length()

    def clear(self) -> None:
        self.__engine.execute("""
        DELETE FROM LocalStorage;
        """)
        self.length = self.__get_length()

    def key(self, index: int):
        if isinstance(index, int) and 0 <= index < self.length:
            result = list(self.__engine.execute("""
            SELECT key
            FROM LocalStorage;
            """))
            return result[index][0]

    def __get_length(self) -> int:
        result = list(self.__engine.execute("""
        SELECT COUNT(*) FROM LocalStorage;
        """))
        return result[0][0]


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class WriteStorageError(BaseError):
    message = "Could not serialize the data"
