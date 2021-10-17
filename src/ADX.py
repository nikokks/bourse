import numpy as np
import pandas as pd

def get_adx(high, low, close, lookback):
    high = pd.DataFrame(high)
    low = pd.DataFrame(low)
    close = pd.DataFrame(close)
    #lookback = pd.DataFrame([lookback])

    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0

    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
    atr = tr.rolling(lookback).mean()

    plus_di = 100 * (plus_dm.ewm(alpha = 1/lookback).mean() / atr)
    minus_di = abs(100 * (minus_dm.ewm(alpha = 1/lookback).mean() / atr))
    dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
    adx = ((dx.shift(1) * (lookback - 1)) + dx) / lookback
    adx_smooth = adx.ewm(alpha = 1/lookback).mean()
    return plus_di, minus_di, adx_smooth


def ADX(array, interval: int=14):
  df = pd.DataFrame(array,columns=['open', 'High', 'Low', 'Adj Close', 'volume'])
  df['-DM'] = df['Low'].shift(1) - df['Low']
  df['+DM'] = df['High'] - df['High'].shift(1)
  df['+DM'] = np.where((df['+DM'] > df['-DM']) & (df['+DM']>0), df['+DM'], 0.0)
  df['-DM'] = np.where((df['-DM'] > df['+DM']) & (df['-DM']>0), df['-DM'], 0.0) 
  df['TR_TMP1'] = df['High'] - df['Low']
  df['TR_TMP2'] = np.abs(df['High'] - df['Adj Close'].shift(1))
  df['TR_TMP3'] = np.abs(df['Low'] - df['Adj Close'].shift(1))
  df['TR'] = df[['TR_TMP1', 'TR_TMP2', 'TR_TMP3']].max(axis=1)  
  df['TR'+str(interval)] = df['TR'].rolling(interval).sum()  
  df['+DMI'+str(interval)] = df['+DM'].rolling(interval).sum()
  df['-DMI'+str(interval)] = df['-DM'].rolling(interval).sum()  
  df['+DI'+str(interval)] = df['+DMI'+str(interval)] /   df['TR'+str(interval)]*100
  df['-DI'+str(interval)] = df['-DMI'+str(interval)] / df['TR'+str(interval)]*100
  df['DI'+str(interval)+'-'] = abs(df['+DI'+str(interval)] - df['-DI'+str(interval)])
  df['DI'+str(interval)] = df['+DI'+str(interval)] + df['-DI'+str(interval)]  
  df['DX'] = (df['DI'+str(interval)+'-'] / df['DI'+str(interval)])*100  
  df['ADX'+str(interval)] = df['DX'].rolling(interval).mean()
  df['ADX'+str(interval)] =   df['ADX'+str(interval)].fillna(df['ADX'+str(interval)].mean())  
  del df['TR_TMP1'], df['TR_TMP2'], df['TR_TMP3'], df['TR'], df['TR'+str(interval)]
  del df['+DMI'+str(interval)], df['DI'+str(interval)+'-']
  del df['DI'+str(interval)], df['-DMI'+str(interval)]
  del df['+DI'+str(interval)], df['-DI'+str(interval)]
  del df['DX']  
  return df[['-DM','+DM','ADX'+str(interval)]].values
