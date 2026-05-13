import requests
import random

import resources


account_id = 1260042234

class Player():
    def __init__(self, id):
        self.id = id

    def player_matches(self, id):
        return f'https://steamcommunity.com/profiles/{self.id}'

player = Player(1260042234)
def responseGet(url):
    response = requests.get(url)
    data = response.json()
    return data


def verifySteamID(id):
    if responseGet(f"https://api.opendota.com/api/players/{id}"):
        return True
    else:
        return False


# ———————————————————————————————————————————————————————————

def PlayerMatchesGet(id):
    info = responseGet(player.player_matches(id))
