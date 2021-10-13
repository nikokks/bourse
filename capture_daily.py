
import os
import time

import requests
import sys

symbol =  str(sys.argv[1])
print(symbol)
API_URL = "https://www.alphavantage.co/query?"
data = {
    "function": "TIME_SERIES_DAILY", 
    "symbol": symbol,
    'outputsize':'full', 
    "datatype": "csv",
    "apikey": "P00XHSMNO0X6Z0NG",
}
response = requests.get(API_URL, data)
with open('data/'+symbol+'_daily.csv','w') as f:
	f.write(response.text)
