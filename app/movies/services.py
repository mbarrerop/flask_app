
# Flask API
from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError

# Schemas
from app.admin.schemas import UploadMoviesSchema

# Exceptions
from app.core.exceptions import UploadFile, FileNotExist

# External services
from app.core.google_api import GoogleStorage

# Utils
from decouple import config
import pandas as pd
import json
import io

class MoviesList(Resource):
    
    def get(self):     
        
        f_name = config('MOVIES_FILE_NAME')
        glg = GoogleStorage()
        
        _file = glg._get_file(f_name)
        
        df = pd.read_csv(io.StringIO(_file))
        json_data = df.to_json(orient='records')
        
        if not _file:
            raise UploadFile()
            
        response = jsonify({'status_code': 200, 'data': json.loads(json_data)})
        return response