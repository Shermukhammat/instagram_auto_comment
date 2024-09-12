from fastapi import FastAPI
from config import TOKEN
from data import DataBase
from instagram import WebhookEntry


app = FastAPI()
db = DataBase('data/data.db')