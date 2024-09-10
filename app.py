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

quotes = [
   {
    "id": 3,
    "author": "Rick Cook",
    "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
   {
    "id": 5,
    "author": "WaldiRavens",
    "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
    },
   {
    "id": 6,
    "author": "Mosher’s Law of Software Engineering",
    "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
   {
    "id": 8,
    "author": "YoggiBerra",
    "text": "В теории, теория и практика неразделимы. На практике это не так."
    },

]
# Нужно больше цитат? https://tproger.ru/devnull/programming-quotes/


@app.route("/quotes")
def quotes1():
    return quotes



@app.route("/")   #первый URL который мы обробатываем
def hello_world():   #Это функц-обработчик будет вызван при запросе УРЛ
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
