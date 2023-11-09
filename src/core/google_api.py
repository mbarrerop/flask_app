
from google.cloud import storage
from decouple import config, Csv
from typing import Optional
import asyncio

class GoogleAPI:
    """
    A class for interacting with Google Cloud 
    services using a service account.

    Attributes:
        _client (google.cloud.storage.Client): A client for interacting with Google Cloud Storage.

    Methods:
        __init__():                 Initializes a new instance of the GoogleAPI class.
        __connect_google_cloud():   Connects to Google Cloud using the provided service account credentials.
        __build_secret_key():       Builds the service account credentials dictionary.
    """

    def __init__(self):
        """
        Initializes a new instance of the GoogleAPI class.

        The GoogleAPI class is used to interact with Google Cloud 
        services using a service account.
        It connects to Google Cloud Storage and provides methods 
        for working with cloud storage.

        Usage:
            api = GoogleAPI()
        """
        self.__api_keys = self.__build_secret_key()
        self._client = self.__connect_google_cloud()

    def __connect_google_cloud(self):
        """
        Connects to Google Cloud using the provided service account credentials.

        Returns:
            google.cloud.storage.Client: A client for interacting with Google Cloud Storage.
        """
        storage_client = storage.Client.from_service_account_info(self.__api_keys)
        return storage_client

    def __build_secret_key(self) -> dict:
        """
        Builds the service account credentials dictionary.

        Returns:
            dict: A dictionary containing the service account credentials.
        """
        credentials_dict = {
            'type': 'service_account',
            "project_id": config('PROJECT_ID'),
            "private_key_id": config('PRIVATE_KEY_ID'),
            "private_key": config('PRIVATE_KEY').replace('\\n', '\n'),
            "client_email": config('CLIENT_EMAIL'),
            "client_id": config('CLIENT_ID'),
            "auth_uri": config('AUTH_URI'),
            "token_uri": config('TOKEN_URI'),
            "auth_provider_x509_cert_url": config('AUTH_PROVIDER'),
            "client_x509_cert_url": config('CLIENT'),
            "universe_domain": config('UNIVERSE_DOMAIN')
        }
        return credentials_dict
    
class GoogleStorage(GoogleAPI):
    """
    A class for interacting with Google Cloud Storage using a service account.

    Attributes:
        _client (google.cloud.storage.Client):                      A client for interacting with Google Cloud Storage.
        __bucket_name (str):                                        The name of the Google Cloud Storage bucket.
        __bucket_loc (str):                                         The location of the Google Cloud Storage bucket.
        __current_bucket (google.cloud.storage.bucket.Bucket):      The current Google Cloud Storage bucket.

    Methods:
        __init__():                             Initializes a new instance of the GoogleStorage class.
        _upload_files(blob_name, file_data):    Uploads a file to the Google Cloud Storage bucket.
        _get_file(blob_name):                   Retrieves the content of a file from the Google Cloud Storage bucket.
        __validate_bucket():                    Validates and retrieves the current Google Cloud Storage bucket.
        __create_bucket():                      Creates a new Google Cloud Storage bucket if it doesn't exist.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the GoogleStorage class.

        The GoogleStorage class extends the GoogleAPI class to provide methods for interacting with
        Google Cloud Storage using a service account. It allows you to upload and retrieve files
        from a specified storage bucket.

        Usage:
            storage = GoogleStorage()
        """
        super().__init__()
        self.__bucket_name = config('BUCKET_NAME')
        self.__bucket_loc = config('BUCKET_LOCATION')
        self.__current_bucket = None

    def _upload_files(self, blob_name: str, file_data: any) -> dict:
        """
        Uploads a file to the Google Cloud Storage bucket.

        Args:
            blob_name (str): The name of the blob (file) to be uploaded.
            file_data (any): The content of the file to be uploaded.

        Returns:
            dict: True if the file was successfully uploaded, False if an error occurred.
        """
        try:
            self.__validate_bucket()
            blob_name = blob_name.replace(' ', '_')
            blob = self.__current_bucket.blob(blob_name)
            blob.upload_from_string(file_data)
            return {'file_name': blob_name, 'uploaded': True}

        except Exception as e:
            return {'file_name': blob_name, 'uploaded': False}

    def _get_file(self, blob_name: str) -> Optional[str]:
        """
        Retrieves the content of a file from the Google Cloud Storage bucket.

        Args:
            blob_name (str): The name of the blob (file) to be retrieved.

        Returns:
            str: The content of the retrieved file, or None if the file does not exist.
        """
        try:
            self.__validate_bucket()
            blob = self.__current_bucket.blob(f'{blob_name}')
            content = blob.download_as_text()
            return content
        except Exception as e:
            return None

    def __validate_bucket(self) -> None:
        """
        Validates and retrieves the current Google Cloud Storage bucket.
        If the bucket does not exist, it attempts to create it.

        Returns:
            None
        """
        try:
            self.__current_bucket = self._client.get_bucket(self.__bucket_name)
        except:
            if not self.__current_bucket:
                self.__create_bucket()

    def __create_bucket(self) -> None:
        """
        Creates a new Google Cloud Storage bucket if it doesn't exist.

        Returns:
            None
        """
        bucket = self._client.bucket(self.__bucket_name)
        bucket.location = self.__bucket_loc
        self.__current_bucket = self._client.create_bucket(bucket)