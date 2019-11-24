from flask import Flask

app = Flask(__name__)

from app.routes import mod

app.register_blueprint(mod)