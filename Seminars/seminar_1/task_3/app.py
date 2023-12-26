# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.


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


@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):
    return str(num + num2)


if __name__ == '__main__':
    app.run()
