from crypto_price import final_top5, final_top10
from search_news import final_news
from scan_eth import get_info

def greet():
    '''Функция приветсвия'''
    text = "Привет! Добро пожаловать в crypto-парсер! \nЗдесь ты можешь узнать стоимость, рыночную капитализацию и изменение цены за последние 24 часа \nТакже ты можешь узнавать последние новости, связанные с криптовалютой! \nВсе это будет классно отображаться в exel файле \nА еще можешь узнать баланс любого кошелька по его адресу."
    print(text)

def choice():
    '''Предлогает функционал'''
    text='Выбери, то что хочешь узнать: \n"Топ-5 крипто" \n"Топ-10 крипто" \n"Новости" \n"Баланс"'
    print(text)
    user=input()
    return user

def main_greet(user):
    '''Главная функция'''
    if user == "Топ-5 крипто":
        print("Создалась таблица цен ! \nP.S. если таблица была - она обновилась.")
        return final_top5()
    if user == "Топ-10 крипто":
        print("Создалась таблица цен! \nP.S. если таблица была - она обновилась.")
        return final_top10()
    if user == "Новости":
        print("Создалась таблица новостей! \nP.S. если таблица была - она обновилась.")
        return final_news()
    if user == "Баланс":
        print("Смотри результат в терминале!")
        return get_info()




if __name__ == '__main__':
    greet()
    main_greet(choice())
