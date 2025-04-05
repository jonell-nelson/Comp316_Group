from flask import Flask, request, make_response
import mysql.connector

db_config = {
    "user" : "-----",
    "password":"-----",
    "host": "-----",
    "database": "-----"
}

app = Flask(__name__)

@app.route('/', methods=[''])
def hello_world():
    return "hello world"


@app.route('/register_user', methods=['GET'])
def register_user():
    pass