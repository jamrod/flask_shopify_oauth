import json
import flask

app = Flask(__name__)

NONCE = None


@app.route('/install_app')
def start_request():
    shop = request.args.get('shop')
