from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, make_response

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from flask import session as login_session

from flask import make_response

from . import app

from .database_setup import Base, User

# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/pastport/')
def showRestaurants():
  return make_response("Hello", 200)
