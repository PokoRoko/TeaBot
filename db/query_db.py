# ToDo Написать функции запросов к БД на основе примеров
from creating_tables import Product, engine
from sqlalchemy.orm import sessionmaker

article = 'BT-174'
parent_category = 'Пуэр преcсованный'
name = 'Пуэрная пирамида Шен, 1 кг'
price_shipper = 5640.00
link_shipper = 'https://besttea.ru/puernaya-piramida-1-kg/'
link_photo = 'https://besttea.ru/images/thumbnails/450/450/detailed/21/bt-174_01.jpg.jpg'



# Создание сессии
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker()
#
# Session.configure(bind=engine)  # Как только у вас появится engine
#
# session = Session()
#

#  Добавление новых объектов
# vasiaUser = User(password="vasia", name="Vasiliy Pypkin", login="vasia2000")
# session.add(vasiaUser)
#
# session.add_all([User("kolia", "Cool Kolian[S.A.]", "kolia$$$"), User("zina", "Zina Korzina", "zk18")])   #добавить сразу пачку записей
# vasiaUser.password = "95959595"   # старый пароль был таки ненадежен, смена пароля
#
# session.commit()
#

# Запросы
# Запрос, который загружает экземпляры User. В итеративном цикле возвращается список объектов User:
# for instance in session.query(User).order_by(User.id):
#     print(instance.name, instance.login, instance.password)

"""Запрос также поддерживает в качестве аргументов дескрипторы, созданные с помощью ORM.
Каждый раз, когда запрашиваются разнообразные объекты классов или многоколоночные объекты в качестве
аргументов функции query(), результаты возвращаются в виде кортежей:"""
# for name, login, password in session.query(User.name, User.login, User.password):
#     print(name, login, password)
#
# # С фильтром
# for name in session.query(User.name).filter(User.login == 'Vasiliy Pypkin'):
#     print(name)

# Создание сессии
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker()
#
# Session.configure(bind=engine)  # Как только у вас появится engine
#
# session = Session()
#

#  Добавление новых объектов
# vasiaUser = User(password="vasia", name="Vasiliy Pypkin", login="vasia2000")
# session.add(vasiaUser)
#
# session.add_all([User("kolia", "Cool Kolian[S.A.]", "kolia$$$"), User("zina", "Zina Korzina", "zk18")])   #добавить сразу пачку записей
# vasiaUser.password = "95959595"   # старый пароль был таки ненадежен, смена пароля
#
# session.commit()

#  Добавление новых объектов
Session = sessionmaker()
Session.configure(bind=engine)  # Как только у вас появится engine
session = Session()
# scrap_product = Product(
#     article=article,
#     parent_category=parent_category,
#     name=name,
#     shipper='',
#     price_shipper=price_shipper,
#     price=0,
#     unit='',
#     min_buy=0,
#     description='',
#     link_shipper=link_shipper,
#     link_photo=link_photo,
#     photo=1
# )


session.add(scrap_product)
session.commit()
print(scrap_product)

