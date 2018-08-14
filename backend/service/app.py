import os
from flask import Flask
from flask_cors import CORS
from blackfynn import Blackfynn

from service.config import Config

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

import routes