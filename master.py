import requests
import json

# Clean server

data = dict()
data['user'] = 'HOla_k_ase'

respuesta = requests.post(url='http://192.168.48.236:5000/new_player',
                          data=data)


print('Let the game begin')

input("Waiting for players to connect")

# Get players from server
# players =




