from flask import Flask, render_template
#import extensions
import controllers
import config

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.album, url_prefix='/zeb62w5z/p1')
app.register_blueprint(controllers.albums, url_prefix='/zeb62w5z/p1')
app.register_blueprint(controllers.pic, url_prefix='/zeb62w5z/p1')
app.register_blueprint(controllers.main, url_prefix='/zeb62w5z/p1')

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)
