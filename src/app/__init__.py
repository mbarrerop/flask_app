
from flask import Flask, jsonify
from src.config.extensions import fx_api

def create_app():
    from src.admin.services import ns as admin
    from src.movies.services import ns as movies
    from src.admin.resources import blueprint as bp_admin
    from src.movies.resources import blueprint as bp_movies
    
    app = Flask(__name__)

    app.url_map.strict_slashes = False
    
    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_movies)
    
    register_error_handlers(app)
    fx_api.init_app(app)
    fx_api.add_namespace(admin)
    fx_api.add_namespace(movies)
    return app

def register_error_handlers(app):
    
    from src.core.exceptions import ObjectNotFound, AppErrorBaseClass, FileNotExist
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        if isinstance (e, dict): 
            return jsonify({'status_code': 500, 'error': e.messages_dict}), 500
        return jsonify({'status_code': 500, 'error': str(e)}), 500
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'status_code': 405, 'error': str(e)}), 405
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'status_code': 403, 'error': str(e)}), 403
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'status_code': 404, 'error': str(e)}), 404
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        response = jsonify({'error': e.detail, 'code': e.code_type, 'date_time': e.date_time})
        response.status_code = e.status_code
        return response
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        response = jsonify({'error': e.detail, 'code': e.code_type, 'date_time': e.date_time})
        response.status_code = e.status_code
        return response
    @app.errorhandler(FileNotExist)
    def handle_file_not_exists(e):
        response = jsonify({'error': e.detail, 'code': e.code_type, 'date_time': e.date_time})
        response.status_code = e.status_code
        return response