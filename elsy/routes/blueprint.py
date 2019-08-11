from flask import Blueprint
from flask_cors import CORS

_bp = Blueprint("api", __name__, url_prefix="/api/v1")
CORS(_bp)
bp = _bp
