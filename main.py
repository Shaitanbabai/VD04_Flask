from flask import Flask, render_template


app = Flask(__name__)  # Создаем переменную арр , где создаем экземпляр класса


@app.route("/")  # создаем декоратор для присвоения url-адреса для функции
def games():
    context = {
        "link": "Подробнее"
    }
    return render_template("index.html", **context)

@app.route("/blog/")
def one_more():
    return render_template("blog.html")


@app.route("/contacts/")
def page_contacts():
    return render_template("contacts.html")


if __name__ == "__main__":  # проверка запуска скрипта на локальном сервере
    app.run()
