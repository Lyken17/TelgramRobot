import requests

class Robot():

    last_update_id = 0
    token = 0

    # Lyken = 18010983
    # Frantic = 66583516
    # RotTryGroup = -90936966
    def __init__(self, config):
        if len(config["token"]) < 10:
            print("token error")
            exit(-1)

        self.token = config["token"]
        self.last_update_id = config["last_update_id"]

    def makeRequests(self, method, data={}):
        return requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method),
            data = data
        ).json()

    def getMe(self):
        url = self.base_url + "/getMe"
        r = requests.get(url)
        print(r.text)

    def getUpdates(self, offset = 0):
        method = "getUpdates"
        data = {'offset': offset}
        return self.makeRequests(method = method, data = data)


    def receiveMessage(self, offset):
        res = self.getUpdates(offset=self.last_update_id)
        pass

    def receiveNewMessage(self):
        res = self.getUpdates(offset=self.last_update_id)

        content = {}
        if not res['ok']:

            return res

        content['ok'] = True
        print(res)
        for each in res['result']:
            
            message = each['message']
            chat_id = message['chat']['id']
            person = message['from']['username']
            text = message['text']
            
            send_text = "Repeat : [ " + text + " ] from " + person
            self.sendMessage(chat_id=chat_id, text=send_text)

            self.last_update_id = each['update_id'] + 1

        pass



    def sendMessage(self, chat_id = -90936966, text=''):

        if len(text) == 0:
            print("input error")
            exit(-1)

        method = "sendMessage"
        data = {'chat_id' : chat_id, 'text' : text}

        return self.makeRequests(method = method, data = data)

    def autorun(self):
        pass

    def test(self):
        self.sendMessage(chat_id = -90936966, text = 'hi')
