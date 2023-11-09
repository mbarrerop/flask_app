
from google.cloud import storage
from decouple import config, Csv
import json
import os
class GoogleAPI():
    
    def __init__(self) -> None:
        self.__api_keys = self.__build_secret_key()
        self._client = self.__connect_google_cloud()
    def __connect_google_cloud(self):
        storage_client = storage.Client.from_service_account_info(self.__api_keys)
        return storage_client

    def __build_secret_key(self):
        
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
    
    def __init__(self) -> None:
        super().__init__()
        self.__bucket_name = config('BUCKET_NAME')
        self.__bucket_loc = config('BUCKET_LOCATION')
        self.__current_bucket = None
    
    def _upload_files(self, blob_name: str, file_path: str):
        try:
            self.__validate_bucket()
            blob = self.__current_bucket.blob(blob_name)
            blob.upload_from_filename(file_path)
            return True
        except Exception as e:
            return False
    
    def _get_file(self, blob_name: str):
        
        try:
            self.__validate_bucket()
            blob = self.__current_bucket.blob(f'{blob_name}')
            content = blob.download_as_text()
            return content
        except Exception as e:
            return None
           
    def __validate_bucket(self):
        
        try:
            self.__current_bucket = self._client.get_bucket(self.__bucket_name)
        except:
            if not self.__current_bucket:
                self.__create_bucket()
        
    def __create_bucket(self):
        
        bucket = self._client.bucket(self.__bucket_name)
        bucket.location = self.__bucket_loc
        self.__current_bucket = self._client.create_bucket(bucket)
     