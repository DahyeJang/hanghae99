from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://dahyejang:sparta@cluster0.xcw2jeh.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'score':'0'}})

movie = db.movies.find_one({'title':'가버나움'})

print (movie)

