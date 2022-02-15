import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserData(Base):
    __tablename__ = "user_data"
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True, primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    token = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)


# class Chats(Base):
#     __tablename__ = "chats"
#     id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, primary_key=True, unique=True)
#     from_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
#     from_name = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
#     from_surname = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)



