from flask import Flask, jsonify
from flask_cors import CORS

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

GAMES = [
    {
        'title':'2k21',
        'genre':'sports',
        'played': True,
    },
    {
        ...
    }
]

@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'games': GAMES,
        'status': 'success'
    })

if __name__ == "__main__":
    app.run(debug=True)