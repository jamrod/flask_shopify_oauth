import hmac
import hashlib
import base64
import re


def verify_hmac(data, hmac_header, SECRET):
    digest = hmac.new(
        SECRET.encode('utf-8'),
        data.encode('utf-8'),
        hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest)
    # print("compare: " + computed_hmac.decode() + " " + hmac_header)

    return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))


def valid_shop_name(name):
    shop_regex = r'[a-zA-Z0-9][a-zA-Z0-9\-]*\.myshopify\.com[\/]?'
    return re.match(shop_regex, name) != None
