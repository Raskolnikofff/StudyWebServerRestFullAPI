from customers.models import Base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sql


def to_jsonORM(studobject):
    a = ['id', 'name', 'surname']
    userdict = list()
    userdict.append(studobject.id)
    userdict.append(studobject.name)
    userdict.append(studobject.surname)
    data = dict(zip(a, userdict))
    return data


def to_json(string):
    a = ['id', 'name', 'surname']
    string = string.split()
    data = dict(zip(a, string))
    return (data)


async def postinfo(request):
    data = await request.post()
    name = data['name']
    surname = data['surname']
    return name, surname


def opendb():
    engine = sql.create_engine('sqlite:///studentsoncourse.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


# Help lines

'''session = opendb()
session.add_all([
    Students(name='11', surname='111'),
    Students(name='22', surname='222'),
    Students(name='333', surname='333'),
])
session.commit()

session = opendb()
a = session.query(Students).filter_by(id=3)
for i in a:
    print(i.name)
session.close()'''
