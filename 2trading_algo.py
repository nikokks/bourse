import numpy as np
from keras.models import load_model
from src.util import csv_to_dataset

import sys

symbol = str(sys.argv[1])
hist_data = int(sys.argv[2])
model = load_model('models/technical_model_'+symbol+'_h'+str(hist_data)+'.h5')
#model = load_model('basic_model.h5')
ohlcv_histories, technical_indicators, next_day_open_values, unscaled_y, y_normaliser = csv_to_dataset('data/'+symbol+'_daily.csv',hist_data)

test_split = 0.9
n = int(ohlcv_histories.shape[0] * test_split)
#n1 = int(ohlcv_histories.shape[0] * test_split + ohlcv_histories.shape[0] * test_split*0.2)

ohlcv_test = ohlcv_histories[n:]
tech_ind_test = technical_indicators[n:]
y_test = next_day_open_values[n:]
unscaled_y_test = unscaled_y[n:]
y_test_predicted = model.predict([ohlcv_test, tech_ind_test])
y_test_predicted = y_normaliser.inverse_transform(y_test_predicted)

delta = []
start = 0
end = -1
for ohlcv, ind in zip(ohlcv_test[start: end], tech_ind_test[start: end]):
            normalised_price_today = ohlcv[-1][0]
            normalised_price_today = np.array([[normalised_price_today]])
            price_today = y_normaliser.inverse_transform(normalised_price_today)
            ohlcv = np.reshape(ohlcv,(1,hist_data,8))
            ind = np.reshape(ind,(1,12))
            predicted_price_tomorrow = np.squeeze(y_normaliser.inverse_transform(model.predict([[ohlcv], [ind]])))

            delta.append(predicted_price_tomorrow - price_today)

dico_gains = {}

for thresh_min in np.linspace(0,1,100):
    for thresh_max in np.linspace(0,1,100):
        buys = []
        sells = []
        start = 0
        end = -1

        x = -1
        for index , (ohlcv, ind) in enumerate(zip(ohlcv_test[start: end], tech_ind_test[start: end])):
            if delta[index] < thresh_max:
                buys.append((x, price_today[0][0]))
            elif delta[index] > -thresh_min:
                sells.append((x, price_today[0][0]))
            x += 1
        print(f"buys: {len(buys)}")
        print(f"sells: {len(sells)}")
        print(f'hours: {x+1}')
        balance = 0
        minimum = 0
        index = 0
        def compute_earnings(buys_, sells_):
            global balance, minimum,index
            minimum = 0
            purchase_amt = 10
            stock = 0
            balance = 0
            while len(buys_) > 0 and len(sells_) > 0:
                if buys_[0][0] < sells_[0][0]:
                    # time to buy $10 worth of stock
                    balance -= purchase_amt
                    stock += purchase_amt / buys_[0][1]
                    buys_.pop(0)
                    if minimum> balance:
                        minimum = balance
                        index = x
                else:
                    # time to sell all of our stock
                    balance += stock * sells_[0][1]
                    stock = 0
                    sells_.pop(0)
            print(f"earnings: ${balance}")


        # we create new lists so we dont modify the original
        compute_earnings([b for b in buys], [s for s in sells])

        print('minimum:',minimum,'balance',balance)
        dico_gains[(thresh_min,thresh_max)]=[minimum,balance]

import pickle
with open('dataa.pkl','wb') as f:
	pickle.dump(dico_gains,f)
