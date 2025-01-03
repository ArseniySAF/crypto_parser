'''Парсинг важных новостей связанных с криптой'''

import requests
from convert_to_exel import to_exel_news

API_KEY = '0704c192d7d447cf8aa2c1bcef3cf160'

def get_news():
    '''Прасинг новостей'''
    url = f'https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['articles']

def filter_news(data):
    '''Фильтр новостей по заголовку, описанию и контенту'''
    filtered_news = []
    for item in data:
        if item.get('title') == '[Removed]':
            continue
        if item.get('description') == None:
            continue
        filtered_item = {
            'title': item.get('title'),
            'description': item.get('description'),
            'content': item.get('content')
        }
        filtered_news.append(filtered_item)
    return filtered_news

def final_news():
    '''Для main.py вызов функции'''
    return to_exel_news(filter_news(get_news()))

