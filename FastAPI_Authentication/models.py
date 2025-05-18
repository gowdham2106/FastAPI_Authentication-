from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
class Blog(Base):
    __tablename__='blog'
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
    creator=relationship("User", back_populates="blogs")
    user_id=Column(Integer, ForeignKey('user.id'))
    
class User(Base):
    __tablename__='user'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    blogs=relationship("Blog", back_populates="creator")