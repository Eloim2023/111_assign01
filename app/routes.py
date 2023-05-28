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