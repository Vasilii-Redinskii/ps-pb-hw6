from app import app, db
from app.models import User, Product
from flask import render_template, request


@app.route('/')
def index():
    
    # Получаем все записи из таблицы Product
    product_list = Product.query.all()

    # Получаем все записи из таблицы User
    user_list = User.query.all()

    # Полученные наборы передаем в контекст
    context = {
        'product_list': product_list,
        'user_list': user_list,
    }

    return render_template('index.html', **context)


@app.route('/create_product', methods=['POST', 'GET'])
def create_product():

    context = None

    if request.method == 'POST':
        
        # Пришел запрос с методом POST (пользователь нажал на кнопку 'Добавить товар')
        # Получаем название товара - это значение поля input с атрибутом name="title"
        product_title = request.form['title']

        # Получаем цену товара - это значение поля input с атрибутом name="price"
        product_price = request.form['price']

        # Добавляем товар в базу данных
        db.session.add(Product(title=product_title, price=product_price))

        # сохраняем изменения в базе
        db.session.commit()

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

@app.route('/create_user', methods=['POST', 'GET'])
def create_user():

    context = None

    if request.method == 'POST':
        
        name = request.form['name']
        username = request.form['username']

        db.session.add(User(name=name, username=username))
        db.session.commit()

        context = {
            'method': 'POST',
            'name': name,
            'username': username,
        }
    
    elif request.method == 'GET':

        context = {
            'method': 'GET',
        }

    return render_template('create_user.html', **context)
    