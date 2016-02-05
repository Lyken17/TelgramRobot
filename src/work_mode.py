import sys
import time
import os

from src.robot import *
import src.file as file
from src.my_decorator import *

bot = None
fp = None

def work_mode(mode="repeat"):
    global bot, fp

    fp = '../config/robot.json'
    config = file.loadConfig(fp)
    bot = Robot(config)

    work = {
        "repeat" : __repeat__,
        "test" : __test__,
    }

    config = None
    work[mode](config)

def __test__(config=None):

    pass

def __repeat__(config=None):
    global bot, fp
    try:
        while True:
            res = bot.receiveNewMessage()
            time.sleep(2)
    except KeyboardInterrupt:
        config['last_update_id'] = bot.last_update_id
        file.updateConfig(fp, config)
        print("Program terminated by user, config has been updated")
    pass

if __name__ == "__main__":
    print(os.getcwd())
    work_mode(mode="repeat")
