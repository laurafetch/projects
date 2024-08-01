import datetime
from flask import Blueprint, jsonify, abort, request
from ..models import db, Food, ShoppingList

bp = Blueprint('shopping', __name__, url_prefix='/shopping')

@bp.route('', methods=['GET'])
def shopping_list():
    list = ShoppingList.query.all()
    result = []
    for i in list:
        result.append(i.serialize())
    return jsonify(result)

## Add item to shopping list
## TODO: confirm food_id exists
@bp.route('', methods=['POST'])
def create():
    if 'food_id' not in request.json:
        return abort(400)
     
    i = ShoppingList(
        food_id=request.json['food_id'],
        num_units=request.json['num_units'],
        date_added=datetime.datetime.utcnow
    )
    db.session.add(i)
    db.session.commit()
    return jsonify(i.serialize())

## Remove item from shopping list
@bp.route('/<int:food_id>', methods=['DELETE'])
def delete(food_id: int):
    i = ShoppingList.query.get_or_404(food_id)
    try:
        db.session.delete(i)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)    

## Change number of units needed in shopping list
@bp.route('/<int:food_id>', methods=['PATCH', 'PUT'])      
def update(food_id: int, num_units: int):
    f = ShoppingList.query.get_or_404(food_id)

    f.num_units = request.json['num_units']

    try:
        #db.session.update(u)
        db.session.commit()
        return jsonify(f.serialize())
        return jsonify(True)
    except:
        return jsonify(False)    

