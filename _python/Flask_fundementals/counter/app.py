from flask import Flask, session, render_template, redirect,request

app= Flask(__name__)
app.secret_key = "my_secret_key"

@app.route('/')
def home():
    if "counter" not in session:
        session["counter"] = 0
    session["counter"] += 1  
        
    return render_template('index.html',counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
