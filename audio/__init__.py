from flask import Flask
from mykey import mypass
app = Flask(__name__)
app.secret_key = mypass
from audio import routes
