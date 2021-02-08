from aiohttp import web


async def to_json(string):
    a = ['id', 'name', 'surname']
    string = string.split()
    data = dict(zip(a, string))
    return data


async def postinfo(request):
    data = await request.post()
    name = data['name']
    surname = data['surname']
    return name, surname


async def gethandler(request):
    with open('DataBase.txt') as dbfile:
        data = list()
        for user in dbfile:
            data.append(await to_json(user))
    return web.json_response(data)


async def getidhandler(request):
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            data = await to_json(user)
            if user.split()[0] == request.match_info['id']:
                return web.json_response(data)


async def postidhandler(request):
    a = ''
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            a += user
            if user.split()[0] == request.match_info['id']:
                return web.Response(
                    status=409,
                    text='user with this id exists'
                )
    with open('DataBase.txt', 'w') as dbfilewr:
        data = await postinfo(request)
        newstud = request.match_info['id'] + ' ' + data[0] + ' ' + data[1]
        print(a + newstud, file=dbfilewr)
    with open('DataBase.txt') as dbfile:
        return web.json_response(await to_json(dbfile.readlines()[-1]))


def deleteidhandler(request):
    a = ''
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            if user[0] == request.match_info['id']:
                with open('DataBase.txt', 'w') as dbfilewr:
                    b = dbfile.read()
                    print((a + b)[:-1], file=dbfilewr)
                    return web.Response(status=204)
            a += user
    return


async def putidhandler(request):
    id = request.match_info['id']
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            if user.split()[0] == id:
                await deleteidhandler(request)
    return await postidhandler(request)
