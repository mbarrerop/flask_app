from typing import Any
from datetime import datetime
from werkzeug.exceptions import HTTPException 


class AbstracException(Exception):
    """Base class for all exceptions."""

    status_code = 400
    code_type: str
    detail: str
    date_time: datetime

    def __init__(self, status_code: int = 400, detail: Any = None) -> None:
        """Initialize the exception.

        Args:
            status_code (int): HTTP status code
            detail (Any, optional): Exception detail. Defaults to None.
        """

        detail = {
            "code_type": self.code_type,
            "detail": detail if detail else self.detail,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        status_code = status_code if status_code else self.status_code

        super().__init__(status_code, detail)


class ValidationError(AbstracException):
    """Error for data submitted by the user."""

    status_code = 400
    code_type = "#01"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("The data submitted by the user is not valid")


class NotFoundError(AbstracException):
    """Error for data not found."""

    status_code = 400
    code_type = "#02"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("The data was not found")

class DatabaseError(AbstracException):
    """Error for database."""

    status_code = 500
    code_type = "#03"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Something went wrong with the database")
    
class MappingError(AbstracException):
    """Error maping data submitted by the user."""

    status_code = 500
    code_type = "#04"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Error mapping data from database")
    
class AppErrorBaseClass(AbstracException):
    status_code = 500
    code_type = "#05"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Something went wrong with the app")

class ObjectNotFound(AbstracException):
    status_code = 500
    code_type = "#06"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Object not found")
    
class UploadFile(AbstracException):
    status_code = 500
    code_type = "#07"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Something went wrong uploading file to Google Storage")
    
class FileNotExist(AbstracException):
    status_code = 400
    code_type = "#08"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("File not found")
    
class InvalidFileName(AbstracException):
    status_code = 400
    code_type = "#09"
    date_time =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detail = ("Invalid file name")