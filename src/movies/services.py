
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
    A class representing a RESTful resource for retrieving a list of movies.

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

        This method fetches movie data from a specified file, performs optional pagination,
        and returns the data as JSON.

        Returns:
            flask.Response: A Flask response with a JSON object containing the movie data.
            The status_code is 200 for a successful response.

        Raises:
            UploadFile: When the request does not contain valid movie data.
        """
        max_records = 30

        f_name = request.args.get('file_name', None)
        page = request.args.get('page', None)

        if page:
            start = (int(page) - 1) * max_records
            end = start + max_records

        
        if not f_name:
            f_name = config('MOVIES_FILE_NAME')

        glg = GoogleStorage()
        
        _file = glg._get_file(f_name)

        if not _file:
            raise UploadFile()
        
        df = pd.read_csv(io.StringIO(_file))

        if page:
            df = df.iloc[start:end]
            
        # Convert the DataFrame to a JSON object with 'records' orientation
        json_data = df.to_json(orient='records')


        response = jsonify({'status_code': 200, 'data': json.loads(json_data),
                            'page': page})
        return response