# Flask API
from flask_restx import Namespace, fields
from config.extensions import fx_api
from flask_restful import Resource
from flask import request, jsonify

# Schemas
from .schemas import UploadMoviesSchema

# Exceptions
from src.core.exceptions import UploadFile, FileNotExist, InvalidFileName

# External services
from src.core.google_api import GoogleStorage

# Utils

from aiohttp import ClientSession
import asyncio

ns = Namespace(name='',description='Netflix API')
@ns.route('/admin/save-movies')
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
        
        responses = list()
        # Manage the file and events
        files = request.files.getlist('files')
        upload_file = None
        if not files:
            raise UploadFile()
        
        glg = GoogleStorage()

        for file in files:
            # Sending to Google Storage
            file_data = file.read()
            upload_file = glg._upload_files(file.filename, file_data)
            responses.append(upload_file)
                
        response = jsonify({'status_code': 200, 'result': responses})
        return response

