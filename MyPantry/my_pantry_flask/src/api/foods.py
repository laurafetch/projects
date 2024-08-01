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

"""
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)

    username = request.json['username']
    password = request.json['password']

    if len(username) < 3 or len(password) < 8:
        return abort(400)
     
    u = User(
        username=username,
        password=scramble(password)
    )
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)    

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])      
def update(id: int):
    u = User.query.get_or_404(id)

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)    

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])

    try:
        #db.session.update(u)
        db.session.commit()
        return jsonify(u.serialize())
        return jsonify(True)
    except:
        return jsonify(False)         

@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)           
"""    