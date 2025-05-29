import requests
from libs.openexchange import OpenExchangeClient
import os
from dotenv import load_dotenv

load_dotenv()

app_key=os.getenv("EXCHANGE_API_KEY")

client =OpenExchangeClient(app_id=app_key)

usd_amount=1000
gbp_amount=client.converter(usd_amount,"USD","GBP")

print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')