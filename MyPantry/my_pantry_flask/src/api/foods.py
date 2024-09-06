import datetime
from flask import Blueprint, jsonify, abort, request
from ..models import db, Inventory

bp = Blueprint('foods', __name__, url_prefix='/foods')

@bp.route('', methods=['GET'])
def index():
    foods = Inventory.query.all()
    result = []
    for f in foods:
        result.append(f.serialize())
    return jsonify(result)