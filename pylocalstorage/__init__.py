from .pylocalstorage import LocalStorage, WriteStorageError
from os import system

try:
    from sqlalchemy import create_engine
except:
    system("pip install SQLAlchemy")
    from sqlalchemy import create_engine

