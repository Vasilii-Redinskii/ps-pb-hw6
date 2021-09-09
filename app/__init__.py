from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Подключаем базу данных к приложению
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../onlineshop.sqlite"

# Отключаем вывод технических сообщений
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Создаем саму базу данных - объект db
db = SQLAlchemy(app)


from app import views