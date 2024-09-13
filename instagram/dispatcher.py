from loader import DataBase
from .entry import WebhookEntry
from .comments import answer_to_comment

class Dispatcher:
    def __init__(self, token : str, storage : DataBase) -> None:
        self.TOKEN = token 
        self.storage = storage

    def respond(self, entry : WebhookEntry):
        if entry.type == 'comments' and entry.text:
            comment_answer = self.storage.get_comment_data(entry.media.id)
            if comment_answer:
                answer_to_comment(entry, comment_answer, self.storage)




            

    