import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'Followers'
    id = Column(Integer, primary_key=True)        
    from_id = Column(Integer, ForeignKey('Users.id'))
    to_id = Column(Integer, ForeignKey('Users.id'))
    user_from_id = relationship('Users',ForeignKey=[from_id], backref='Follower')
    user_to_id = relationship('Users',ForeignKey=[to_id], backref='Followed')


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    city = Column(String)

    def to_dict(self):
        return{
            "id" : self.id,
            "email" : self.email,
            "city" : self.city
        }


class Posts(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('Users', backref='Posts')


class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('Users', backref='Comments')
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship('Posts', backref='Comments')

class Medias(Base):
    __tablename__ = 'Medias'
    id = Column(Integer, primary_key=True)
    src = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    post = relationship('Posts', backref='Medias')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
