from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/zprava')
def zprava():
    return render_template('zprava.html')

if __name__ == '__main__':
    app.run(debug=True, port=8090)