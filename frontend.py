# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask import Flask, render_template, request

from .forms import *
from .nav import nav
import hashlib

#from extensions import db
import MySQLdb as mdb
con = mdb.connect('localhost', 'root', 'root', 'team5')
frontend = Blueprint('frontend', __name__)
cursor = con.cursor()

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
        id = request.form.get('id')

        # vulnerable to sql injection!
        cursor.execute("SELECT username FROM User WHERE userID='" + id + "'")

        username = cursor.fetchone()
        if 'username' in session and session['username'] == username:
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
    return redirect(url_for('login.route'))


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/signup', methods=('GET', 'POST'))
def signup_route():
    form = SignupForm(request.form)


    if request.method == 'POST' and form.validate():
        '''
        print form.firstname.data
        print form.lastname.data
        print form.email.data
        print form.zipcode.data
        print form.age.data
        print form.diagnosis.data
        print form.community.data
        print form.private.data
        print form.searchable.data
        print form.bio.data
        print form.gender.data
        print "HI"

        '''





        cursor.execute('INSERT INTO User firstname, lastname, email, location, age, diagnosis, community, private, searchable, bio, gender' +
                       ' VALUES("' + form.firstname.data + '","' + form.lastname.data + '","' + form.email.data + '",' + form.zipcode.data + ',' + form.age.data + ',"' + form.diagnosis.data + '","' + form.community.data + '",' + form.private.data + ',' + form.searchable.data + ',"' + form.bio.data + '","' + form.gender.data + '" )')
        return redirect(url_for('.login'))

    return render_template('signup.html', form=form)

@frontend.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():

        # hash password for check against db
        m = hashlib.md5()
        m.update(form.password)
        hashed_pass = m.hexdigest()

        if hashed_pass == cursor.exicute("SELECT password FROM User WHERE email='" + form.email + "'").fetchone():

            # login was good! Congrats
            flash('Logged in successfully.')
            session['username'] = form.email.data
            return redirect(url_for('.messages'))

    # login was bad :(
    return render_template('login.html', form=form)




