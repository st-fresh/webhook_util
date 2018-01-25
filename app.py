from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def homepage():
    print('REQUEST')
    print('Headers: {}'.format(str(request.headers)))
    print('Body: {}'.format(request.get_data()))
    print('Entire Request: {}'.format(str(request)))
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
