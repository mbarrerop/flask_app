from flask_marshmallow import Marshmallow
from flask_migrate import Migrate 
from concurrent.futures import ThreadPoolExecutor
from decouple import config


ma = Marshmallow()
migrate = Migrate()
