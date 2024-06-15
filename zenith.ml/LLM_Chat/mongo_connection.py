from pymongo import MongoClient

connection_string="mongodb+srv://ronakchhabra:ruro1234@ronakchhabra.tvgeidk.mongodb.net/?retryWrites=true&w=majority&appName=Ronakchhabra"
client = MongoClient(connection_string)  
db = client["test"]  
videos = db["videos"] 


def find_course_transcribe(course_id):
    rows=list(videos.find({"CourseID":course_id}))
    print(rows)
    transcribes=[]
    print(type(course_id))
    for data in rows:
        print(data)
        transcribes.append(data["Trascribe"])
    return "".join(transcribes)

