import os
import sqlite3

from flask import Flask

db_file = os.getenv('DATABASE_FILE', 'test.db')
db = sqlite3.connect(db_file)
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
