from flask import Flask, json
from pymongo import MongoClient
from urllib.parse import urlencode
import settings
from os import environ


USER = environ['DB_USER']
PASS = environ['DB_PASSWORD']
HOST = environ['DB_HOST']
NAME = environ['DB_NAME']
PORT = environ['PORT']
app = Flask(__name__)


##### MongoDB ####
params = {
    "retryWrites" : "true",
    "w" : "majority",
    "ssl" : "true",
    "ssl_cert_resq" : "CERT_NONE"
    }

client = MongoClient("mongodb+srv://" + USER + ":" + PASS + "@"  + HOST + "/" + NAME + "?" + urlencode(params))
db = client

##################

@app.route("/")
def hello_flask():
    return  '<h1>Hola Mundo</h1>'

@app.route("/users")
def twitterUsers():
    users = [
        {'name' : 'ManuMariani_'},
        {'name' : 'eantech'},
        {'name' : 'TinchoLutter'},
        {'name' : 'bitcoinArg'}        
        ]
    response = app.response_class(response = json.dumps(users),status = 200, mimetype = 'application/json')
    return response
    
@app.route("/users/<path>")
def searchUsers(path):
    '''
    if path == "people":
        return "ACA VA UN JSON DE PERSONAS"
    elif path == "company":
        return "ACA VA UN JSON DE EMPRESAS"
    else:
        return "UPPS... NO PUEDO BUSCAR LO QUE ESTAS PIDIENDO :("

    '''
    if path not in ["people","company", "all"]:
        return "UPPS... NO PUEDO BUSCAR LO QUE ESTAS PIDIENDO :("
    
    data = db['PDD-MJ-N-287']
    test = data['twitter']
    
    if path == 'all':
        users = test.find().limit(10)
    else:
        users = test.find({"type" : path}).limit(10)
    
    
    
    result = []
    
    for user in users:
        item = {
            'usuario' : user['name']
            }
        
        result.append(item)
    
    response = app.response_class(response = json.dumps(result),status = 200, mimetype = 'application/json')
    
    return response
 
@app.route("/test")
def test():
    data = db['PDD-MJ-N-287']
    test = data['twitter']
    
    users = test.find()
    
    for user in users:
        print(user)
     
    
    return 'Mira la consola...'

@app.route("/tweets/<user>/<limit>")
def filterUsers(user,limit):
    data = db['PDD-MJ-N-287']
    twitter = data['twitter']
    
    if limit != None and limit.isnumeric():
        limit = int(limit)
    else:
        response = {
             'ok' : False,
             'msg': "ERROR: No puede realizarse la busqueda :"
            }
        return app.response_class(response = json.dumps(response), status = 404, mimetype = 'application/json' )
        
    tweets = twitter.find({"in_reply_to_screen_name" : user}).limit(limit)
    
    response=[]
    
    for tweet in tweets:
        item = {
             'id' :tweet['id_str'],
             'user' : tweet['in_reply_to_screen_name'],
             'tweet' : tweet['full_text'] 
            }
        response.append(item)                 
    return app.response_class(response = json.dumps(response), status = 200, mimetype = 'application/json' )

    
app.run(port = PORT, host = '0.0.0.0')
