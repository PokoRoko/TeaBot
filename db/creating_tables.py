from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Определяем тип и название БД (echo параметр логирования)
engine = create_engine('sqlite:///tea.db', echo=True)
# Определяем базовый класс
Base = declarative_base()


# Создаем и определяем поля для таблицы Пользователи
class User(Base):
    """
    Класс для создания таблицы Продуктовой линейки с помощью SQlalchemy
    Описание:
    id - Уникальный id пользователя
    telegram_id - id из Телеграма если есть
    name - Имя пользователя
    login - Логин для входа
    password  - Пароль для входа
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    name = Column(String)
    login = Column(String)
    password = Column(String)

    def __init__(self, telegram_id, name, login, password,):
        self.telegram_id = telegram_id
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.telegram_id, self.name, self.login, self.password,)


# Создаем и определяем поля для таблицы Продукты
class Product(Base):
    """
    Класс для создания таблицы Продуктовой линейки с помощью SQlalchemy
    Описание:
    id - id в таблице
    article - Уникальный артикул продукта
    category - Категория к которой относится товар
    name - Наименование
    shipper - Продавец
    price_shipper - Цена от поставщика
    price - Розничная цена
    unit - Единица в которой измеряется товар
    min_buy - Минимально количество для покупки данноготовара
    description - Описани
    link_shipper - Ссылка на товар, на странице поставщика
    link_photo  - Ссылка на фото товара
    photo - Фото
    """

    __tablename__ = 'products'
    id = Column(Integer)
    article = Column(String, primary_key=True)
    category = Column(String)
    name = Column(String)
    shipper = Column(String)
    price_shipper = Column(Integer)
    price = Column(Integer)
    unit = Column(String)
    min_buy = Column(Integer)
    description = Column(Text)
    link_shipper = Column(String)
    link_photo = Column(String)
    photo = Column(Boolean)

    def __init__(self, article, category, name, shipper, price_shipper, price, unit,
                 min_buy, description, link_shipper, link_photo, photo,):
        self.article = article
        self.category = category
        self.name = name
        self.shipper = shipper
        self.price_shipper = price_shipper
        self.price = price
        self.unit = unit
        self.min_buy = min_buy
        self.description = description
        self.link_shipper = link_shipper
        self.link_photo = link_photo
        self.photo = photo

    def __repr__(self):
        return (
            self.id, self.article, self.category, self.name, self.shipper,
            self.price_shipper, self.price, self.unit, self.min_buy,
            self.description, self.link_shipper, self.link_photo, self.photo,
            )


# Создаем и определяем поля для таблицы Заказы
class Order(Base):
    """
    Класс для создания таблицы Заказов с помощью SQlalchemy
    Описание:
    id - Уникальный id пользователя
    telegram_id - id из Телеграма если есть
    name - Имя пользователя
    login - Логин для входа
    password  - Пароль для входа
    """
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    date_create = Column(DateTime)
    status = Column(String)
    list_products = Column(String)
    price_shipper = Column(Integer)
    price = Column(Integer)
    address_delivery = Column(Text)
    type_delivery = Column(String)
    date_delivery = Column(DateTime)

    def __init__(self, id_user, date_create, status, list_products, price_shipper,
                 price, address_delivery, type_delivery, date_delivery,
                 ):

        self.id_user = id_user
        self.date_create = date_create
        self.status = status
        self.list_products = list_products
        self.price_shipper = price_shipper
        self.price = price
        self.address_delivery = address_delivery
        self.type_delivery = type_delivery
        self.date_delivery = date_delivery

    def __repr__(self):
        return (
            self.id_user, self.date_create, self.status, self.list_products, self.price_shipper,
            self.price, self.address_delivery, self.type_delivery, self.date_delivery,
        )

Base.metadata.create_all(engine)  # Создает таблицы если их нет

# # Создание сессии
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

