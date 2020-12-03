import csv
from config import name_new_price
from db.creating_tables import Product


# Чтобы подготовить файл, его надо сохранить в CSV и подписать колонку единицы измерений
def scan_opt_price_csv():
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
                print(dict_prod)

            prod = Product(**dict_prod)
            prod.add_price_product_db()



