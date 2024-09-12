import requests
from loader import DataBase
from webhook import WebhookEntry


class Dispatcher:
    def __init__(self, token : str, storage : DataBase) -> None:
        self.TOKEN = token 

    def respond(self, entry : WebhookEntry):
        if entry.type == 'commit' and entry.text:
            entry.media.id

            

    