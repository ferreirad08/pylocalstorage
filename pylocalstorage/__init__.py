try:
    import sqlalchemy
except:
    from os import system
    system("pip install SQLAlchemy")

from .localstorage import LocalStorage, WriteStorageError
