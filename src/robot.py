import requests

class Robot():

    lastMessageID = 0

    # Lyken = 18010983
    # Frantic = 66583516
    # RotTryGroup = -90936966
    def __init__(self, config):
        t
        if len(token) < 10:
            print("token error")
            exit(-1)
        self.token = token

    def makeRequests(self, method, data={}):
        return requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method),
            data = data
        ).json()

    def getMe(self):
        url = self.base_url + "/getMe"
        r = requests.get(url)
        print(r.text)

    def getUpdates(self, offset=0 ):
        method = "getUpdates"
        res = requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method),
            data = {'offset':519396914}
        ).json()
        print(res)

    def receiveMessage(self):

        pass

    def receiveNewMessage(self):

        pass

    def sendMessage(self, chat_id = -90936966, text=''):
        if len(text) == 0:
            print("input error")
            exit(-1)

        method = "sendMessage"
        data = {'chat_id' : chat_id, 'text' : text}

        res = self.makeRequests(method=method, data=data)
        print (res)
        return res

    def test(self):
        self.sendMessage(chat_id = -90936966, text = 'hi')
        # self.getUpdates()