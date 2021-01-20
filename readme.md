Flask shopify oauth token generator

this repo contains the basic code to generate oath tokens to allow programmatic access to Shopify stores. You need to set up a Shopify Partners account and create an "app" which will give you an API key that will be necessary to complete.

Not included in the repo is the config.py file, whilch should be located in the src folder and contins the API key and scopes, etc. use below as template

API_KEY = ""

SECRET = ""

REDIRECT_URI = "https://**\*\***.ngrok.io/welcome"

SCOPES = ""

start server: python src/server.py

start ngrok: ./ngrok http 5000
