from config import INSTAGRAM_TOKEN
from data import CommentAnswer, DataBase
from .entry import WebhookEntry
import requests, re 


def answer_to_comment(entry : WebhookEntry, comment_answer : CommentAnswer, storage : DataBase):
    if storage.MY_INSTAGRAM_ID == entry.change_id:
        return
    
    answer = storage.get_comment_answer_by_media_id(entry.media.id)
    
    if answer and is_code_exsit(entry.text, answer.code):
        private_reply(entry.change_id, f"Kino likni: {comment_answer.url}")
        
        if storage.PUBLIC_REPLAY_ALLOW:
            public_replay(entry.change_id, f"profilingizga kino liknin yubordik")    



def private_reply(comment_id : str, message : str, token : str = None):
    params = {'access_token' : INSTAGRAM_TOKEN}
    data = {"recipient": {"comment_id": comment_id},
            "message": {"text": message}}

    respond = requests.post(f"https://graph.instagram.com/v20.0/me/messages", params=params, json=data) 
    if respond.status_code == 200:
        return True
    return False


def public_replay(comment_id : int, message : str):
    params = {'access_token': INSTAGRAM_TOKEN}
    data = {"message": message}
    
    respond = requests.post(f"https://graph.instagram.com/v20.0/{comment_id}/replies", params = params, json = data)
    if respond.status_code == 200:
        return True
    return False



def is_code_exsit(comment : str, code : str):
    if re.search(code, comment.lower()):
        return True
    return False