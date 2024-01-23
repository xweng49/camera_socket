from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")

def create_app(debug=False):
    """
    Create an application

    Args:
        debug (bool, optional): launches app in debug mode. Defaults to False.
    """
    app = Flask(__name__, static_folder="./templates/static")
    app.debug=debug
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    socketio.init_app(app)
    return app
    