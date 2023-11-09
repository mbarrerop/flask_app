# Extensions
from marshmallow import fields
from src.config.extensions import ma

class UploadMoviesSchema(ma.Schema):
    files = fields.String(required=True)
    