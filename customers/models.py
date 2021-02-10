from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql

Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    surname = sql.Column(sql.String)
