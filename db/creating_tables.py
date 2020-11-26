from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///tea.db', echo=False)
Base = declarative_base()


# Создаем и определяем поля таблицы
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

    def __init__(self, telegram_id, name, login, password):
        self.telegram_id = telegram_id
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.telegram_id, self.name, self.login, self.password)


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
    """

    __tablename__ = 'products'
    id = Column(Integer)
    article = Column(String, primary_key=True)
    category = Column(String)
    name = Column(String)
    shipper = Column(String)
    price_shipper = Column(String)
    price = Column(String)
    unit = Column(String)
    min_buy = Column(Integer)
    description = Column(String)
    link_shipper = Column(String)
    link_photo = Column(String)

    def __init__(self, article, category, name, shipper, price_shipper, price, unit,
                 min_buy, description, link_shipper, link_photo):
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

    def __repr__(self):
        return (
            self.id, self.article, self.category, self.name, self.shipper,
            self.price_shipper, self.price, self.unit, self.min_buy,
            self.description, self.link_shipper, self.link_photo,
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

