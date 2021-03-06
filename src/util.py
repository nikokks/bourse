import pandas as pd
from sklearn import preprocessing
import numpy as np
from src.ADX import *
from src.RSI import *
#history_points = 200


def csv_to_dataset(csv_path,history_points):

    data = pd.read_csv(csv_path)
    #data = data.drop('timestamp', axis=1)
    data = data.drop('timestamp', axis=1)
    data = data.drop(0, axis=0)
    data = data[[ 'open', 'high', 'low', 'close',
       'volume']]
    print('columns name',data.columns)
    data = data.values

    data_normaliser = preprocessing.MinMaxScaler()
    data_normalised = data_normaliser.fit_transform(data)

    # using the last {history_points} open close high low volume data points, predict the next open value
    ADX_3cols = ADX(data_normalised)
    RSI =  get_rsi(data_normalised[:,3],14)
    print('shape(RSI)',RSI.shape)
    print('input shapes',data_normalised.shape,ADX_3cols.shape)
    data_normalised = np.column_stack((data_normalised,ADX_3cols))
    ohlcv_histories_normalised = np.array([data_normalised[i:i + history_points].copy() for i in range(len(data_normalised) - history_points)])

    print(ohlcv_histories_normalised.shape,'test')



    next_day_open_values_normalised = np.array([data_normalised[:, 0][i + history_points].copy() for i in range(len(data_normalised) - history_points)])
    next_day_open_values_normalised = np.expand_dims(next_day_open_values_normalised, -1)

    next_day_open_values = np.array([data[:, 0][i + history_points].copy() for i in range(len(data) - history_points)])
    next_day_open_values = np.expand_dims(next_day_open_values, -1)

    y_normaliser = preprocessing.MinMaxScaler()
    y_normaliser.fit(next_day_open_values)

    def calc_ema(values, time_period):
        # https://www.investopedia.com/ask/answers/122314/what-exponential-moving-average-ema-formula-and-how-ema-calculated.asp
        sma = np.mean(values[:, 3])
        ema_values = [sma]
        k = 2 / (1 + time_period)
        for i in range(len(his) - time_period, len(his)):
            close = his[i][3]
            ema_values.append(close * k + ema_values[-1] * (1 - k))
        return ema_values[-1]

    technical_indicators = []
    print('shape(ohlcv_histories)',ohlcv_histories_normalised.shape)
    for his in ohlcv_histories_normalised:
        # note since we are using his[3] we are taking the SMA of the closing price
        sma = np.mean(his[:, 3])
        sma_20 = np.mean(his[-20:,3])
        sma_10 = np.mean(his[-10:,3])
        ema_12 = calc_ema(his, 12)
        ema_26 = calc_ema(his, 26)
        diff_sma_t20 = sma - sma_20
        diff_sma_t10 = sma - sma_10
        diff_sma_20_10 = sma_20 - sma_10
        ema_20 = calc_ema(his, 20) 
        ema_50 = calc_ema(his, 50)
        macd_20_50 = ema_20 - ema_50
        macd_12_26 = ema_12 - ema_26
        #technical_indicators.append(np.array([sma]))
        technical_indicators.append(np.array([sma,sma_20,sma_10,ema_12,ema_26,diff_sma_t20,diff_sma_t10,diff_sma_20_10,macd_20_50,ema_20,ema_50,macd_12_26]))

    technical_indicators = np.array(technical_indicators)
    tech_ind_scaler = preprocessing.MinMaxScaler()
    technical_indicators_normalised = tech_ind_scaler.fit_transform(technical_indicators)

    assert ohlcv_histories_normalised.shape[0] == next_day_open_values_normalised.shape[0] == technical_indicators_normalised.shape[0]
    return ohlcv_histories_normalised, technical_indicators_normalised, next_day_open_values_normalised, next_day_open_values, y_normaliser


def multiple_csv_to_dataset(test_set_name,history_points):
    import os
    ohlcv_histories = 0
    technical_indicators = 0
    next_day_open_values = 0
    for csv_file_path in list(filter(lambda x: x.endswith('daily.csv'), os.listdir('./'))):
        if not csv_file_path == test_set_name:
            print(csv_file_path)
            if type(ohlcv_histories) == int:
                ohlcv_histories, technical_indicators, next_day_open_values, _, _ = csv_to_dataset(csv_file_path)
            else:
                a, b, c, _, _ = csv_to_dataset(csv_file_path)
                ohlcv_histories = np.concatenate((ohlcv_histories, a), 0)
                technical_indicators = np.concatenate((technical_indicators, b), 0)
                next_day_open_values = np.concatenate((next_day_open_values, c), 0)

    ohlcv_train = ohlcv_histories
    tech_ind_train = technical_indicators
    y_train = next_day_open_values

    ohlcv_test, tech_ind_test, y_test, unscaled_y_test, y_normaliser = csv_to_dataset(test_set_name)

    return ohlcv_train, tech_ind_train, y_train, ohlcv_test, tech_ind_test, y_test, unscaled_y_test, y_normaliser
