# Extensions
from marshmallow import fields
from src.config.extensions import ma

class UploadMoviesSchema(ma.Schema):
    file = fields.String(required=True)
    