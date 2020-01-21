from csv import reader
from random import choice
import json

# ------------Заполнить!------------
books_path = '/home/alex/Documents/otus_dz3/books.csv'
users_path = '/home/alex/Documents/otus_dz3/users.json'
result_path = '/home/alex/Documents/otus_dz3/result.json'
# ----------------------------------

books = []
with open(books_path) as books_file:
    table = reader(books_file)
    for line in table:
        books.append({'title': line[0], 'author': line[1], 'height': line[3]})

users = []
with open(users_path) as users_file:
    users_json = json.load(users_file)
    for user in users_json:
        users.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'books': [choice(books), choice(books)],
            }
        )

with open(result_path, 'wt') as result_file:
    json.dump(users, result_file)
