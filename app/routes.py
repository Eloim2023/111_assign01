from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    me = {
        "first_name": "Eloim",
        "last_name": "Arreola",
        "hobbies": "reading books",
        "is_active": True
}
    return me

@app.post("/")
def create_entry():
    raw_data = request.json
    mylist.append(raw_data)
    return "", 204

@app.get("/entries")
def get_entries():
    return mylist
