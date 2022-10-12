import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://dahyejang:sparta@cluster0.xcw2jeh.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        number = movie.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        score = movie.select_one('td.point').text
        doc = {
             'title':title,
             'number':number,
             'score':score
        }

        db.movies.insert_one(doc)

     