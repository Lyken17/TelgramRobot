from robot import *
import file
import json
from datetime import datetime
import time




fp = "config/robot.json"
# file.initConfig(fp)
config = file.loadConfig(fp)



bot = Robot(config)
# bot.sendMessage(text="now is " + str(datetime.now()))

while True:
    res = bot.receiveNewMessage()
    time.sleep(2)

# print (res)