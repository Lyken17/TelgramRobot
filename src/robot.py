import requests

class Robot():


    # Lyken = 18010983
    # Frantic = 66583516
    # RotTryGroup = -90936966
    def __init__(self, token = " "):
        self.token =  "110949338:AAHIcJhOAg2okKjuTTcy0VCwZEoqjeoqTUs"

    def getMe(self):
        url = self.base_url + "/getMe"
        r = requests.get(url)
        print(r.text)

    def getUpdates(self):
        method = "getUpdates"
        res = requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method),
            data = {'offset' : 519396902}
        ).json()
        print(res)

    def sendMessage(self, chat_id = 18010983, text=''):
        if len(text) == 0:
            print("input error")
            exit(-1)

        method = "sendMessage"
        res = requests.post(
            url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, method),
            data = {'chat_id' : chat_id, 'text' : text}
        ).json()
        print(res)

    def test(self):
        self.sendMessage(chat_id = -90936966, text = 'hi')
        # self.getUpdates()