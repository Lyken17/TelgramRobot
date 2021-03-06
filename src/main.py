import sys
import time
import os

from src.robot import *
import src.file as file
from src.my_decorator import *

def test(a=1):
    pass

def main():

    fp = 'config/robot.json'
    # file.initConfig(fp)
    config = file.loadConfig(fp)

    bot = Robot(config)
    # bot.sendMessage(text="now is " + str(datetime.now()))

    try:
        while True:
            res = bot.receiveNewMessage()
            time.sleep(2)

    except KeyboardInterrupt:
        config['last_update_id'] = bot.last_update_id
        file.updateConfig(fp, config)
        print("Program terminated by user, config has been updated")


if __name__ == '__main__':
    print(os.getcwd())
    main()
    # main()