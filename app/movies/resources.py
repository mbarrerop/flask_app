from flask import Blueprint, request, Response
from flask_restful import Api


from app.movies.services import MoviesList
blueprint = Blueprint('movies', __name__, url_prefix='/movies')

api = Api(blueprint)

api.add_resource(MoviesList, '/list', endpoint='movies_list')