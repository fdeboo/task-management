import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager" # optional
app.config["MONGO_URI"] = "mongodb+srv://root:patch2488@mycluster-qtjor.mongodb.net/task_manager?retryWrites=true&w=majority"

mongo = PyMongo(app) # Instance of PyMongo


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == "__main__":
    app.run(debug=True)