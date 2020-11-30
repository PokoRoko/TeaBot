import requests
from bs4 import BeautifulSoup


def parse_names_and_link_categories():
    """
    Функция собирает ссылки и название категорий и подкатегорий в основном каталоге магазина.
    ToDo В дальнейшем из него будут браться хлебные крошки.
    :return:
    Упаковывает в словарь с ключом в виде названии категории
    и вложенными списками с названием подкатекории и ссылкой на нее.
    """
    url = 'https://besttea.ru/catalog/'  # Страница с основным каталогом, из которого мы будем брать надкатегории
    r = requests.get(url)
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


# Функция поиска ссылки для перехода по страницам категории
def search_next_page_link(url):
    """
    Функция для поиска кнопки перехода на следующую страницу
    :param url: Принимает ссылку на страницу с товаром
    :return: Ссылка на следующую страницу с товаром
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    next_page_button = soup.find(class_= "ty-pagination__item ty-pagination__btn ty-pagination__next cm-history cm-ajax ty-pagination__right-arrow")
    try:
        link_next_page = next_page_button['href']
        return link_next_page
    except:
        return None


# Подготавливаю парсер ссылык на страницу товара
def search_products_link(url):
    """
    Функция собирает все ссылки на товар со страницы и так же производит поиск на следующих страницах
    :param url: Ссылка на страницу с товаром в категории
    :return: Список с ссылками на товар во всей категории
    """
    res = []
    if search_next_page_link(url) != None:
        np = search_products_link(search_next_page_link(url))
        res.extend(np)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    products = soup.find_all(class_="ut2-gl__name")  # Получаем ссылки на все напродукты со страницы категории
    for link_product in products:
        link = link_product.a['href']
        res.append(link)
    return res

def parse_product(url):
    """
    ToDo Функция собирает даные о товаре и передает в БД
    :param url: Ссылка на продукт
    :return:
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    article = (soup.find(class_="ty-control-group__item")).get_text()
    parent_category = (soup(class_="ty-breadcrumbs__a")[-1]).get_text()
    name = (soup.find(class_="ut2-pb__title")).get_text()
    # shipper
    price_shipper = (soup.find(class_="ty-price-num")).get_text()
    # price
    # unit
    # min_buy
    # description
    # link_shipper
    link_photo = (soup.find(class_="cm-image-previewer cm-previewer ty-previewer")).img['data-src']
    # photo


def start_parsing():
    """
    Впринципе агрегирует в себе все функции парсинга страниц.
    1) Поиск категорий
    2) Поиск ссылок на товар по категориям
    3) Парсинг страницы с товаром
    4) Запись в базу данных
    ToDo 5) Генерирует хлебные крошки
    :return:
    """
    categories = parse_names_and_link_categories()
    for link_categories in categories.values():
        for k in link_categories:
            print('parse:', k[0])  # Имя родительского каталога
            link_products = search_products_link(k[1])  # Ищем ссылки на товар в категории
            for link in link_products:
                parse_product(link)

