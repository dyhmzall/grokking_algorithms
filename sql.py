# скрипт для генерации данных
# именно для схемы базы данных
# https://d2xzmw6cctk25h.cloudfront.net/asset/3142199/attachment/039b5a727283aa5d9b2c516c87a75f8d.sql

# для генерации случайных слов используем проект
# https://pypi.org/project/lorem-text/
from lorem_text import lorem
import hashlib
import random

words = 1
test = lorem.words(words)

print(test)

data = {
    'users': {
        'count': 2,
        'items': [],
        'sql': ''
    }
}


class Users:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        hash_object = hashlib.md5(first_name.encode())
        self.password = hash_object.hexdigest()
        self.phone = phone


# таблица users
for i in range(data['users']['count']):
    user = Users(
        lorem.words(1),
        lorem.words(1),
        lorem.words(1) + '@gmail.com',
        random.randint(79000000000, 79999999999)
    )
    data['users']['items'].append(user)
    sql = f"INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `password_hash`, `phone`) VALUES (NULL, '{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}', '{user.phone}');\n"
    data['users']['sql'] += sql

print(data['users']['sql'])
