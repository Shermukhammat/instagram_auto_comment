import sqlite3
from .tables import creat_tables
from .comment_answers import CommentAnswersData, CommentAnswer
from .photo import  PhotoData
from .params import Params

class DataBase(PhotoData, CommentAnswersData, Params):
    def __init__(self, path : str, yaml_path : str = 'data/params.yaml') -> None:
        creat_tables(path)
        PhotoData.__init__(self, path)
        CommentAnswersData.__init__(self, path)
        Params.__init__(self, yaml_path)