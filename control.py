import requests
from config import TOKEN



respons = requests.post("https://shermuhammad.uz/comment", params={'token' : TOKEN,
                                                                  'instagram_url' : "https://www.instagram.com/p/DA-3xjlumZb/",
                                                                  "code" : "+",
                                                                  "movi_url" : "https://t.me/FilmBufferBot?start=bot&code=7"})

# respons = requests.delete("https://shermuhammad.uz/comment", params={'token' : TOKEN, "id" : "18063770626711667"})

print(respons.status_code)
print(respons.text)