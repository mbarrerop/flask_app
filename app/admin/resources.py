from flask import Blueprint, request, Response
from flask_restful import Api


from app.admin.services import AdminMoviesList
blueprint = Blueprint('admin_movies', __name__, url_prefix='/admin')

api = Api(blueprint)


api.add_resource(AdminMoviesList, '/manage-movies', endpoint='admin_movies_list')