from app import create_app, socketio
import json

app = create_app(debug=True)

if __name__ == "__main__":
    socketio.run(app)