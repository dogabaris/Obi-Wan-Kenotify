# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify, flash
from flask.ext.sqlalchemy import SQLAlchemy
import json as pyjson
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    if 'username' in session:
        # return
        return "Logged in as %s " % escape(session['username']) + escape(str(session)[1:-1])
    return 'You are not logged in'


@app.route('/post/create', methods=['GET', 'POST'])
def post_crate():
    if 'username' in session:
        if request.method == 'POST':
            # TODO: validate data

            data = {'author_id': session['user_id'],
                    'title': str(escape(request.form['title'])),
                    'tags': escape(request.form['tag']),
                    'content': escape(request.form['body'])
                    }
            return jsonify(data)

        return render_template('createpost.html')
    else:
        return 'NOT LOGGED IN'


@app.route('/json', methods=['POST'])
def json():
    request_string = request.get_json(force=True)
    data = {"username": str(escape(request_string['username'])), "password": str(escape(request_string['password']))}

    return jsonify(data)


#   Escapes data
@app.route('/jst', methods=['GET', 'POST'])
def jst():
    if request.method == 'POST':
        data = {"username": escape(request.form['username']), "password": escape(request.form['password'])}
        return jsonify(data)

    return render_template('jst.html')


@app.route('/loginjson', methods=['GET', 'POST'])
def loginjson():
    if request.method == 'POST':
        credentials = request.get_json(force=True)

        credentials['username'] = str(escape(credentials['username']))  # lemme escape 'em first
        credentials['password'] = str(escape(credentials['password']))  # and let there be string, god said

        user = validate(credentials['username'], credentials['password'])

        if user is not None:
            session['username'] = credentials['username']
            session['password'] = credentials['password']
            session['user_id'] = user.id

            data = {"username": str(escape(session['username'])), "password": str(escape(session['password']))}

            return jsonify(data)


    return 'not logged in'


def validate(username, password):
    user = models.User.query.filter_by(username=username, password=password).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return 'Already logged in'

    if request.method == 'POST':
        user = validate(request.form['username'], request.form['password'])

        if user is not None:
            session['username'] = str(escape(request.form['username']))
            session['password'] = str(escape(request.form['password']))
            session['user_id'] = user.id

            return redirect(url_for('post_crate'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)


    # json_string = '{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}'
    # aa = json.JSONEncoder().encode(json_string) => to python obj
    # aa = json.loads(json_string) => to python obj

    # data = {"id": str(album.id), "title": album.title}
    # json.dumps(data)

    # session['username'] = request.form['username']
    # session['password'] = request.form['password']
    # return redirect(url_for('index'))


    # v = validate_func( jsonify(request.form))
    # if v == True
    #   return redirect(url_for('index')
