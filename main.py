from flask import Flask, render_template

app = Flask(__name__)  # создаем переменную арр , где создаем экземпляр класса


@app.route("/")  # создаем декоратор для присвоения url-адреса для функции
def games():
    return render_template("index.html")


@app.route("/second/")
def one_more():
    return render_template("second.html")


@app.route("/blog/")
def page_blog():
    pass


@app.route("/contacts/")
def page_contacts():
    pass


if __name__ == "__main__":  # проверка запуска скрипта на локальном сервере
    app.run()
