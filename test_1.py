from aiohttp import web
from routes import setup_routes
import views


async def test_homepagehandler(aiohttp_client, loop):
    app = web.Application()
    setup_routes(app)
    client = await aiohttp_client(app)
    resp = await client.get('/students/2')
    assert resp.status == 200
    text = await resp.text()
    assert '{"id": "2", "name": "value1", "surname": "value2"}' == text


async def test_deleteidhandler(aiohttp_client, loop):
    app = web.Application()
    setup_routes(app)
    client = await aiohttp_client(app)
    resp = await client.delete('/students/2')
    assert resp.status == 200


async def test_to_json():
    assert await views.to_json('1 2 3') == dict(id='1', name='2', surname='3')
