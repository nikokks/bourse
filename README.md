# Stock Trading with Machine Learning

## Overview

A stock trading bot that uses machine learning to make price predictions.

## Requirements

-   Python 3.5+
-   alpha_vantage
-   pandas
-   numpy
-   sklearn
-   keras
-   tensorflow
-   matplotlib

## Documentation

[Blog Post](https://yacoubahmed.me/blog/stock-prediction-ml)

[Medium Article](https://medium.com/towards-data-science/getting-rich-quick-with-machine-learning-and-stock-market-predictions-696802da94fe)

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
* A- ajouter de le delta des bourses du meme type fermées plus tot
* B- faire les algos sur les moyenne boursieres pour voir si elles sont plus certaines
* C- [ajouter des indicateurs en input](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)
### MOYEN TERME
* C- faire une prediction analyse multi dimensionnelle paralelle aux autres cours boursier presents en meme temps
* D- faire un transformer-decoder pour predire le cours boursier apres option C

### LONG TERME
* E- ajouter des lstm et GRU en sortie du decoder
* F- ajouter lanalyse de sentiment de la journée precedente et courante (tout depend si l'algo vend/achete en fin/debut de journée)

# TO READ 'SEARCH ON GOOGLE'

- predict stock prices
- indicators prediction
- indicators prediction time series
- methods for stock prices
- methods for quantitative finance
- algorithmic trading


### SAHRABIA A DECORTIQUER

- Issu d'une formation supérieure en informatique Bac+2 à Bac+5, tu maîtrises le protocole FIX, les VWAP, TWAP, les Iceberg et autres stop suiveurs. Bref la base.... et même un peu plus que la base. Dans l’idéal, tu as une expérience d’environ 3 à 10 ans soit en salle des marchés soit chez un ISV (FIS / SUNGARD, ITIVITY / ULLINK, FIDESSA ou n’importe quel autre éditeur de solution de passage d’ordre) en tant qu'ingénieur / support technique, TAM et/ou support fonctionnel.

- Depuis la relation avec les traders à la gestion des projets d'accès marchés en passant par le suivi des ISV, des memberships, de l'OMS, des onboardings en DMA / BSA, etc.


