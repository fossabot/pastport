from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from . import app
from .db.models import Base, Users

engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
  return make_response("Hello", 201)

@app.route('/newuser', methods= ['POST'])
def newUser():
  req = request.json

  newName = req['name']
  newUser = Users(email = req['email'], name = newName)

  session.add(newUser)
  session.commit()
  print("Here")
  print(newUser.email)

  return make_response("Hello", 200)

@app.route('/users')
def getUsers():
  allUsers = session.query(Users).all()
  return jsonify(Users=[i.serialize for i in allUsers])

# TODO: Add Post method handler for editing the user
@app.route('/users/<int:user_id>', methods = ['GET', 'DELETE', 'POST'])
def getUser(user_id):
  if request.method == 'GET':
    userById = session.query(Users).filter_by(id = user_id).one()
    return jsonify(userById.serialize)

  if request.method == 'DELETE':
    userById = session.query(Users).filter_by(id = user_id).one()
    session.delete(userById)
    session.commit
    return make_response('', 204)

  if request.method == 'POST':
    return make_response('', 200)

@app.route('/users/<int:user_id>/interactions')
  def getPlaces(user_id):
    placesById = session.query(interactions).filter_by(user_id = user_id).all()
    return jsonify(Interactions=[i.serialize for i in placesById])

# TODO: Add Post method handler for editing the interaction
@app.route('/interactions/<int:interaction_id>', methods = ['GET', 'DELETE', 'POST'])
def getUser(interaction_id):
  if request.method == 'GET':
    interactionById = session.query(Interaction).filter_by(id = interaction_id).one()
    return jsonify(userById.serialize)

  if request.method == 'DELETE':
    interactionById = session.query(Interaction).filter_by(id = interaction_id).one()
    session.delete(interactionById)
    session.commit
    return make_response('', 204)

  if request.method == 'POST':
    return make_response('', 200)

# @app.route('/profile/')
# def showRestaurants():
#   return make_response("Hello", 200)
#
# @app.route('/login/')
# def showRestaurants():
#   return make_response("Hello", 200)
#
# @app.route('/newthing/')
# def showRestaurants():
#   return make_response("Hello", 200)
