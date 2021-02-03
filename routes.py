from aiohttp import web
from viewsORM import gethandler,getidhandler,putidhandler,postidhandler,deleteidhandler

def setup_routes(app):
        app.add_routes([
            web.get('/students',gethandler),
            web.get('/students/{id}',getidhandler),
            web.put('/students/{id}',putidhandler),
            web.post('/students/{id}',postidhandler),
            web.delete('/students/{id}',deleteidhandler)
            ])
