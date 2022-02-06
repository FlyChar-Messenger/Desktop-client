import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserData(Base):
    __tablename__ = "user_data"
    id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, unique=True, primary_key=True)
    token = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)


# class Chats(Base):
#     __tablename__ = "chats"
#     id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, primary_key=True, unique=True)
#     from_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
#     from_name = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
#     from_surname = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)



