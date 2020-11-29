import requests
from bs4 import BeautifulSoup


def parse_name_and_link_category():
    url = 'https://besttea.ru/catalog/'  # Страница с основным каталогом, из которого мы будем брать надкатегории
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
    global_categories = soup.find_all(class_="ab-lc-group")  # Получаем все ссылки и название абсолютно всех категорий
    res = {}
    for categories in global_categories:
        # Получаем ссылки и названия основных категорий
        soup_cat = categories.find(class_="cat-title")
        glob_cat_name = soup_cat.get_text()
        glob_cat_link = soup_cat.a['href']
        res[glob_cat_name] = [glob_cat_link]

        subcategories = categories.find(class_="items-level-2")  # Получаем ссылки и название всех подкатегорий
        for subcategory in subcategories:
            # Получаем ссылки и название подкатегорий
            soup_sub = subcategory.a
            sub_cat_name = soup_sub.get_text()
            sub_cat_link = soup_sub['href']

            ss = subcategory.find(class_="items-level-3")  # Получаем ссылки и название доп категорий
            dop = []  # Докостыливаю добавление доп категорий
            if ss is not None:
                for i in ss:
                    dop =[i.get_text(), i.a['href']]
            else:
                dop = []
            res[glob_cat_name].append([sub_cat_name, sub_cat_link, dop])
    return res

# # Подготавливаю парсер ссылык на страницу товара
# url = 'https://besttea.ru/premialnyy-chay/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# product = soup.find_all(class_="ut2-gl__name")
# print(product)