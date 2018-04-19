import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.mysql import MySQL
import constraint
from recipe import recipe

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)


@app.route('/show')
def show_recipes():
    height = request.args.get('height')
    weight = request.args.get('weight')
    age = request.args.get('age')
    gender = request.args.get('gender')
    activity = request.args.get('activity')
    satisfied_recipes = recipe(age, height, weight, gender, activity)

    entries = []
    for item in satisfied_recipes:
        print(' '.join(item))
        entries.append(' '.join(item))
    return render_template('recipeRecommend.html', entries=entries)


@app.route('/', methods=['GET', 'POST'])
def choose_flavor():
    if request.method == 'POST':
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        gender = request.form['gender']
        activity = request.form['activity']
        return redirect(url_for('show_recipes', age=age, height=height, weight=weight, gender=gender, activity=activity))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0')
