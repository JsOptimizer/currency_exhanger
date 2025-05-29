from dotenv import load_dotenv
import os
import requests

load_dotenv()

headers = {"accept": "application/json"}

class OpenExchangeClient:
    BASE_URL=os.getenv("BASE_URL")
    def __init__(self,app_id)->None:
        self.app_id=app_id
        pass

    @property
    def latest(self)->dict:
        return requests.get(f'{self.BASE_URL}?app_id={self.app_id}',headers=headers).json()
    
    def converter(self,from_amount,from_currency,to_currency):
        rates=self.latest["rates"]
        to_rate=rates[to_currency]
        if from_currency=="USD":
            return from_amount*to_rate
        else:
            from_in_usd=from_amount/rates[from_currency]
            return from_in_usd*to_rate


