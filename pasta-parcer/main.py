import requests
from bs4 import BeautifulSoup

import json

# Ссылка на категорию макарон в Metro (пример)
url = "https://zakaz.ua/uk/kyiv/pasta-zakaz/"

# Заголовок, чтобы сайт думал, что мы - обычный браузер
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Подключаюсь к сайту...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем первый товар на странице (класс может меняться, это база)
    product = soup.find('div', {'class': 'css-114scyh'})
    
    #print(product)
    if product:
        title = product.find('p', {'title': 'Макаронні вироби Pasta Reggia Фузіллі №48 500г'})
        p_tag = title['title']
        price = product.find('span', {'class': 'PricesRange__start'}).text
        
        print(f"--- УСПЕХ! ---")
        print(f"Товар: {p_tag}")
        print(f"Цена: {price} грн")
    else:
        print("Не нашел карточку товара. Похоже, сайт обновил дизайн.")
else:
    print(f"Ошибка доступа: {response.status_code}")

products = soup.find_all('div', class_='CatalogProductCard')

for product in products:
    # 2. Ищем тот самый "золотой" скрипт внутри карточки
    script_tag = product.find('script', {'data-testid': 'ld-json-script'})
    
    if script_tag:
        # 3. Превращаем текст скрипта в обычный словарь Python
        data = json.loads(script_tag.string)
        
        name = data.get('name')
        # Цена в JSON обычно лежит в списке offers
        price = data.get('offers', [{}])[0].get('price')
        currency = data.get('offers', [{}])[0].get('priceCurrency')
        
        print(f"Товар: {name}")
        print(f"Цена: {price} {currency}")
        print("-" * 30)