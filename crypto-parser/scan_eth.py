'''Слежка за покупкой кошелька на блокчейне ETH'''
import requests


API_KEY = 'EEJYZEH89ZN2JT4AIIKG97QHVGVCPZFQIX'

def get_info():
    '''Отслеживание баланса кошелька в ETH'''
    wallet = input("Введите адрес кошелька: ")
    address = wallet.strip()
    params = {
    'module': 'account',
    'action': 'balance',
    'address': address,
    'tag': 'latest', 
    'apikey': API_KEY
    }
    url = "https://api.etherscan.io/api"
    response = requests.get(url, params=params)
    data = response.json()
    balance = int(data['result'])
    return print(f'Баланс кошелька: {balance / 10**18} ETH')
