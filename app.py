from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

import database

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('animal', type=str, help='Name of animal to be inserted/updated.')
parser.add_argument('characteristics', type=str, help='Characteristics of animal to be inserted.')
parser.add_argument('position', type=int, help='The position of the animal in the calendar.')

# Chinese Zodiac
# This is the resource for getting, updating, or deleting individual zodiac animals.
class ChineseZodiac(Resource):
    # get  animal
    def get(self, name):
        animal = database.find_animal(name)
        if animal is not None:
            return animal, 200
        abort(404, message="Animal {} doesn't exist!".format(name))

    # update animal
    def put(self, name):
        kwargs = {}
        args = parser.parse_args()
        for key in args.keys():
            if args[key] is not None:
                kwargs[key] = args[key]
        animal = database.update_animal(name, **kwargs)
        if animal is not None:
            return animal, 200
        abort(404, message="Animal {} doesn't exist!".format(name))

    # delete animal
    def delete(self, name):
        success = database.delete_animal(name)
        if (success):
            return None, 200
        abort(404, message="Animal {} doesn't exist!".format(name))


# This is the resource for getting and updating the list of zodiac animals.
class ChineseZodiacList(Resource):
    # get list of animals
    def get(self):
        animals = database.get_animals()
        return animals, 200

    # post a new animal in the list
    def post(self):
        args = parser.parse_args()
        name = args["animal"]
        characteristics = args["characteristics"]
        position = args["position"]
        animal = database.insert_animal(name, characteristics, position)
        return animal, 200


api.add_resource(ChineseZodiacList, '/zodiac/chinese')
api.add_resource(ChineseZodiac, '/zodiac/chinese/<string:name>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)