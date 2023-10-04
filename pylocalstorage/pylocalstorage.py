from json import dumps, loads
from os.path import split, abspath

from sqlalchemy import create_engine, text


class LocalStorage:

    __version__ = "1.3.0"
    __engine = None
    length = 0

    def __init__(self) -> None:
        # Getting PATH of file
        pathname, _ = split(abspath(__file__))
        self.__engine = create_engine(f"sqlite:///{pathname}/localStorage.db")
        with self.__engine.begin() as connection:
            connection.execute(text("""
            CREATE TABLE IF NOT EXISTS LocalStorage (
                key TEXT UNIQUE,
                value TEXT
            );
            """))
        self.__update_length()

    def setItem(self, key, value) -> None:
        try:
            value_str = dumps(value)
            with self.__engine.begin() as connection:
                connection.execute(text(f"""
                INSERT INTO LocalStorage (key, value)
                VALUES ('{key}','{value_str}')
                ON CONFLICT(key) DO UPDATE SET value = '{value_str}';
                """))
            self.__update_length()
        except:
            raise WriteStorageError

    def getItem(self, key):
        with self.__engine.begin() as connection:
            result = list(connection.execute(text(f"""
            SELECT value
            FROM LocalStorage
            WHERE key = '{key}';
            """)))
        if result:
            return loads(result[0][0])

    def removeItem(self, key) -> None:
        with self.__engine.begin() as connection:
            connection.execute(text(f"""
            DELETE FROM LocalStorage
            WHERE key = '{key}';
            """))
        self.__update_length()

    def clear(self) -> None:
        with self.__engine.begin() as connection:
            connection.execute(text("""
            DELETE FROM LocalStorage;
            """))
        self.__update_length()

    def key(self, index: int):
        if isinstance(index, int) and 0 <= index < self.length:
            with self.__engine.begin() as connection:
                result = list(connection.execute(text("""
                SELECT key
                FROM LocalStorage;
                """)))
            return result[index][0]

    def __update_length(self) -> None:
        with self.__engine.begin() as connection:
            result = list(connection.execute(text("""
            SELECT COUNT(*) FROM LocalStorage;
            """)))
        self.length = result[0][0]


class BaseError(Exception):
    """Base class for other exceptions"""
    message: str = None

    def __init__(self) -> None:
        class_name = self.__class__.__name__
        super().__init__(f"{class_name}(message={self.message})")


class WriteStorageError(BaseError):
    message = "Could not serialize the data"
