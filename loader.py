from fastapi import FastAPI
from config import TOKEN, INSTAGRAM_TOKEN
from data import DataBase, CommentAnswer
from instagram import WebhookEntry, Dispatcher


app = FastAPI()
db = DataBase('data/data.db')
dp = Dispatcher(INSTAGRAM_TOKEN, db)