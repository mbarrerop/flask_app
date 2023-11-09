# Extensions
from marshmallow import fields
from app.config.extensions import ma

class UploadMoviesSchema(ma.Schema):
    path = fields.String(required=True)
    