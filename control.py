import requests
from config import TOKEN



respons = requests.post("https://shermuhammad.uz/comment", params={'token' : TOKEN,
                                                                  'instagram_url' : "https://www.instagram.com/reel/DBEn_rmOmn7/",
                                                                  "code" : "kino",
                                                                  "movi_url" : "https://t.me/FilmBufferBot?star=12"})

#18297879247205820
# respons = requests.delete("https://shermuhammad.uz/comment", params={'token' : TOKEN,
#                                                                   'id':"18297879247205820"})
# respons = requests.delete("https://shermuhammad.uz/comment", params={'token' : TOKEN, "id" : "18063770626711667"})

print(respons.status_code)
print(respons.text)