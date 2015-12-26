'''
This is about file operations.
'''
import json

def loadConfig(file):
    with open(file, 'r') as fp:
        content = json.load(fp)
        return content

def updateConfig(file, config):
    with open(file,'w') as fp:
        json.dump(config, fp, indent=4)

def initConfig(file):
    content = {}
    content["taken"] = "110949338:AAHIcJhOAg2okKjuTTcy0VCwZEoqjeoqTUs"
    updateConfig(file, config=content)



