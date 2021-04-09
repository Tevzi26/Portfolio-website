from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/certificates')
def certificates():
    return render_template('certificates.html')


@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.13')
