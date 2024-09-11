import sqlite3

if __name__ == '__main__':
    from photo import PhotoData
else:
    from .photo import  PhotoData

class DataBase(PhotoData):
    def __init__(self, path : str) -> None:
        PhotoData.__init__(self, path)