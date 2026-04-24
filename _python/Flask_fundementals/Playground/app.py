from flask import Flask,render_template,redirect

app=Flask(__name__)

@app.route('/')
def home():
    return redirect('/play')

@app.route('/play')
def play():
    x=3
    color='blue'
    return render_template('index.html',x=x,color=color)

@app.route('/play/<int:x>')
def number_of_X(x):
    color='blue'
    return render_template('index.html',x=x,color=color)

@app.route('/play/<int:x>/<color>')
def number_and_color(x,color):
    return render_template('index.html',x=x,color=color)

@app.errorhandler(404)
def page_not_found(e):
    return 'error page not found'

if __name__== '__main__':
    app.run(debug=True)