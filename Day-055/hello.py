from flask import Flask
app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media4.giphy.com/media/1nUkRa68hPskXLOjIh/giphy.gif?cid=ecf05e4775kyj6ivo6fi1izxzecs4x1d56m0nzhgugquuo21&rid=giphy.gif&ct=g" width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)