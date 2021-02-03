from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql

Base = declarative_base()


def opendb():
    engine = sql.create_engine('sqlite:///studentsoncourse.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


class Students(Base):
    __tablename__ = 'students'

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    surname = sql.Column(sql.String)


# Help lines
'''
%He
session = opendb()
session.add_all([
    Students(name='11', surname='111'),
    Students(name='22', surname='222'),
    Students(name='333', surname='333'),
])
session.commit()

session = opendb()
a = session.query(Students).filter_by(id=3)
for i in a:
    print(i.name)'''
