# Flask API
from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError

# Schemas
from app.admin.schemas import UploadMoviesSchema

# Exceptions
from app.core.exceptions import UploadFile, FileNotExist, InvalidFileName

# External services
from app.core.google_api import GoogleStorage

# Utils
from app.core.utils import val_existing_file

class AdminMoviesList(Resource):
    """
    A class representing a RESTful resource for managing movie files.

    Attributes:
        None

    Methods:
        post(): Handles the HTTP POST request to save a Netflix titles file to Google Cloud Storage.

    Example usage:
        resource = AdminMoviesList()
    """

    def post(self):
        """
        Handles the HTTP POST request to save a Netflix titles file to Google Cloud Storage.

        This method manages the uploaded file, verifies its validity, and saves it to Google Cloud Storage.

        Returns:
            flask.Response: A Flask response with a JSON object containing the result. If the upload is successful,
                            the status_code is 200.

        Raises:
            UploadFile: When the request does not contain files.
            InvalidFileName: When the uploaded file has an invalid name.
            UploadFile: When there are failures while updating the netflix_titles.csv file in Google Cloud Storage.
        """
        
        # Manage the file and events
        upload_file = None
        if 'file' not in request.files:
            raise UploadFile()
        
        file = request.files['file']
        
        if file.filename == '':
            raise InvalidFileName()
        
        if file:
            file_data = file.read()
        
        # Sending to Google Storage
        glg = GoogleStorage()
        upload_file = glg._upload_files(file.filename, file_data)
        
        if not upload_file:
            raise UploadFile()
            
        response = jsonify({'status_code': 200, 'uploaded': upload_file})
        return response

