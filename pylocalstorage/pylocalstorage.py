from os.path import split, abspath
from sqlalchemy import create_engine

engine = None


def init():
    # Getting PATH of file
    pathname, _ = split(abspath(__file__))
    global engine
    engine = create_engine(f"sqlite:///{pathname}/localStorage.db", echo=False)
    engine.execute("""
    CREATE TABLE IF NOT EXISTS LocalStorage (
        key TEXT,
        value TEXT
    );
    """)

def getItem():
    result = list(engine.execute("""
    SELECT value
    FROM LocalStorage
    WHERE key = 'name';
    """))
    if result:
        return result[0][0]


def setItem():
    if getItem() is None:
        engine.execute("""
        INSERT INTO LocalStorage (key, value)
        VALUES ('name','SendCommand');
        """)
    else:
    	engine.execute("""
        UPDATE LocalStorage
        SET value = 'HDMIMonitorTest'
        WHERE key = 'name';
        """)


def removeItem():
    engine.execute("""
    DELETE FROM LocalStorage
    WHERE key = 'name';
    """)


def key(index):
    result = list(engine.execute("""
    SELECT key
    FROM LocalStorage;
    """))
    if result:
        return result[index][0]


def clear():
    engine.execute("""
    DELETE FROM LocalStorage;
    """)


init()
setItem()
print(getItem())
setItem()
print(getItem())
print(key(0))
removeItem()
clear()
print(getItem())
