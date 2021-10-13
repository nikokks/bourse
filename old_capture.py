
import os
import time

for year in ['1','2']:
	for month in [str(i) for i in range(1,13)]:
		import requests
		#minutes = '60min'
		API_URL = "https://www.alphavantage.co/query?"
		data = {
    "function": "TIME_SERIES_DAILY",  #TIME_SERIES_DAILY #TIME_SERIES_INTRADAY_EXTENDED
    "symbol": "GOOGL",
    'outputsize':'full', 
    "datatype": "csv",
    #'interval':minutes, # comment for DAILY
    'slice':'year'+year+'month'+month,
    "apikey": "P00XHSMNO0X6Z0NG",
    		}
		response = requests.get(API_URL, data)
		#with open('IBM'+year+'_'+month+'_'+minutes+'.csv','w') as f:
		with open('IBM'+year+'_'+month+'.csv','w') as f:
			f.write(response.text)
		time.sleep(15)
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&outputsize=full&apikey=P00XHSMNO0X6Z0NG&interval=1min&slice=year1month1
