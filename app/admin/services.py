# Flask API
from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError

# Schemas
from app.admin.schemas import UploadMoviesSchema

# Exceptions
from app.core.exceptions import AppErrorBaseClass, UploadFile, FileNotExist

# External services
from app.core.google_api import GoogleStorage

# Utils
from app.core.utils import val_existing_file

class AdminMoviesList(Resource):
    
    def post(self):
        
        upload_file = None
        upload_schema = UploadMoviesSchema()
        
        data = request.get_json()
        movie_body = upload_schema.load(data)
        
        if not movie_body:
            raise ValidationError()
        
        f_path = movie_body.get('path')
        f_exists, f_name = val_existing_file(f_path)
        
        if not f_exists and not f_name:
            raise FileNotExist()
        
        glg = GoogleStorage()
        upload_file = glg._upload_files(f_name, f_path)
        
        if not upload_file:
            raise UploadFile()
            
        response = jsonify({'status_code': 200, 'uploaded': upload_file})
        return response

