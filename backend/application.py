from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from anagrams import AnagramFinder

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/anagram": {"origins": "*"}})


class AnagramAPI(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('stem', type=str)
        stem = parser.parse_args()['stem']
        anagram_list = AnagramFinder(stem).anagrams_by_length()
        return anagram_list

api.add_resource(AnagramAPI, '/anagram', endpoint='anagram')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
