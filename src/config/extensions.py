from flask_marshmallow import Marshmallow
from flask_migrate import Migrate 
from concurrent.futures import ThreadPoolExecutor
from decouple import config
from flask_restx import Api

ma = Marshmallow()
migrate = Migrate()
fx_api = Api()
