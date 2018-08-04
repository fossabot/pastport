from flask import Flask

def init_app():
    application = Flask(__name__)
    return application

app = init_app()
