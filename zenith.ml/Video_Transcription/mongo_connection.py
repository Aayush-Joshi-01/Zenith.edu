from pymongo import MongoClient
from bson import ObjectId

connection_string="mongodb+srv://ronakchhabra:ruro1234@ronakchhabra.tvgeidk.mongodb.net/?retryWrites=true&w=majority&appName=Ronakchhabra"
client = MongoClient(connection_string)  
db = client["test"]  
videos = db["videos"] 
# course= db[""]


def find_video_data(id):
    print(id)
    data=list(videos.find({"_id":ObjectId(id)}))[0]
    if data:
        return data,True
    return None, False

def add_transcript(id, data, transcript):
    data["Trascribe"]=transcript
    videos.update_one({"_id":ObjectId(id)},{"$set":data})
    