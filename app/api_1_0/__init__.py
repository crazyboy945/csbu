from flask import Blueprint

api = Blueprint('api', __name__)

from app.model.contract  import Contract
from app.model.user import User

