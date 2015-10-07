from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    #request.args is a dict that will be filled with keys and values from any forms on the previous page
    answer = request.args.get('answer')
    if answer == "yes":
        #render a different template, game.html 
        return render_template("game.html")
        #add a simple form that asks for a person, a color, a noun, and an adjective
    else:
        return render_template("goodbye.html")
        #send them to goodbye.html and say "goodbye"
    return 8

@app.route('/madlib')
def show_madlib():
    person = request.args.get('person')
    color = request.args.get('color')
    noun =  request.args.get('noun')
    adjective = request.args.get('adjective')

    country = request.args.get('country')
    feelings = request.args.get('feelings')

    madlibs = ["madlib.html","madlibs2.html"]

    madlibchoice = choice(madlibs)
    print madlibchoice

    return render_template(choice(madlibs),person=person, color=color, noun=noun, adjective=adjective,country=country,feelings=feelings)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
