from aiohttp import web
from views import homepagehandler, gethandler, getidhandler,\
    putidhandler, postidhandler, deleteidhandler


def setup_routes(app):
    app.add_routes([
        web.get('/', homepagehandler),
        web.get('/students', gethandler),
        web.get('/students/{id}', getidhandler),
        web.put('/students/{id}', putidhandler),
        web.post('/students/{id}', postidhandler),
        web.delete('/students/{id}', deleteidhandler)
    ])
