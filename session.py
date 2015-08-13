# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify, abort
import json as pyjson
import os
from flask.json import jsonify
from flask_orator import Orator
from datetime import datetime
from dateutil import parser

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = True
app.config['ORATOR_DATABASES'] = {
    'development': {
        'driver': 'sqlite',
        'database': 'orator-models-branch.db'
    }
}

import models

db = Orator(app)


@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'status_code': 400,
                        'message': error.description})
    response.status_code = 400
    return response


@app.errorhandler(403)
def forbidden(error):
    response = jsonify({'status_code': 403,
                        'message': error.description})
    response.status_code = 403
    return response


@app.errorhandler(404)
def forbidden(error):
    response = jsonify({'status_code': 404,
                        'message': error.description})
    response.status_code = 404
    return response

@app.route('/q')
def q():
    data = models.Post.where('id', 1).first().test()
    return jsonify(results=data)


@app.route('/')
def index():
    if 'username' in session:
        # return
        return "Logged in as %s " % escape(session['username']) + escape(str(session)[1:-1])
    return 'You are not logged in'


# {"username":"aa", "title":"bbb", "tag":"dskalda", "announcement":"dskaldaks", "date":"dsjkaldsa"}
@app.route('/create', methods=['POST'])
def create():
    #   session control, role control, sessiondan userı al, gelenle kontrol et
    expected_key_list = ['username',
                         'title',
                         'tag',
                         'announcement',
                         'published_at']
    post = request.get_json(force=True)

    if ('username' in session) and (session['username'] == post['username']):

        if sorted(expected_key_list) != sorted(post.keys()):
            abort(400, 'Invalid request.')

        tag = models.Tag.where('name', post['tag']).first()
        if tag is None:
            abort(404, 'Tag can\'t found')

        # validate if user have this role
        if check_role(session['roles'], tag) is not True:
            abort(403, 'You do not have permission for this tag.')

        user = models.User.where('id', session['user_id']).first()
        published_at = post['published_at']  # parser.parse()

        new_post = user.posts().create(
            title=post['title'],
            content=post['announcement'],
            tag_id=tag.id,
            published_at=published_at
        )

        new_post.user()
        new_post.tag()
        if new_post is not None:
            response = jsonify(Post=new_post.to_dict())
            response.status_code = 201
            return response

    else:
        return abort(403, 'You need to login to create a post.')


def check_role(roles_list, r):
    for role in roles_list:
        if role['name'] == r.name:
            return True

    return False


@app.route('/loginjson', methods=['GET', 'POST'])
def loginjson():
    if request.method == 'POST':
        credentials = request.get_json(force=True)

        credentials['username'] = str(escape(credentials['username']))  # lemme escape 'em first
        credentials['password'] = str(escape(credentials['password']))  # and let there be string, god said

        user = validate(credentials['username'], credentials['password'])
        if user is not None:
            user.roles()  # Load roles
            session['username'] = credentials['username']
            session['password'] = credentials['password']
            session['user_id'] = user.id
            session['roles'] = user.roles.to_dict()  # session['roles'][0]['name']

            # data = {"username": str(escape(session['username'])), "user_id": user.id,
            # "password": str(escape(session['password']))}



            return jsonify(Profile=user.to_dict())

    return 'not logged in'


def validate(u, p):
    user = models.User.where('username', u).where('password', p).first()
    return user

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
