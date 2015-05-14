from random import choice
from flask import Flask, render_template, request

app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."


# route to display a simple web page
@app.route('/hello', methods=['GET', 'POST'])
def say_hello():
    return render_template("hello.html")


@app.route('/greet', methods=['POST'])
def greet_person():
    player = 'Anonymous person'
    if 'person' in request.form:
        player = request.form['person']
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
        'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
        'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player,
        compliment=compliment)


@app.route('/game', methods=['POST'])
def show_game_form():
    if request.form['play'] == 'yes':
        return render_template('game.html')
    else:
        return render_template('goodbye.html')


madlibs = [
    'There once was a {color} {noun} sitting in the Hackbright Lab. When \
    {person} went to pick it up, it burst into flames in a totally {adjective} \
    way.',
    'Every {color} {noun} waits for {adjective} stuff with {person}.',
]


@app.route('/madlib', methods=['POST'])
def show_madlib():
    random_variable = 42
    defaults = ['noun', 'person', 'color', 'adjective']
    args = dict()
    for el in defaults:
        args[el] = request.args.get(el, 'default')
    madlib = madlibs[0]
    madlib = madlib.format(**args)
    return render_template('madlib.html', madlib=madlib)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
