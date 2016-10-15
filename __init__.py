# Welcome to the Flask-Bootstrap sample application. This will give you a
# guided tour around creating an application using Flask-Bootstrap.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#
# Then, you can actually run the application.
#
#   $ flask --app=sample_app dev
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.

from flask import Flask
from flask.ext.login import LoginManager, UserMixin, login_required
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

from .frontend import frontend
from .nav import nav


def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)

    # We use Flask-Appconfig here, but this is not a requirement
    AppConfig(app)

    # Install our Bootstrap extension
    Bootstrap(app)

    # Our application uses blueprints as well; these go well with the
    # application factory. We already imported the blueprint, now we just need
    # to register it:
    app.register_blueprint(frontend)

    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    # We initialize the navigation as well
    nav.init_app(app)

    class User(UserMixin):
        # proxy for a database of users
        user_database = {"JohnDoe": ("JohnDoe", "John"),
                         "JaneDoe": ("JaneDoe", "Jane")}

        def __init__(self, username, password):
            self.id = username
            self.password = password

        @classmethod
        def get(cls, id):
            return cls.user_database.get(id)

    @login_manager.request_loader
    def load_user(request):
        token = request.headers.get('Authorization')
        if token is None:
            token = request.args.get('token')

        if token is not None:
            username, password = token.split(":")  # naive token
            user_entry = User.get(username)
            if (user_entry is not None):
                user = User(user_entry[0], user_entry[1])
                if (user.password == password):
                    return user
        return None

    return app
