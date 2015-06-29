from app import app, db
from flask import jsonify, request
from .models import Board
import sqlalchemy

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/boards', methods=['GET', 'POST'])
def boards():
    if request.method == "GET":
        return jsonify(boards = [i.serialize for i in Board.query.all()])
    else:
        if not request.json or not 'shortname' in request.json or not 'name' in request.json:
            return jsonify({'status': 'missing args'})
        if not 'description' in request.json:
            new_board = Board(request.json['shortname'],
                                  request.json['name'])
        else:
            new_board = Board(request.json['shortname'],
                                  request.json['name'],
                                  request.json['description'])
        try:
            db.session.add(new_board)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'status': 'duplicate entry'})
        return jsonify({'status': 'okay'})
