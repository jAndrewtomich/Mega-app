from flask import Bluprint

bp = Blueprint('errors', __name__)

from app.errors import handlers

