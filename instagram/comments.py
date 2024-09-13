from config import INSTAGRAM_TOKEN
from data import CommentAnswer, DataBase
from .entry import WebhookEntry
import requests, re 


def answer_to_comment(entry : WebhookEntry, comment_answer : CommentAnswer, storage : DataBase):
    if storage.MY_INSTAGRAM_ID == entry.change_id:
        return
    
    if is_code_exsit(entry.text, comment_answer.code):
        status = private_reply(entry.change_id, f"Kino likni: {comment_answer.url}")
        print(f"private replay status: {status}")
        if storage.PUBLIC_REPLAY_ALLOW:
            status = public_replay(entry.change_id, f"profilingizga kino liknin yubordik")    
            print(f"public replay status: {status}")


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