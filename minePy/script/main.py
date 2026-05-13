from mcrcon import MCRcon
from mcpi import minecraft

import time

import data
import handlers

mc = minecraft.Minecraft.create("localhost")

print('[Script] Скрипт сервера працює...')


host = "localhost"
password = "1111"
port = 25575


def runCommand(command):
    with MCRcon(host, password, port) as mcr:
        return mcr.command(command)


runCommand(r'scoreboard objectives setdisplay list blocksBroken')

runCommand(r'scoreboard objectives modify blocksBroken displayname "§lДобуто вугілля"')


while True:

    runCommand(r'setblock -9 -57 -9 minecraft:coal_ore')


    data.getData()

    handlers.commandCheck()

    time.sleep(0.1)