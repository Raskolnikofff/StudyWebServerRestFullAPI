from aiohttp import web
from routes import setup_routes
import viewsORM
from os import rename, remove,path
from ORM import opendb, Students


def help_open():
    testData = [Students(id=1, name='name1', surname='surname1'),
                Students(id=2, name='name2', surname='surname2'),
                Students(id=3, name='name3', surname='surname3')]
    if path.isfile('studentsoncourse.db'):
        rename('studentsoncourse.db', 'studentsoncourseConst.db')
    session = opendb()
    session.add_all(testData)
    session.commit()
    session.close()
    app = web.Application()
    setup_routes(app)
    return app


def help_close():
    remove('studentsoncourse.db')
    if path.isfile('studentsoncourseConst.db'):
        rename('studentsoncourseConst.db', 'studentsoncourse.db')


async def test_to_json():
    st = Students(id=1, name='name1', surname='surname1')
    assert viewsORM.to_json(st) == dict(id=1, name='name1', surname='surname1')


async def test_postinfo():
    pass


async def test_gethandler(aiohttp_client):
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.get('/students')
    help_close()
    assert resp.status == 200
    text = await resp.text()
    testtext1 = '[{"id": 1, "name": "name1", "surname": "surname1"}, '
    testtext2 = '{"id": 2, "name": "name2", "surname": "surname2"}, '
    testtext3 = '{"id": 3, "name": "name3", "surname": "surname3"}]'
    testtext = testtext1 + testtext2 + testtext3
    assert testtext == text


async def test_getidhandler(aiohttp_client):
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.get('/students/2')
    help_close()
    assert resp.status == 200
    text = await resp.text()
    assert '[{"id": 2, "name": "name2", "surname": "surname2"}]' == text


async def test_postidhandler(aiohttp_client):
    params = {'name': 'name4', 'surname': 'surname4'}
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.post('/students/2', data=params)
    help_close()
    assert resp.status == 409
    text = await resp.text()
    assert 'user with this id exists' == text
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.post('/students/4', data=params)
    help_close()
    assert resp.status == 200
    text = await resp.text()
    assert '[{"id": 4, "name": "name4", "surname": "surname4"}]' == text


async def test_deleteidhandler(aiohttp_client):
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.delete('/students/3')
    help_close()
    assert resp.status == 204


async def test_putidhandler(aiohttp_client):
    params = {'name': 'name5', 'surname': 'surname5'}
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.put('/students/5', data=params)
    help_close()
    assert resp.status == 200
    text = await resp.text()
    assert '[{"id": 5, "name": "name5", "surname": "surname5"}]' == text
    app = help_open()
    client = await aiohttp_client(app)
    resp = await client.post('/students/4', data=params)
    help_close()
    assert resp.status == 200
    text = await resp.text()
    assert '[{"id": 4, "name": "name5", "surname": "surname5"}]' == text
