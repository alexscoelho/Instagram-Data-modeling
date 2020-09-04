import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    account_type = Column(String(250), nullable=False)


    # one to many relationship with comments, here parent
    sent_comments = relationship("Comment", backref="user_commenting", foreign_keys=["Comment.user_commenting_id"])
    recieved_comments = relationship("Comment", backref="user_commented", foreign_keys=[ "Comment.user_commented_id"])

    # one to many relationship with direct message, here parent
    sent_messages = relationship("Direct_message", backref="user_sending_message", foreign_keys=["Direct_message.user_sending_message_id"])
    recieved_messages = relationship("Direct_message", backref="user_receiving_message", foreign_keys=[ "Direct_message.user_receiving_message_id"])

    # one to many relationship with following, here parent
    follower = relationship("Follows", backref="user_following", foreign_keys=["Follows.follower_id"])
    followed = relationship("Follows", backref="user_followed", foreign_keys=[ "Follows.followed_id"])

    # one to many relationship with post, here parent
    children = relationship("Post", back_populates="user")
    

class Follows(Base):
    __tablename__ = 'follows'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    # One to many relationship, here child
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    media = Column(String(250), nullable=False)

    # # one to many relationship, child
    post_user_id = Column(Integer, ForeignKey('user.id'))
    parent = relationship("User", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)

    # One to many relationship, here child
    user_commenting_id = Column(Integer, ForeignKey('user.id'))
    user_commented_id  = Column(Integer, ForeignKey('user.id'))
    

class Direct_message(Base):
    __tablename__ = 'direct message'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    message = Column(String(250), nullable=False)
    new_message = Column(Boolean, nullable=False)

    # One to many relationship, here child
    user_sending_message_id = Column(Integer, ForeignKey('user.id'))
    user_receiving_message_id  = Column(Integer, ForeignKey('user.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')