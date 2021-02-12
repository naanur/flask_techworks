from flask import Flask, render_template, redirect
from flask.helpers import url_for
from werkzeug.exceptions import HTTPException

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')




@app.errorhandler(Exception)
def handle_exception(e):
    # Отлов ошибок
    if isinstance(e, HTTPException):
        return redirect(url_for('index'))
    return render_template("index.html"), 404

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True )