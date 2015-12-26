'''
This is about file operations.
'''
import json

def loadConfig(file):
    with open(file, 'r') as fp:
        content = json.load(fp)
        print content


def updateConfig(file, config):
    with open(file,'w') as fp:
        json.dump(config, fp)

def initConfig(file):
    content = []



