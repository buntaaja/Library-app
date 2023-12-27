from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

# 'pipenv shell' to run virtual enviroment
# in windows shell in cd frontend: 1.npm install -g @vue/cli
# 2. npm install --save--dev eslint eslint-plugin-vue
# vue create frontend
# V mapi frontent/frontend napiši npm i axios
# V isti mapi: npm install bootstrap@4.6.0 --save

# Update the app constantly
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
#CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})

@app.route('/', methods=['GET'])
def greetings():
    return("Hello, World!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark!")

BOOKS = [
    {
        'id':uuid.uuid4().hex,
        'title':'The 7 Husbands of Evelyn Hugo',
        'genre':'fiction novel',
        'read': False
    },
    {
        'id':uuid.uuid4().hex,
        'title':'The Way of Kings',
        'genre': 'fantasy novel',
        'read': True
    },
    {
        'id':uuid.uuid4().hex,
        'title':'Words of Radiance',
        'genre': 'fantasy novel',
        'read': False
    }
]

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'read': post_data.get('read')})
        response_object['message'] = "Book Added!"
        return jsonify(response_object), 201
    else:
        response_object['books'] = BOOKS
        return jsonify(response_object)


# The put and delete route handlers
@app.route('/books/<book_id>', methods = ['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
           'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'read': post_data.get('read')
        })
        response.object['message'] = "Book updated!"
    if request.method == "DELETE":
        remove_book(book_id)
        response_object['message'] = "Book Removed!"
    return jsonify(response_object)

# Removing the book
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)