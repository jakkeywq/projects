from mcpi import minecraft
import commands


mc = minecraft.Minecraft.create("localhost")

commandList = {
    'clear': commands.clearScore, # 1
    'eat': commands.giveFood,
    'tool': commands.giveTool,
    'fly': commands.giveRocket,
    'level': commands.checkLevel,

    'time': commands.setTime, # 2
}

def commandCheck():

    chatEvents = mc.events.pollChatPosts()

    for event in chatEvents:

        message = event.message
        player = mc.entity.getName(event.entityId)

        if message.startswith('p!'):
            command = message[2:].strip().split()

            cmd = command[0]

            if len(command) == 1:

                if cmd in commandList:
                    commandList[cmd](player)

            if len(command) == 2:
                
                request = command[1]

                if cmd in commandList:
                    commandList[cmd](request)


