import requests

import os
from dotenv import load_dotenv

load_dotenv()

url=os.getenv("BASE_URL")
api_key=os.getenv("EXCHANGE_API_KEY")
headers = {"accept": "application/json"}

exchange_res=requests.get(f'{url}?app_id={api_key}',headers=headers)

print(exchange_res.json())

exchange_rates=exchange_res.json()["rates"]

for currency, rate in exchange_rates.items():
    print(f"{currency}: {rate}")