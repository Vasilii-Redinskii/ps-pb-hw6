from app import app
from flask import render_template, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_product', methods=['POST', 'GET'])
def create_product():

    context = None

    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Добавить товар')
        # Получаем название товара - это значение поля input с атрибутом name="title"
        product_title = request.form['title']

        # Получаем цену товара - это значение поля input с атрибутом name="price"
        product_price = request.form['price']

        # Заполняем словарь контекста
        context = {
            'method': 'POST',
            'title': product_title,
            'price': product_price,
        }
    
    elif request.method == 'GET':

        # Пришел запрос с методом GET - пользователь просто открыл в браузере страницу по адресу http://127.0.0.1:5000/create_product
        # В этом случае просто передаем в контекст имя метода
        context = {
            'method': 'GET',
        }

    return render_template('create_product.html', **context)