from src.robot import *
import src.file as file
from src.decorator import *

import json
from datetime import datetime

import time

@protect
@logger
def test(a=1):
    print('test is running')
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
    test(1)
    # main()