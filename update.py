import pandas as pd
import requests
from datetime import datetime
from dateutil import tz
import os

CRYPTO_SYMBOL_NAMES = {
  'ADA': "Cardano", 
  'AVAX': "Avalanche", 
#   'BNB': "Binance Coin", 
#   'BTC': "Bitcoin", 
#   # 'BUSD': "Binance USD", 
#   'CRO': "Crypto.com Coin", 
#   'DOGE': "Dogecoin", 
#   'DOT': "Polkadot", 
#   'ETH': "Ethereum", 
#   # 'LINK': "Chainlink", 
#   # 'LTC': "Litecoin", 
#   'LUNA1': "Terra", 
#   'MATIC': "Polygon", 
#   'SHIB': "SHIBA INU", 
#   'SOL1': "Solana", 
#   # 'USDC': "USD Coin", 
#   # 'USDT': "Tether",
#   # 'UNI': "Uniswap",
#   # 'WBTC': "Wrapped Bitcoin", 
#   'XRP': "XRP"
}

def get_crypto_symbols():
  return CRYPTO_SYMBOL_NAMES.keys()

def utc_integer_to_utc_date(utc_integer): 
  utc_zone = tz.gettz('UTC')
  return str(datetime.fromtimestamp(utc_integer).astimezone(utc_zone).date())

# Request data from yahoo finance
def get_latest_data(crypto_symbol):
  url = f'https://yfapi.net/v8/finance/chart/{crypto_symbol}-USD?range=1d&region=US&interval=1d&lang=en'
  # API_KEY = os.getenv('YAHOO_FINANCE_API_KEY')
  API_KEY = "LLWzhpJcly7nb3bdV1wQl4EvR3GPwtI2ayFXqYVw"
  headers = {
    'accept':'application/json',
    'x-api-key': API_KEY
  }
  response = requests.get(url, headers=headers).json()
  print(API_KEY)
  return response

def update_dataset():
  print("method strt")
  crypto_symbol = 'BTC'
  response = get_latest_data(crypto_symbol)
  filename = response['chart']['result'][0]['meta']['symbol']
  utc_integer = response['chart']['result'][0]['timestamp'][0]
  priceData = response['chart']['result'][0]['indicators']['quote'][0]
  
  newRow = pd.DataFrame({
    'Date': utc_integer_to_utc_date(utc_integer),
    'Open': priceData['open'], 
    'High': priceData['high'], 
    'Low': priceData['low'],
    'Close': priceData['close'],
    'Volume': priceData['volume'],
  })

  df = pd.read_csv(f'/Users/justinhoe/Desktop/Projects/scheduledTask/dataset/{filename}.csv')
  newdf = df.append(newRow)
  newdf.to_csv(f'/Users/justinhoe/Desktop/Projects/scheduledTask/dataset/{filename}.csv', index=False)
  print("method end")

update_dataset()