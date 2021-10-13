import os
for i in ['FBK','Gold','AMZN','IBM','GOOGL']:
	for j in [50,200]:
		for k in [0.1,0.2,0.5]:	
			os.system('python3.6 trading_algo.py '+i+' '+str(j)+' '+str(k))
