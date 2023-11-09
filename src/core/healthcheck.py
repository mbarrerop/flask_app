
# Flask API
from flask_restful import Resource
from flask import request, jsonify

# Tools
from time import time
from datetime import datetime, timedelta
import pytz

class HealthCheckSystem(Resource):
    
    def get(self):
        """Healthcheck service"""
    
        start = time()
        date = None
        
        try:
            date = self.datetime_utc_now()
            if not date:
                raise Exception('Container internal error')
        except Exception as e:
            content = {"error": str(e)}
            return jsonify({'status_code': 500, 'content': content})
    
        response_time = time() - start
        content = {"server_date": date, "response_time": response_time}
        return jsonify(content)
        

    def datetime_utc_now(self):
        """
        Funtion to transform the differents formats of dates in
        Verifik responses.
        
        Args:
            c_date (str):   A string with a specific format from
                            Verifik.
                            
        Returns:
            str:            A string formatted.
        """           
        time_zone = pytz.timezone('America/Bogota')
        dt = datetime.now(time_zone) + timedelta(hours=5)
        dt = dt.strftime('%Y-%m-%d %H:%M:%S')
        return str(dt)