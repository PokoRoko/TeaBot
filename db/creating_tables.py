from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Определяем тип и название БД (echo параметр логирования)
engine = create_engine('sqlite:///tea.db', echo=True)
# Определяем базовый класс
Base = declarative_base()

# ToDo Стоит пересмотреть варианты отображения в __repr__,__str__,__dict__
# Создаем и определяем поля для таблицы Пользователи
class User(Base):
    """
    Класс для создания таблицы Продуктовой линейки с помощью SQlalchemy
    Описание:
    id - Уникальный id пользователя
    telegram_id - id из Телеграма если есть
    name - Имя пользователя
    first_name - Полное имя
    login - Логин для входа
    password  - Пароль для входа
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    name = Column(String)
    first_name = Column(String)
    login = Column(String)
    password = Column(String)

    def __init__(self, telegram_id, name, first_name, login, password,):
        self.telegram_id = telegram_id
        self.name = name
        self.first_name = first_name
        self.login = login
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s', '%s')>" % \
               (self.telegram_id, self.name, self.first_name, self.login, self.password,)


# Создаем и определяем поля для таблицы Продукты
class Product(Base):
    """
    Класс для создания таблицы Продуктовой линейки с помощью SQlalchemy
    Описание:
    id - id в таблице
    article - Уникальный артикул продукта
    parent_category - Категория к которой относится товар
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
    parent_category = Column(String)
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

    def __init__(self, article, parent_category, name, shipper, price_shipper, price, unit,
                 min_buy, description, link_shipper, link_photo, photo,):
        self.article = article
        self.parent_category = parent_category
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
            self.id, self.article, self.parent_category, self.name, self.shipper,
            self.price_shipper, self.price, self.unit, self.min_buy,
            self.description, self.link_shipper, self.link_photo, self.photo,
            )

    def __str__(self):
        return 'fuck'


# Создаем и определяем поля для таблицы Заказы
class Order(Base):
    """
    Класс для создания таблицы Заказов с помощью SQlalchemy
    Описание:
    id - Уникальный id заказа
    id_user - id пользователя сделавшего заказ
    date_create - Дата создания заказа
    status - Статус заказа
    dict_products - Словарь-список артикулов с количеством продукта
    price_shipper - Цена поставщика на момент заказа
    price - Цена на момент заказа
    address_deliver - Адресс доставки
    type_delivery -  Тип доставки
    date_delivery - Дата доставки
    """
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    date_create = Column(DateTime)
    status = Column(String)
    dict_products = Column(String)
    price_shipper = Column(Integer)
    price = Column(Integer)
    address_delivery = Column(Text)
    type_delivery = Column(String)
    date_delivery = Column(DateTime)

    def __init__(self, id_user, date_create, status, dict_products, price_shipper,
                 price, address_delivery, type_delivery, date_delivery,
                 ):

        self.id_user = id_user
        self.date_create = date_create
        self.status = status
        self.dict_products = dict_products
        self.price_shipper = price_shipper
        self.price = price
        self.address_delivery = address_delivery
        self.type_delivery = type_delivery
        self.date_delivery = date_delivery

    def __repr__(self):
        return (
            self.id_user, self.date_create, self.status, self.dict_products, self.price_shipper,
            self.price, self.address_delivery, self.type_delivery, self.date_delivery,
        )


Base.metadata.create_all(engine)  # Создает таблицы если их нет

