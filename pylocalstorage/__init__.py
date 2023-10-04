try:
    from sqlalchemy import create_engine
except:
    from os import system
    system("pip install SQLAlchemy")

from .pylocalstorage import LocalStorage, WriteStorageError
