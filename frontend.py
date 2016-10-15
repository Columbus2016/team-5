# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask import Flask, render_template, request
from flask.ext.wtf import Form
from wtforms import Form, TextField, BooleanField, PasswordField, TextAreaField, validators

from .forms import *
from .nav import nav
import hashlib
from extensions import db
#import MySQLdb as mdb
#con = mdb.connect('localhost', 'root', 'root', 'team5')

frontend = Blueprint('frontend', __name__)
cursor = db.cursor()

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('Home', '.index'),
    View('Signup', '.signup_route'),
    View('Login', '.login_route')
))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/createGroup')
def create_group():
    return render_template('creategroup.html')

@frontend.route('/user', methods=('GET', 'POST'))
def user_route():

    if request.method == 'GET':

        if not request.args.get('id'):
            # incorrect user! Redirect
            return redirect(url_for('frontend.login_route'))

        id = request.args.get('id')
        print ("id = " + id)

        # vulnerable to sql injection!
        cursor.execute("SELECT email FROM User WHERE userID='" + id + "'")
        username = cursor.fetchone()
        print (username)

        if 'username' in session and session['username'] == username:

            name = cursor.execute("SELECT firstname FROM User WHERE email='" + session['username'] + "'") + cursor.execute("SELECT lastname FROM User WHERE username='" + session['username'] + "'")
            email = cursor.execute("SELECT email FROM User WHERE email='" + session['username'] + "'")
            age = cursor.execute("SELECT age FROM User WHERE email='" + session['username'] + "'")
            gender = cursor.execute("SELECT gender FROM User WHERE email='" + session['username'] + "'")
            community = cursor.execute("SELECT diagnosis FROM User WHERE email='" + session['username'] + "'")
            group = cursor.execute("SELECT community FROM User WHERE email='" + session['username'] + "'")
            bio = cursor.execute("SELECT bio FROM User WHERE email='" + session['username'] + "'")

            return render_template('user.html')

    elif request.method == 'POST':
        id = request.form.get('id')
        field = request.form.get('field')
        data = request.form.get('data')

        # vulnerable to sql injection!
        cursor.execute("SELECT username FROM User WHERE userID='" + id + "'")

        username = cursor.fetchone()
        if 'username' in session and session['username'] == username:

            # update info
            cursor.execute("UPDATE User SET " + field + "= '" + data + "' WHERE userID='" + id + "'")

            #return new user page
            return render_template('user.html')


    # incorrect user! Redirect
    return redirect(url_for('frontend.login_route'))


@frontend.route('/forum', methods=('GET', 'POST'))
def forum_route():
    return render_template('forum.html')

# Shows a long signup form, demonstrating form rendering.
@frontend.route('/signup', methods=('GET', 'POST'))
def signup_route():
    form = SignupForm(request.form)

    if request.method == 'POST':
        cursor.execute('INSERT INTO User (firstname, lastname, email, password, location, age, diagnosis, community, bio, gender)' +
                       ' VALUES("' + form.firstname.data + '","' + form.lastname.data + '","' + form.email.data + '","' + form.password.data + '","'+ form.zipcode.data + '","' + form.age.data + '","' + form.diagnosis.data + '","' + form.community.data + '","' + form.bio.data + '","' + form.gender.data + '")')
        return redirect(url_for('frontend.login_route'))

    return render_template('signup.html', form=form)

@frontend.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if request.method == 'POST' and form.validate():

        if form.password == cursor.execute('SELECT password FROM User WHERE email="' + form.email.data + '"').fetchone():

            # login was good! Congrats
            flash('Logged in successfully.')
            session['username'] = form.email.data
            return redirect(url_for('frontend.index'))


    print ("Login not validated!")
    return render_template('login.html', form=form)




