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
                    dop.append([i.get_text(), i.a['href']])
            res[glob_cat_name].append([sub_cat_name, sub_cat_link, dop])
    return res


# Функция поиска ссылки для перехода по страницам категории
def search_next_page_link(url):
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
