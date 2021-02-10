from aiohttp import web
from aiohttpproject.urls import setup_routes

if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host='127.0.0.1')
