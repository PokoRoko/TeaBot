import csv
from config import name_new_price
from db.creating_tables import Product


# Чтобы подготовить файл, его надо сохранить в CSV и подписать колонку единицы измерений
def scan_opt_price_csv():
    """
    Функция откравает файл csv с указанным именем, достает и добавляет в БД
    оптовые цены и единицу измерения по артикулу
    ToDo определить except и решить проблему с запятой в цене
    :return:
    """
    with open(name_new_price, 'r', encoding="utf-8-sig") as f_obj:
        price = csv.DictReader(f_obj, delimiter=';')
        for line in price:
            try:
                dict_prod = {'article': line['артикул'],
                             'opt_price': int(line['Цена']),
                             'unit': line['ед.изм']
                             }
            except:
                print(f"Ошибка записи: {line['артикул']}")

            prod = Product(**dict_prod)
            prod.add_price_product_db()
