from flask import Blueprint, request, Response
from flask_restful import Api


from .healthcheck import HealthCheckSystem
blueprint = Blueprint('healthcheck', __name__, url_prefix='/state')

api = Api(blueprint)

api.add_resource(HealthCheckSystem, '/healthcheck', endpoint='health_check_system')