# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask.ext.login import LoginManager, UserMixin, login_required
from markupsafe import escape

from .forms import *
from .nav import nav
import hashlib
#from extensions import db

from extensions import db

frontend = Blueprint('frontend', __name__)
#cursor = db.cursor()

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

@frontend.route('/user', methods=('GET', 'POST'))
def user_route():
    return render_template('user.html')

# Shows a long signup form, demonstrating form rendering.
@frontend.route('/signup', methods=('GET', 'POST'))
def signup_route():
    form = SignupForm()

    if form.validate_on_submit():
        cursor.execute('INSERT INTO User firstname, lastname, email, location, age, diagnosis, community, private, searchable, bio' +
                       ' VALUES()')
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

        if hashed_pass == cursor.exicute("SELECT * FROM User WHERE email='" + form.email + "'").fetchone():

            # login was good! Congrats
            flash('Logged in successfully.')
            session['username'] = form.email.data
            return redirect(url_for('.messages'))

    # login was bad :(
    return render_template('login.html', form=form)




