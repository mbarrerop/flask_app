
from app import create_app
from core.exceptions import ObjectNotFound, AppErrorBaseClass, FileNotExist
from flask import Flask, jsonify
from decouple import config

app = create_app()
if __name__ == '__main__':
    app.run(debug=True if config('DEBUG') == 'True' else False)