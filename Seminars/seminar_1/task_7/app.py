# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через
# контекст.


from flask import Flask, render_template

app = Flask(__name__)  # создание объекта приложения


@app.route('/')  # переход на главную страницу
def index():
    return render_template('base.html')


@app.route('/about/')  # переход на about
def about():
    return render_template('about.html')


@app.route('/contact/')  # переход на contact
def contact():
    return render_template('contact.html')


@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):
    return str(num + num2)


@app.route('/str-len/<str_inp>')
def str_len(str_inp):
    return str(len(str_inp))


@app.route('/students/')
def students():
    _students = [
        {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "average": 85
        },
        {
            "name": "Jane",
            "surname": "Smith",
            "age": 22,
            "average": 92
        }
    ]
    context = {'students': _students}
    return render_template('students.html', **context)


@app.route('/news/')
def news():
    _news = [
        {
            "title": "John",
            "descr": "Doe",
            "date": 201
        },
        {
            "title": "John2",
            "descr": "Doe",
            "date": 202
        },
        {
            "title": "John3",
            "descr": "Doe",
            "date": 203
        }
    ]
    context = {"news": _news}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()
