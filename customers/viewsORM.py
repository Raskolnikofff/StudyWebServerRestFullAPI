from aiohttp import web
from customers.models import Students
from customers.fictures import opendb
from customers.fictures import to_jsonORM, postinfo


def gethandler(request):
    session = opendb()
    data = list()
    for user in session.query(Students).all():
        data.append(to_jsonORM(user))
    session.close()
    return web.json_response(data)


def getidhandler(request):
    session = opendb()
    user = session.query(Students).filter_by(id=request.match_info['id']).one_or_none()
    if user is not None:
        data = [to_jsonORM(user)]
        session.close()
        return web.json_response(data)


async def postidhandler(request):
    session = opendb()
    user = session.query(Students).filter_by(id=request.match_info['id']).one_or_none()
    if user is not None:
        session.close()
        return web.Response(status=409, text='user with this id exists')
    data = await postinfo(request)
    newstud = Students(id=request.match_info['id'], name=data[0], surname=data[1])
    session.add(newstud)
    session.commit()
    session.close()
    return getidhandler(request)


def deleteidhandler(request):
    statuscode = 0
    session = opendb()
    user = session.query(Students).filter_by(id=request.match_info['id']).one_or_none()
    if user is not None:
        session.delete(user)
        statuscode = 204
        session.commit()
    session.close()
    return web.Response(status=statuscode)


async def putidhandler(request):
    id = request.match_info['id']
    session = opendb()
    user = session.query(Students).filter_by(id=id).one_or_none()
    session.close()
    if user is not None:
        deleteidhandler(request)
    return await postidhandler(request)
