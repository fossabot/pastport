from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    name = Column(String(40), nullable = False)
    email = Column(String(100), nullable = False)
    # Allow google and facebook login but also have a custom one
    password = Column(String(30), nullable = False)
    id = Column(Integer, primary_key = True)
    # Zip Code
    # Language
    # Online/Offline - Allow a user to never connect with other users

    @property
    def serialize(self):
       return {
            'name'              : self.name,
            'email'             : self.email,
      }

class Place(Base):
    __tablename__ = 'places'
    name = Column(String(40), nullable = False)
    address = Column(String(40), nullable = False)
    id = Column(Integer, primary_key = True)
    # coordinates
    # Hours, or for event the days it happens
    # Price Range - Good time to Great time (Cheap price to balling out)
        # No $ or bullshit like that. Just a range of pricees
        # Good time - Restaurant. Entree, Drink
        # Balling out - Restaurant. Appetizer, Entree, 2 Drinks, Dessert
    # Location(City, State,Country)

    @property
    def serialize(self):
       return {
            'name'              : self.name,
            'address'           : self.address,
      }

class PlaceType(Base):
    __tablename__ = 'placetypes'
    category = Column(String(10), nullable = False)
    # Customized by users but they can request new ones when creating.
    # Select from drop down list and then open a text box
    # Food/Drink, Outdoor Active, Event, Indoor Active, Shopping, Sight,
    # Manage sub categories
    place_id = Column(Integer, ForeignKey(Place.id))
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
       return {
            'category'              : self.type,
            'place_id'          : self.place_id,
      }

class Interaction(Base):
    __tablename__ = 'interactions'
    personal_name = Column(String(100))

    # TODO: Is boolean an option
    completed = Column(Integer, nullable = False)
    interest = Column(Integer, nullable = False)
    notes = Column(String(100))
    place_id = Column(Integer, ForeignKey(Place.id))
    user_id = Column(Integer, ForeignKey(Users.id), nullable = False)
    id = Column(Integer, primary_key = True)
    # Time spent
    # Clothing: Harcore, Athletic, Swimwear, Casual, Business Casual, Formal, Black Tie
    # Cost
    # Data and time
    # Weather auto lookup if it is an outdoor activity
    # Cloudy, sunny, rainy
    # Temperature

    @property
    def serialize(self):
       return {
            'completed'         : self.completed,
            'personal_name'     : self.personal_name,
            'interest'          : self.interest,
            'notes'             : self.notes,
            'place_id'          : self.place_id,
            'user_id'           : self.user_id,
      }

# class PlannedInteraction(Base):
#     __tablename__ = 'plannedinteractions'
#     notes = Column(String(100))
#     place_id = Column(Integer, ForeignKey(Place.id))
#     user_id = Column(Integer, ForeignKey(Users.id))
#     id = Column(Integer, primary_key = True)
#
#     @property
#     def serialize(self):
#        return {
#             'notes'             : self.notes,
#             'place_id'          : self.place_id,
#             'user_id'           : self.user_id,
#       }

engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')
Base.metadata.create_all(engine)
