import json
import uuid

from flask import Flask, redirect, request, render_template
from config import API_KEY, REDIRECT_URI, SCOPES, SECRET
from helpers import verify_hmac, valid_shop_name

app = Flask(__name__)

NONCE = None


@app.route('/')
def test_route():
    return "Flask Token Generator Running!"


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
    # first check NONCE
    state = request.args.get('state')
    if state != NONCE:
        return "Invalid 'state' received", 400
    NONCE = None
    # then check hmac
    req_args = request.args
    hmac = req_args.pop('hmac')
    verified = verify_hmac(req_args, hmac, SECRET)
    if not verified:
        print("hamc verification error")
    # then check shop name is valid
    shop = request.args.get('shop')
    if shop:
        valid_name = valid_shop_name(shop)
        if not valid_name:
            return "Invalid shop name", 400
    else:
        return "No shop name", 400
    # all checks having passed accept token
    token = request.args.get('code')
    # do something with token here
    print(token)
    # render welcome screen
    return render_template('welcome.html', shop=shop)


if __name__ == '__main__':
    app.run()
