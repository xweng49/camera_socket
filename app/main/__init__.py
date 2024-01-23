from flask import Blueprint
from flask_restx import Api


main = Blueprint('main', __name__)
api_blueprint = Blueprint('api', __name__)



apiApp = Api(api_blueprint,
          title='api',
          description='API')

from . import routes, socket
from .api import api as ns1

apiApp.add_namespace(ns1)