from mcrcon import MCRcon

host = "localhost"
password = "1111"
port = 25575

def runCommand(command):
    with MCRcon(host, password, port) as mcr:
        return mcr.command(command)
    
def checkList():
    rawListPlayer = runCommand('list').split()[10:]
    listPlayer = []

    for each in rawListPlayer:
        if '§' in each:
            continue
    
        each = each.replace(',', '')

        listPlayer.append(each)
    
    formattedList = []

    for index, item in enumerate(listPlayer, start=1):
        line = f'{index}. <code>{item}</code>'
        formattedList.append(line)

    return '\n'.join(formattedList)


def checkRawList():
    rawListPlayer = runCommand('list').split()[10:]
    listPlayer = []

    for each in rawListPlayer:
        if '§' in each:
            continue
    
        each = each.replace(',', '')

        listPlayer.append(each)

    return listPlayer


def everyPlayerGlow():
    runCommand('effect give @a minecraft:glowing 10 0 true')

def everyPlayerKill():
    runCommand('kill @a')

def playerKill(nickname):
    runCommand(f'kill {nickname}')