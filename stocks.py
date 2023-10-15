import requests
import os
from dotenv import load_dotenv

load_dotenv()


url = "https://live.trading212.com/api/v0/equity/history/orders"

# query = {
#     "cursor": "0",
#     "ticker": "string",
#     "limit": "20"
# }

headers = {"Authorization": os.environ["TRADING_API"]}

response = requests.get(url, headers=headers)

data = response.json()

print(response.status_code)

# headers = {"Authorization": os.environ["TRADING_API"]}

# response = requests.get(url, headers=headers, params=query)

# data = response.json()
# print(data)
