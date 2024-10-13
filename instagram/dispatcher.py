from .entry import WebhookEntry
from .comments import answer_to_comment
from data import DataBase
from .types import Field


class Dispatcher:
    def __init__(self, token : str, storage : DataBase) -> None:
        self.TOKEN = token 
        self.storage = storage

    async def respond(self, entry : WebhookEntry):
        if entry.type == Field.comments and type(entry.text) == str:
            comment_answer = self.storage.get_comment_data(entry.media.id)
            if comment_answer:
                # print(comment_answer.get_row_data())
                answer_to_comment(entry, comment_answer, self.storage)