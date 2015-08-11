# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import json as pyjson
import os
from flask_orator import Orator

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = True
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'sqlite',
        'database': 'orator-models-branch.db'
    }
}
# import models
db = Orator(app)


@app.route('/q')
def q():
    data = models.User.all().to_dict()
    return str(data)

@app.route('/')
def index():
    if 'username' in session:
        # return
        return "Logged in as %s " % escape(session['username']) + escape(str(session)[1:-1])
    return 'You are not logged in'


# {"username":"aa", "title":"bbb", "tag":"dskalda", "announcement":"dskaldaks", "date":"dsjkaldsa"}
@app.route('/create', methods=['POST'])
def create():
    post = request.get_json(force=True)

    tag_id = models.Tag.where('name', post['tag']).first().id
    user_id = models.User.where('username', post['username']).first().id
    new_post = models.Post.create(
        title=post['title'],
        content=post['announcement'],
        user_id=user_id,
        tag_id=tag_id
    )

    if new_post is not None:
        response = models.Post.where('title', post['title']).where('tag_id', tag_id).first()
        response_dict = {'username': response.user.username,
                         'title': response.title,
                         'tag': response.tag.name,
                         'announcement': response.content
                         }
        return jsonify(response_dict)




@app.route('/aq', methods=['POST'])
def aq():
    request_string = request.get_json(force=True)
    data = {"username": str(escape(request_string['username'])), "password": str(escape(request_string['password']))}

    return pyjson.dumps(data)


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


#   testing json methods
# @app.route('/test', methods=['POST'])
# def test():
#     #json_string = json.dump(request.form)
#
#     return jsonify(**json.loads(json.htmlsafe_dump(json.loads(request.data))))
#     #return "%(username)s  %(password)s" % request.form

@app.route('/loginjson', methods=['GET', 'POST'])
def loginjson():
    if request.method == 'POST':
        credentials = request.get_json(force=True)

        credentials['username'] = str(escape(credentials['username']))  # lemme escape 'em first
        credentials['password'] = str(escape(credentials['password']))  # and let there be string, god said

        user = validate(credentials['username'], credentials['password'])
        if user != None:  # just kiddin'
            session['username'] = credentials['username']
            session['password'] = credentials['password']
            session['user_id'] = user.id

            data = {"username": str(escape(session['username'])), "user_id": user.id,
                    "password": str(escape(session['password']))}

            return jsonify(data)


    return 'not logged in'


def validate(u, p):
    user = models.User.where('username', u).where('password', p).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return jsonify(request.get_json(force=True))
        # json_string = '{"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},{"firstName":"Peter", "lastName":"Jones"}]}'
        # aa = json.JSONEncoder().encode(json_string) =>
        # aa = json.loads(json_string) => to python obj

        # data = {"id": str(album.id), "title": album.title}
        # json.dumps(data)

        # session['username'] = request.form['username']
        # session['password'] = request.form['password']
        # return redirect(url_for('index'))


        # v = validate_func( jsonify(request.form))
        # if v == True
        #   return redirect(url_for('index')

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
