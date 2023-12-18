import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' :"https://faceattendance-e11f7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1BG21CS083":
        {
            "name": "Shriddhi Shetty",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 3,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1BG21CS088":
        {
            "name": "Spandana Kamkar",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 5,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1BG21CS089":
        {
            "name": "Spoorthi N P",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 1,
            "year": 2,
            "last_attendance_time": "2023-03-15 00:54:34"
        },
    "1BG21CS091":
        {
            "name": "Srinisha S J",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1BG21CS092":
        {
            "name": "Srushti Sanjay",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 2,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1BG21CS101":
        {
            "name": "Tanisha N",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 8,
            "year": 2,
            "last_attendance_time": "2023-03-15 00:54:34"
        },
    "1BG21CS106":
        {
            "name": "Vaishnavi P S",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1BG21CS119":
        {
            "name": "Yukta B N",
            "course": "CSE",
            "starting_year": 2022,
            "total_attendance": 8,
            "year": 2,
            "last_attendance_time": "2023-03-15 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)