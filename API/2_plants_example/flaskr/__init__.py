from flask import Flask, app, jsonify, request
from models import setup_db, Plant

from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup_db(app)
    #CORS(app, resources={r"*/api/*" : {origins: '*'}})
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
        return response

    #@cross_origin
    @app.route('/plants', methods=['POST', 'GET'])
    def get_plants():
        #pagination
        page = request.args.get('page',1, type=int)
        start = (page - 1)
        end = start + 10

        
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]
        return jsonify({
            'success': True,
            'Plants': formatted_plants[start:end],
            'Total_plants': len(formatted_plants)
        })

    @app.route('/plants/<int:plant_id>')
    def specific_plant(plant_id):

        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

        return jsonify ({
            'success': True,
            'Plant': plant.format()
            

        })
    


    return app