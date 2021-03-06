from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, make_response
from flask import session as login_session
from flask_hashing import Hashing
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from . import app
hashing = Hashing(app)
salt = 'salt'

from .db.models import Base, Users, Interaction

engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
  return make_response("Hello", 201)


@app.route('/users')
def getUsers():
  allUsers = session.query(Users).all()
  return jsonify(Users=[i.serialize for i in allUsers])

@app.route('/users/new', methods= ['POST'])
def newUser():
  req = request.json

  newName = 'tempName'
  email = req['email']
  if session.query(Users).filter_by(email = email).scalar() != None:
    return make_response("User already exists", 401)

  password = hashing.hash_value(req['password'], salt=salt)
  newUser = Users(email = email, password = password, name = newName)

  session.add(newUser)
  session.commit()

  return make_response("Hello", 200)

# TODO: Add Post method handler for editing the user
@app.route('/users/<int:user_id>', methods = ['GET', 'DELETE', 'POST'])
def getUser(user_id):
  # Return specific user
  if request.method == 'GET':
    userById = session.query(Users).filter_by(id = user_id).one()
    return jsonify(userById.serialize)

  # Delete specific user
  if request.method == 'DELETE':
    userById = session.query(Users).filter_by(id = user_id).one()
    session.delete(userById)
    session.commit()
    return make_response('', 204)

  #TODO
  # Edit specific user
  if request.method == 'POST':
    req = request.json
    userById = session.query(Users).filter_by(id = user_id).one()
    userById.email = req['email']
    session.commit()
    return make_response('', 200)

@app.route('/users/<int:user_id>/interactions', methods = ['GET', 'POST'])
def getInteractions(user_id):
  # Get specific interaction by user_id
  if request.method == 'GET':
    placesById = session.query(Interaction).filter_by(user_id = user_id).all()
    return jsonify(Interactions=[i.serialize for i in placesById])

  # New interaction by user_id
  if request.method == 'POST':
    req = request.json

    isCompleted = req['completed']
    newInterest = req['interest']
    newPersonalName = req['personal_name']
    newInteraction = Interaction(personal_name = newPersonalName, interest = newInterest, user_id = user_id, completed = isCompleted)

    session.add(newInteraction)
    session.commit()
    return make_response('', 204)

# TODO: Add Post method handler for editing the interaction
@app.route('/interactions/<int:interaction_id>', methods = ['GET', 'DELETE', 'POST'])
def getInteraction(interaction_id):
  interactionById = session.query(Interaction).filter_by(id = interaction_id).one()
  # Get inteaction by interaction_id
  if request.method == 'GET':
    return jsonify(interactionById.serialize)

  # Delete interaction by interaction_id
  if request.method == 'DELETE':
    session.delete(interactionById)
    session.commit
    return make_response('', 204)

  #TODO:
  # Edit interaction by interaction_id
  if request.method == 'POST':
    req = request.json
    interactionById.completed = req['completed']
    session.commit()
    return make_response('', 200)

# @app.route('/profile/')
# def showRestaurants():
#   return make_response("Hello", 200)

@app.route('/login', methods = ['GET'])
def showRestaurants():
  user = request.args['email']
  password = request.args['password']

  username = session.query(Users).filter_by(email = user).scalar()
  if username == None:
    print('nothin')
    return make_response('Invalid Email', 401)

  if not hashing.check_value(username.password, password, salt):
    return make_response('Invalid Password', 401)

  return make_response(jsonify(cookie='123ABC'), 200)


# @app.route('/newthing/')
# def showRestaurants():
#   return make_response("Hello", 200)
