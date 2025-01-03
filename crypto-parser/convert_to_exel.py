'''Файл для конвертации data в xlsx файл'''
import pandas as pd

def to_exel_prices(data):
    '''Создаем xlsx файл с data_price'''
    df = pd.DataFrame(data)
    df.to_excel('crypto_price.xlsx')

def to_exel_news(data):
    '''Создаем xlsx файл с data_news'''
    df = pd.DataFrame(data)
    df.to_excel('crypto_news.xlsx')

