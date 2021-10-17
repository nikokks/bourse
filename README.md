
## Installation

1. Clone the repo
2. Pip install the requirements `pip install -r requirements.txt`

## Download Data

python3.6 capture_daily.py with hyperparameter symbol hist_data

## Training model

python3.6 tech_ind_model.py symbol hist_data

## inference earning in trading

python3.6 trading_algo.py symbol hist_data thresh

# IDEAS TO PERFOM ALGO

### COURT TERME 
* 0 - ajouter la serie temporelle RS , see in RSI.py
* A- ajouter de le delta des bourses du meme type fermées plus tot
* B- faire les algos sur les moyenne boursieres pour voir si elles sont plus certaines
* C- [ajouter des indicateurs en input](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)
* D- ajouter les booleen de conditions des amx ema macd rsi des liens suivants: https://python.plainenglish.io/trading-using-python-average-directional-index-adx-aeab999cffe7
 
### MOYEN TERME
* C- faire une prediction analyse multi dimensionnelle paralelle aux autres cours boursier presents en meme temps
* D- faire un transformer-decoder pour predire le cours boursier apres option C

### LONG TERME
* E- ajouter des lstm et GRU en sortie du decoder
* F- ajouter lanalyse de sentiment de la journée precedente et courante (tout depend si l'algo vend/achete en fin/debut de journée)

# TO READ 'SEARCH ON GOOGLE'
- see [indicators on this website](https://www.alphavantage.co/documentation/)
- best indicators for decision stock market
- predict stock prices
- indicators prediction
- indicators prediction time series
- methods for stock prices
- methods for quantitative finance
- algorithmic trading

# TO IMPLEMENT IN CODE
### TO DO
* [codes_indicators](https://gist.github.com/whittlem?)
### DONE
* DONE [ADX](https://python.plainenglish.io/trading-using-python-average-directional-index-adx-aeab999cffe7)


# AMELIORATIONS
* faire une recherche d'hyperparametres sur les parametres
* faire une recherche dhyperparamter sur les threeshold pour optimiser les ventes

# INDICATORS DONE
* ema
* sma
* adx
* macd
* rsi

# NE PAS OUBLIER DE PREDIRE SUR LES 5 prochains mois soit 5*20

