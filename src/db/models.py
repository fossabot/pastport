from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    name = Column(String(40), nullable = False)
    email = Column(String(100), nullable = False)
    id = Column(Integer, primary_key = True)

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

    @property
    def serialize(self):
       return {
            'name'              : self.name,
            'address'           : self.address,
      }

class PlaceType(Base):
    __tablename__ = 'placetypes'
    type = Column(String(10), nullable = False)
    place_id = Column(Integer, ForeignKey(Place.id))
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
       return {
            'type'              : self.type,
            'place_id'          : self.place_id,
      }

class Interaction(Base):
    __tablename__ = 'interactions'
    personal_name = Column(String(100))
    interest = Column(Integer, nullable = False)
    notes = Column(String(100))
    place_id = Column(Integer, ForeignKey(Place.id))
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key = True)
    # Data and time
    # Weather auto lookup if it is an outdoor activity
    # Cloudy, sunny, rainy
    # Temperature

    @property
    def serialize(self):
       return {
            'personal_name'     : self.personal_name,
            'interest'          : self.interest,
            'notes'             : self.notes
            'place_id'          : self.place_id,
            'user_id'           : self.user_id,
      }

class PlannedInteraction(Base):
    __tablename__ = 'plannedinteractions'
    notes = Column(String(100))
    place_id = Column(Integer, ForeignKey(Place.id))
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
       return {
            'notes'             : self.notes
            'place_id'          : self.place_id,
            'user_id'           : self.user_id,
      }

engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')
Base.metadata.create_all(engine)
