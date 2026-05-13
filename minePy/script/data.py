from mcrcon import MCRcon
from mcpi import minecraft

import json
import os

import commands


host = "localhost"
password = "1111"
port = 25575

def runCommand(command):
    with MCRcon(host, password, port) as mcr:
        return mcr.command(command)
    
# ————————————————————————————————————————————————————————————————————————————

dataPlayer = {}
rewardPlayer = {}

if os.path.exists('data_player.json'):
    with open('data_player.json', 'r') as f:
        dataPlayer = json.load(f)

def saveData():
    with open('data_player.json', 'w') as f:
        json.dump(dataPlayer, f)

if os.path.exists('reward_player.json'):
    with open('reward_player.json', 'r') as f:
        rewardPlayer = json.load(f)

def saveReward():
    with open ('reward_player.json', 'w') as f:
        json.dump(rewardPlayer, f) 

# ————————————————————————————————————————————————————————————————————————————

def getData():

    rawListPlayer = runCommand('list').split()[10:]
    listPlayer = []

    for each in rawListPlayer:
        if '§' in each:
            continue
    
        each = each.replace(',', '')

        listPlayer.append(each)

    saveData()
    saveReward()


    for each in listPlayer:
        if each not in rewardPlayer:
            rewardPlayer[each] = 0

        valuePlayer = int(runCommand(f'scoreboard players get {each} blocksBroken').split()[2])
        dataPlayer[each] = valuePlayer

        if valuePlayer >= 10 and rewardPlayer[each] == 0:
            
            rewardPlayer[each] = 1

            commands.getReward1(each)

        if valuePlayer >= 20 and rewardPlayer[each] == 1:

            rewardPlayer[each] = 2

            commands.getReward2(each)

            print('hell yeah')
        
        


