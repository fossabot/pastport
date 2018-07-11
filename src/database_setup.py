from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    name = Column(String(40), nullable = False)
    email = Column(String(100), nullable = False)
    picture = Column(String(250))
    id = Column(Integer, primary_key = True)


engine = create_engine('postgresql://zachlavallee:***@localhost:5432/pastport')

Base.metadata.create_all(engine)
