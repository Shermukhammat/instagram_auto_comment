from config import INSTAGRAM_TOKEN, proxies
from data import CommentAnswer, DataBase
from .entry import WebhookEntry
import requests, re 




def answer_to_comment(entry : WebhookEntry, comment_answer : CommentAnswer, storage : DataBase):
    if storage.MY_INSTAGRAM_ID == entry.change_id:
        return 
    
    if is_code_exsit(entry.text, comment_answer.code):
        if storage.SERVER:
            current_proxy = proxies
        else:
            current_proxy = None

        status = private_reply(entry.change_id, f"🎥 Kino havloasi: {comment_answer.url}", proxies=current_proxy)
        print(f"private replay status: {status}")
        if storage.PUBLIC_REPLAY_ALLOW:
            status = public_replay(entry.change_id, f"✅ Profilingizga kino havolasni yubordik", proxies=current_proxy)    
            print(f"public replay status: {status}")


def private_reply(comment_id : str, message : str, proxies : dict = None):
    params = {'access_token' : INSTAGRAM_TOKEN}
    data = {"recipient": {"comment_id": comment_id},
            "message": {"text": message}}
    
    try:
        respond = requests.post(f"https://graph.instagram.com/v20.0/me/messages", 
                            params=params, 
                            json=data, 
                            proxies = proxies,
                            timeout=5) 
        if respond.status_code == 200:
            return True
        
    except Exception as e:
        print(f"private_reply: {e}")

    return False


def public_replay(comment_id : int, message : str, proxies : dict = None):
    params = {'access_token': INSTAGRAM_TOKEN}
    data = {"message": message}
    
    try:
        respond = requests.post(f"https://graph.instagram.com/v20.0/{comment_id}/replies", 
                            params = params, 
                            json = data, 
                            proxies=proxies,
                            timeout=5)
        if respond.status_code == 200:
            return True
    except Exception as e:
        print(f"public_replay: {e}")
    
    return False


def is_code_exsit(comment : str, code : str):
    if type(code) == str and type(comment) == str:
        if code.strip().lower() == comment.strip().lower():
            return True
    return False