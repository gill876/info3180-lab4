from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)

# Config Values
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
