import requests as rq

from cryptoApi import HEADERS, URL_SPECIFIC_EXCHANGE

class APIError(Exception):
    pass

class CrytoValueModel:
    def __init__(self, origin : str = "", destination : str = ""):
        self.origin = origin
        self.destination = destination
        self.rate = None


    def getRate(self):
        self.answer = rq.get(URL_SPECIFIC_EXCHANGE.format(self.origin, self.destination), headers = HEADERS)
        
        if self.answer.status_code != 200:
            raise APIError(self.answer.json()["error"])
        self.rate = self.answer.json()["rate"]

    def calculate(self, amount):
        return self.rate * float(amount)

