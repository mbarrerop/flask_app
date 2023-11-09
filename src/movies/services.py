
# Flask API
from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError

# Exceptions
from src.core.exceptions import UploadFile 

# External services
from src.core.google_api import GoogleStorage

# Utils
from decouple import config
import pandas as pd
import json
import io

class MoviesList(Resource):
    """
    A class representing a RESTful resource for listing movies.

    Attributes:
        None

    Methods:
        get(): Handles the HTTP GET request to retrieve a list of movies.

    Example usage:
        resource = MoviesList()
    """

    def get(self):
        """
        Handles the HTTP GET request to retrieve a list of movies.

        This method fetches a CSV file from Google Cloud Storage, reads it into a Pandas DataFrame,
        and converts the DataFrame to a JSON response.

        Returns:
            flask.Response: A Flask response containing the list of movies in JSON format.
        
        Raises:
            UploadFile: If the requested file is not found in Google Cloud Storage.
        """
        f_name = config('MOVIES_FILE_NAME')
        glg = GoogleStorage()
        
        _file = glg._get_file(f_name)
        
        if not _file:
            raise UploadFile()
            
        df = pd.read_csv(io.StringIO(_file))
        json_data = df.to_json(orient='records')
        
        response = jsonify({'status_code': 200, 'data': json.loads(json_data)})
        return response