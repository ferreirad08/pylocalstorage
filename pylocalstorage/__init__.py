try:
    from sqlalchemy import create_engine
except:
    from os import system
    system("pip install SQLAlchemy==1.4.46")

from .pylocalstorage import LocalStorage, WriteStorageError
