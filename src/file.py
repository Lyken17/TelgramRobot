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
    content["token"] = "110949338:AAHIcJhOAg2okKjuTTcy0VCwZEoqjeoqTUs"
    content["last_update_id"] = 519396914
    updateConfig(file, config=content)



