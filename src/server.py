import json
import uuid

from flask import Flask, redirect, request, render_template
from config import API_KEY, REDIRECT_URI, SCOPES, SECRET
# from helpers import verify_hmac

app = Flask(__name__)

NONCE = None


@app.route('/')
def test_route():
    return "I'm Running!"


@app.route('/install_app')
def start_request():
    global NONCE
    shop = request.args.get('shop')
    NONCE = uuid.uuid4().hex
    redirect_url = f"https://{shop}/admin/oauth/authorize?client_id={API_KEY}&scope={SCOPES}&redirect_uri={REDIRECT_URI}&state={NONCE}"

    return redirect(redirect_url, code=302)


@app.route('/welcome')
def get_token():
    global NONCE
    state = request.args.get('state')
    if state != NONCE:
        return "Invalid 'state' received", 400
    NONCE = None

    # hmac = request.args.get('hmac')
    # verified = verify_hmac(request, hmac, SECRET)

    # if not verified:
    #     print("hamc verification error")

    token = request.args.get('code')
    print(token)
    shop = request.args.get('shop')

    return render_template('welcome.html', shop=shop)


if __name__ == '__main__':
    app.run()
