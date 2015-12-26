from robot import *
import file
import json

fp = "config/robot.json"
config = file.loadConfig(fp)
bot = Robot(config["taken"])
bot.test()