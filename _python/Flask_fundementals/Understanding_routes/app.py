from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello World!'

@app.route('/Champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def say(name):
    return f'Hello, {name}!'

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return (word + " ") * num

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry no response try again!'
if __name__ == '__main__':
    app.run(debug=True)