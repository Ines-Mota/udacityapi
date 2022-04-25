from flask import Flask
from flask_cors import CORS
from models import setup_db, Plant

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"*/api/*": {'origin':"*"}}) #RESOURCE-SPECIFIC USAGE: specifies which sources can get access to the api, the * means 
                                                    #anything can come before and after 'api', and in origins * means all origins are allowed


    @app.after_request #decorator "after a request is received run this method"
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

#@cross_origin  --to enable CORS on a given route
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    return app
