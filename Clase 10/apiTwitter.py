import tweepy
from pprint import pprint

claves = open ('E:/Curso/clavesTwiter.txt')
keys = [clave.split(';') for clave in claves]

consumer_key = keys[0][0]
consumer_secret = keys[1][0]
access_token = keys[2][0]
access_token_secret = keys[3][0]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#%%
#Mi perfil
usuario = api.me()
pprint(usuario._json)
#Otro usuario
otro_usuario = api.get_user('ManuMariani_')
pprint(otro_usuario._json)
#%%
#Seguidores (devuelve 20 porque es el resultado paginado)
seguidores = api.followers(screen_name = 'ManuMariani_')
for seguidor in seguidores:
    print(seguidor._json['name'])
#%%
#Si quiero mas de 20 resultados
for amigo in tweepy.Cursor(api.friends, screen_name = 'ManuMariani_').items(50):
    nombre = amigo._json['screen_name']
    print(nombre)
#%%
#los twits que posteo un usuario
contador = 1
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'alferdez', tweet_mode = 'extended').items(20):
    try:    
        print(contador, 'esto es un RT')
        pprint(tweet._json['retweeted_status']['text'])
    except:
        print(contador)
        pprint(tweet._json['full_text'])
    contador +=1
#%%
for tweet in tweepy.Cursor(api.search, q = 'music', tweet_mode = 'extended').items(20):
    print(tweet._json['full_text'])