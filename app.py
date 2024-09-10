from flask import Flask

app = Flask(__name__)



about_me = {
"name": "Мурат",
"surname": "Байрамуков",
"email": "Bay733@mail.ru"
}

@app.route("/about")
def about():
    return about_me



@app.route("/")   #первый URL который мы обробатываем
def hello_world():   #Это функц-обработчик будет вызван при запросе УРЛ
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
