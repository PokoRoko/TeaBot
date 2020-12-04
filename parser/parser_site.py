import requests
from config import time_out
from bs4 import BeautifulSoup
from db.creating_tables import Product


# Подмена хэдэра для парсинга
def headers():
    """
    :return: Заголовок запроса для имитации пользователя
    """
    head = requests.utils.default_headers()
    head.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})
    return head


# Парсер имен и ссылок на категории
def parse_names_and_link_categories():
    """
    Функция собирает ссылки и название категорий и подкатегорий в основном каталоге магазина.
    ToDo В дальнейшем из него будут браться хлебные крошки.
    :return:
    Упаковывает в словарь с ключом в виде названии категории
    и вложенными списками с названием подкатекории и ссылкой на нее.
    """
    url = 'https://besttea.ru/catalog/'  # Страница с основным каталогом, из которого мы будем брать надкатегории
    r = requests.get(url, headers(), timeout=time_out)
    soup = BeautifulSoup(r.text, 'html.parser')  # Отправляем полученную страницу в библиотеку для парсинга
    global_categories = soup.find_all(class_="ab-lc-group")  # Получаем все ссылки и название абсолютно всех категорий
    res = {}
    for categories in global_categories:
        # Получаем ссылки и названия основных категорий
        soup_cat = categories.find(class_="cat-title")
        glob_cat_name = soup_cat.get_text()
        res[glob_cat_name] = []
        # glob_cat_link = soup_cat.a['href']
        # res[glob_cat_name] = [glob_cat_link]

        subcategories = categories.find(class_="items-level-2")  # Получаем ссылки и название всех подкатегорий
        for subcategory in subcategories:
            # Получаем ссылки и название подкатегорий
            soup_sub = subcategory.a
            sub_cat_name = soup_sub.get_text()
            sub_cat_link = soup_sub['href']
            # res[glob_cat_name].append([sub_cat_name, sub_cat_link])
            ss = subcategory.find(class_="items-level-3")  # Получаем ссылки и название доп категорий
            dop = []  # Докостыливаю добавление доп категорий
            if ss is not None:
                for i in ss:
                    dop.append([i.get_text(), i.a['href']])
            res[glob_cat_name].append([sub_cat_name, sub_cat_link, dop])  # !Отключать другой res!
    return res


# Поиск ссылки для перехода по страницам категории
def search_next_page_link(url):
    """
    Функция для поиска кнопки перехода на следующую страницу
    :param url: Принимает ссылку на страницу с товаром
    :return: Ссылка на следующую страницу с товаром
    """

    r = requests.get(url, headers(), timeout=time_out)
    soup = BeautifulSoup(r.text, 'html.parser')
    next_page_button = soup.find(class_="ty-pagination__item ty-pagination__btn ty-pagination__next cm-history "
                                        "cm-ajax ty-pagination__right-arrow")
    try:
        link_next_page = next_page_button['href']
        return link_next_page
    except:
        return None


# Поиск ссылык на страницу товара
def search_products_link(url):
    """
    Функция собирает все ссылки на товар со страницы и так же производит поиск на следующих страницах.
    :param url: Ссылка на страницу с товаром в категории
    :return: Список с ссылками на товар во всей категории
    """
    res = []
    if search_next_page_link(url) is not None:
        np = search_products_link(search_next_page_link(url))
        res.extend(np)
    r = requests.get(url, headers(), timeout=time_out)
    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.find_all(class_="ut2-gl__name")  # Получаем ссылки на все напродукты со страницы категории
    for link_product in products:
        link = link_product.a['href']
        res.append(link)
    return res


# Сбор информации о продукте со страницы
def scrap_product(url):
    """
    Функция собирает даные о товаре сохраняет в словарь с параметрами
    :param url: Ссылка на продукт
    :return:
    """
    try:
        r = requests.get(url, headers=headers(), timeout=time_out)
    except:
        r = requests.get(url, headers=headers())
        print("!!!Задержка по TimeOut!!!")
    soup = BeautifulSoup(r.text, 'html.parser')
    res = {'article': (soup.find(class_="ty-control-group__item")).get_text(),
           'parent_category': (soup(class_="ty-breadcrumbs__a")[-1]).get_text(),
           'name': (soup.find(class_="ut2-pb__title")).get_text(),
           'price_shipper': (soup.find(class_="ty-price-num")).get_text(),
           'link_shipper': url,
           }
    try:
        res['link_photo'] = (soup.find(class_="cm-image-previewer cm-previewer ty-previewer")).img['data-src']
    except:
        print(f"Ссылка на фото ({res['name']}) не найдено.")
    return res


# Старт процесса сбора данных с сохранением в БД
def start_parsing():
    """
    Впринципе агрегирует в себе все функции парсинга страниц.
    1) Поиск категорий
    2) Поиск ссылок на товар по категориям
    3) Парсинг страницы с товаром
    4) Запись в базу данных

    :return:
    """
    categories = parse_names_and_link_categories()
    for link_categories in categories.values():
        for k in link_categories:
            print('parse:', k[0])  # Имя родительского каталога
            link_products = search_products_link(k[1])  # Ищем ссылки на товар в категории
            for link in link_products:
                dict_product = scrap_product(link)
                prod = Product(**dict_product)
                prod.add_scrap_product_db()


# Проверка моего ip
def check_ip():
    """
    Проверка ip
    :return: Возвращает мой ip
    """
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)


# Генерирует словарь с хлебными крошками
def generate_bread_crumbs():
    """
    Парсит и генерирует словарь хлебных крошек(по плану перед каждым запуском программы)
    Костыль, но всегда можно переделать)))
    :return: Словарь с именем категории в ключе и родительской директорией в значении
    """
    dict_category = parse_names_and_link_categories()
    bread_crumbs = {}
    for item in dict_category.keys():
        bread_crumbs[item] = "base"
        for subcategory in dict_category[item]:
            bread_crumbs[subcategory[0]] = item
            if subcategory[2]:
                for subsubcategory in subcategory[2]:
                    bread_crumbs[subcategory[0]] = subsubcategory[0]
    return bread_crumbs
