'''Для парсинга цен'''

import requests

from convert_to_exel import to_exel_prices

def get_crypto_prices_top5():
    '''Берем API с сайта CoinGecko(крипто сканер) - топ 5 по капитализации'''
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        "vs_currency": "usd", 
        "order": "market_cap_desc", 
        "per_page": 6,
        "page": 1 
    }
    response = requests.get(url, params=params)
    return response.json()

def get_crypto_prices_top10():
    '''Берем API с сайта CoinGecko(крипто сканер) - топ 10 по капитализации'''
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 11,
        "page": 1  
    }
    response = requests.get(url, params=params)
    return response.json()

def filter_data(data):
    '''Фильтруем самые важные столбцы с названием, ценой и изменением за 24 часа'''
    filtered_data = []
    for item in data:
        filtered_item = {
            'id': item.get('id'),
            'current_price': item.get('current_price'),
            'market_cap': item.get('market_cap'),
            'price_change_percentage': item.get('price_change_percentage_24h')  
        }
        filtered_data.append(filtered_item)
    return filtered_data


def final_top5():
    '''Для main.py вызов парсера Топ-5 крипто'''
    crypto_top5 = filter_data(get_crypto_prices_top5())
    to_exel_prices(crypto_top5)

def final_top10():
    '''Для main.py вызов парсера Топ-10 крипто'''
    crypto_top10 = filter_data(get_crypto_prices_top10())
    to_exel_prices(crypto_top10)

