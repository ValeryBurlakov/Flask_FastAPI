# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)  # создание объекта приложения


@app.route('/')  # переход на главную страницу
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
