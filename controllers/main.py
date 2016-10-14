from flask import *
from extensions import db

main = Blueprint('main', __name__, template_folder='templates')

cursor = db.cursor()

@main.route('/')
def main_route():
    return render_template("index.html", **options)