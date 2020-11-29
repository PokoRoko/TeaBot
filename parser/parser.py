import requests
from bs4 import BeautifulSoup

url = 'https://besttea.ru/catalog/'  # Страница с основным каталогом, из которого мы будем брать надкатегории
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
global_categories = soup.find_all(class_="ab-lc-group")  # Получаем все ссылки и название абсолютно всех категорий

for categories in global_categories:
    # Получаем ссылки и названия основных категорий
    soup_cat = categories.find(class_="cat-title")
    glob_cat_name = soup_cat.get_text()
    glob_cat_link = soup_cat.a['href']

    subcategories = categories.find(class_="items-level-2")  # Получаем ссылки и название всех подкатегорий
    for subcategory in subcategories:
        # Получаем ссылки и название подкатегорий
        soup_sub = subcategory.a
        sub_cat_name = soup_sub.get_text()
        sub_cat_link = soup_sub['href']

        print(sub_cat_name)
        print(sub_cat_link)
