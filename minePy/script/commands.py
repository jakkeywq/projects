from mcrcon import MCRcon
import data

host = "localhost"
password = "1111"
port = 25575

def runCommand(command):
    with MCRcon(host, password, port) as mcr:
        return mcr.command(command)
    
# ————————————————————————————————————————————————————————————————————————————

def clearScore(player):
    runCommand(fr'scoreboard players set {player} blocksBroken 0')

def giveFood(player):
    runCommand(fr'give {player} minecraft:pumpkin_pie')

def giveTool(player):
    runCommand(fr'give {player} minecraft:iron_pickaxe{{CanDestroy:[coal_ore], Unbreakable:1}}')
    
def giveRocket(player):
    runCommand(fr'give {player} minecraft:firework_rocket')

def setTime(time):
    if time == 'day':
        runCommand(r'time set day')

    if time == 'night':
        runCommand(r'time set midnight')

    if time == 'evening':
        runCommand(r'time set 12500')

def checkLevel(player):
    level = data.rewardPlayer[player]
    runCommand(fr'tellraw {player} ["",{{"text":"[] ","color":"gray"}},{{"text":"\u0412\u0438 \u0434\u043e\u0441\u044f\u0433\u043b\u0438 "}},{{"text":"{level} \u0440\u0456\u0432\u043d\u044f!","bold":true,"color":"#A294F9"}}]')

# ————————————————————————————————————————————————————————————————————————————

def getReward1(player):
    
    runCommand(fr'playsound minecraft:entity.experience_orb.pickup master {player}')
    runCommand(fr'tellraw {player} ["",{{"text":"[]","color":"gray"}},{{"text":" \u0412\u0438 \u043e\u0442\u0440\u0438\u043c\u0430\u043b\u0438 "}},{{"text":"\u043d\u0430\u0433\u043e\u0440\u043e\u0434\u0443...","bold":true,"color":"#A294F9"}}]')

    runCommand(fr'item replace entity {player} armor.chest with minecraft:elytra{{Unbreakable:1}}')

def getReward2(player):

    runCommand(fr'playsound minecraft:entity.experience_orb.pickup master {player}')
    runCommand(fr'tellraw {player} ["",{{"text":"[]","color":"gray"}},{{"text":" \u0412\u0438 \u043e\u0442\u0440\u0438\u043c\u0430\u043b\u0438 "}},{{"text":"\u043d\u0430\u0433\u043e\u0440\u043e\u0434\u0443...","bold":true,"color":"#A294F9"}}]')

    runCommand(fr'give {player} minecraft:stick 1')


# ————————————————————————————————————————————————————————————————————————————

def checkList():
    rawListPlayer = runCommand('list').split()[10:]
    listPlayer = []

    for each in rawListPlayer:
        if '§' in each:
            continue
    
        each = each.replace(',', '')

        listPlayer.append(each)

        return listPlayer