from db.creating_tables import Product


def test_add_scrap_product_db():
    article = 'Test_article'
    parent_category = 'Тестовая категория'
    name = 'Тестовый товар'
    price_shipper = 666.00
    link_shipper = 'https://besttea.ru/puernaya-piramida-1-kg/'
    link_photo = 'https://besttea.ru/images/thumbnails/450/450/detailed/21/bt-174_01.jpg.jpg'

    scrap_product = Product(
        article=article,
        parent_category=parent_category,
        name=name,
        price_shipper=price_shipper,
        link_shipper=link_shipper,
        link_photo=link_photo,
    )
    scrap_product.add_scrap_product_db()


test_add_scrap_product_db()
