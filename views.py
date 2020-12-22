from aiohttp import web
import asyncio
import os

def to_json(string):
    a=['id','name','surname']
    string=string.split()
    data=dict(zip(a,string))
    return (data)

async def postinfo(request):
        data = await request.post()
        name=data['name']
        surname=data['surname']
        return name,surname

def gethandler(request):
    with open('DataBase.txt') as dbfile:
        data = list()
        for user in dbfile:
            data.append(to_json(user))
    return web.json_response(data)

def getidhandler(request):
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            data=to_json(user)
            if user.split()[0]==request.match_info['id']:
                return web.json_response(data)

async def postidhandler(request):
    a=''
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            a+=user
            if user.split()[0]==request.match_info['id']:
                return web.Response(status=409,text='user with this id exists')
    with open('DataBase.txt','w') as dbfilewr:
            data=await postinfo(request)
            newstud=request.match_info['id']+' '+data[0]+' '+data[1]
            print(a+newstud,file=dbfilewr)
    with open('DataBase.txt') as dbfile:
        return web.json_response(to_json(dbfile.readlines()[-1]))

async def putidhandler(request):
    id=request.match_info['id']
    info=await postinfo(request)
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            if user.split()[0]==id:
                pass
        else:
            return  os.system("curl -X POST -d 'name={}&surname={}' http://0.0.0.0:8080/students/{}".format(info[0],info[1],id))

def deleteidhandler(request):
    a=''
    with open('DataBase.txt') as dbfile:
        for user in dbfile:
            if user[0] == request.match_info['id']:
                with open('DataBase.txt', 'w') as dbfilewr:
                    b=dbfile.read()
                    print((a+b)[:-1],file=dbfilewr)
            a+=user
    return 

