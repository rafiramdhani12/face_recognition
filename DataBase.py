import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://face-recognition-8aea5-default-rtdb.asia-southeast1.firebasedatabase.app"
})

ref = db.reference("Students")

data = {
    "456784" : 
        {
            "name": "Perrel brown",
            "major": "Edgings",
            "starting_year" : 2017,
            "total_attendance" : 6,
            "standing" : "G",
            "year" : 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "696969" : 
        {
            "name": "aku raja",
            "major": "Edgings",
            "starting_year" : 2017,
            "total_attendance" : 6,
            "standing" : "G",
            "year" : 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
    
}

# unzip the json
for key,value in data.items():
    ref.child(key).set(value)
