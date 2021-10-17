
import os
import time

import requests
import sys

with open('../all_tickers.txt','r') as f:
	texte = f.read().split('\n')
while True:
	for index,symbol in enumerate(texte):
		if not os.path.isfile('../data/'+symbol+'_daily.csv'):

			API_URL = "https://www.alphavantage.co/query?"
	
			data = {
    "function": "TIME_SERIES_DAILY", 
    "symbol": symbol,
    'outputsize':'full', 
    "datatype": "csv",
    "apikey": "P00XHSMNO0X6Z0NG", # IE2IUZIANAQI1KV6 # P00XHSMNO0X6Z0NG
	}
			response = requests.get(API_URL, data)
			if "Error Message" in response.text:
				continue
			if '"Note"' in response.text:
				print(response.text)
				break
			with open('../data/'+symbol+'_daily.csv','w') as f:
				f.write(response.text)
			print(index,len(texte),index/float(len(texte))*100.)
			time.sleep(15)
		else:
			print(symbol,' exist yet')

	time.sleep(15)
