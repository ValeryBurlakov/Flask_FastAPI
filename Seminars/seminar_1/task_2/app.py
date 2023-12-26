# Дорабатываем задачу 1.
# 📌 Добавьте две дополнительные страницы в ваше веб-
# приложение:
# ○ страницу "about"
# ○ страницу "contact".
from flask import Flask, render_template

app = Flask(__name__)  # создание объекта приложения


@app.route('/')  # переход на главную страницу
def hello_world():
    return 'Hello World!'


@app.route('/about/')  # переход на about
def about():
    return render_template('about.html')


@app.route('/contact/')  # переход на contact
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
