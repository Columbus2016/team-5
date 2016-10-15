# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, session
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask.ext.login import LoginManager, UserMixin, login_required
from markupsafe import escape

from .forms import *
from .nav import nav

frontend = Blueprint('frontend', __name__)

# We're adding a navbar as well through flask-navbar. In our example, the
# navbar has an usual amount of Link-Elements, more commonly you will have a
# lot more View instances.
nav.register_element('frontend_top', Navbar(
    View('Home', '.index'),
    View('Signup', '.signup_route'),
    View('Login', 'debug.debug_root')
))


# Our index-page just shows a quick explanation. Check out the template
# "templates/index.html" documentation for more details.
@frontend.route('/')
def index():
    return render_template('index.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/signup', methods=('GET', 'POST'))
def signup_route():
    form = SignupForm()

    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.email.data)))

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

    return render_template('signup.html', form=form)

@frontend.route('/login', methods=['GET', 'POST'])
def login_route():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():

        flash('Logged in successfully.')
        session['username'] = form.email.data

        return redirect(url_for('.index'))
    return render_template('login.html', form=form)

