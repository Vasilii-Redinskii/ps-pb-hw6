from app import db
from app.models import User


# создаем экземпляр класса User
new_user = User(name="Иван")

# добавляем изменения в базу данных (при этом база не сохраняется)
db.session.add(User(name="Иван"))
db.session.add(User(name="Петр"))
db.session.add(User(name="Ольга"))
db.session.add(User(name="Игнат"))

# сохраняем изменения в базе
db.session.commit()