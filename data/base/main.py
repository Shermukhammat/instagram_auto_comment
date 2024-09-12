import sqlite3
from .tables import creat_tables
from .comment_answers import CommentAnswersData, CommentAnswer

if __name__ == '__main__':
    from photo import PhotoData
else:
    from .photo import  PhotoData

class DataBase(PhotoData, CommentAnswersData):
    def __init__(self, path : str) -> None:
        creat_tables(path)
        PhotoData.__init__(self, path)
        CommentAnswersData.__init__(self, path)