"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_id(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member is None:
            return jsonify({"message": "Id incorrecto"}), 400
        return jsonify(member), 200
    
    except Exception as error:
        print(error)
        return  "No se puede acceder al miembro", 500
        




@app.route('/member', methods=['POST'])
def create_user():
    try:
        body = request.json
        result = jackson_family.add_member(body)
        if result:
            return jsonify([result]), 200
    except Exception as error:
        return jsonify({"messasge": "Intento fallido al agregar un nuevo miembro"}), 400
    
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        result = jackson_family.delete_member(id)
        if result:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"message": "User con el id proporcionado no existe"}), 404
    except Exception as error:
        return jsonify({"message": "Ha ocurrido un error"}), 500




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
