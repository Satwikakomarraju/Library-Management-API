from flask import Flask, jsonify, request, abort
from typing import Optional, Dict, List
from functools import wraps

app = Flask(__name__)

# Mock storage
book_records: List[Dict] = []
member_records: List[Dict] = []

# Mock token for authentication
TOKEN = "your_secure_token"

# Utility functions
def locate_book(book_id: int) -> Optional[Dict]:
    return next((record for record in book_records if record['id'] == book_id), None)

def locate_member(member_id: int) -> Optional[Dict]:
    return next((record for record in member_records if record['id'] == member_id), None)

# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {TOKEN}":
            abort(403, 'Unauthorized access.')
        return f(*args, **kwargs)
    return decorated

# CRUD for Books
@app.route('/books', methods=['GET'])
@token_required
def fetch_books():
    search_query = request.args.get('q', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page

    filtered_records = [
        record for record in book_records 
        if search_query.lower() in record['title'].lower() or search_query.lower() in record['author'].lower()
    ]
    return jsonify(filtered_records[start:end]), 200

@app.route('/books', methods=['POST'])
@token_required
def create_book():
    payload = request.get_json()
    if not payload or 'id' not in payload or 'title' not in payload or 'author' not in payload:
        abort(400, 'Invalid book data.')
    if locate_book(payload['id']):
        abort(400, 'Book with this ID already exists.')
    book_records.append(payload)
    return jsonify(payload), 201

@app.route('/books/<int:book_id>', methods=['GET'])
@token_required
def fetch_book(book_id: int):
    record = locate_book(book_id)
    if not record:
        abort(404, 'Book not found.')
    return jsonify(record), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
@token_required
def modify_book(book_id: int):
    record = locate_book(book_id)
    if not record:
        abort(404, 'Book not found.')
    payload = request.get_json()
    record.update(payload)
    return jsonify(record), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
@token_required
def remove_book(book_id: int):
    record = locate_book(book_id)
    if not record:
        abort(404, 'Book not found.')
    book_records.remove(record)
    return '', 204

# CRUD for Members
@app.route('/members', methods=['GET'])
@token_required
def fetch_members():
    return jsonify(member_records), 200

@app.route('/members', methods=['POST'])
@token_required
def create_member():
    payload = request.get_json()
    if not payload or 'id' not in payload or 'name' not in payload:
        abort(400, 'Invalid member data.')
    if locate_member(payload['id']):
        abort(400, 'Member with this ID already exists.')
    member_records.append(payload)
    return jsonify(payload), 201

@app.route('/members/<int:member_id>', methods=['GET'])
@token_required
def fetch_member(member_id: int):
    record = locate_member(member_id)
    if not record:
        abort(404, 'Member not found.')
    return jsonify(record), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
@token_required
def modify_member(member_id: int):
    record = locate_member(member_id)
    if not record:
        abort(404, 'Member not found.')
    payload = request.get_json()
    record.update(payload)
    return jsonify(record), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
@token_required
def remove_member(member_id: int):
    record = locate_member(member_id)
    if not record:
        abort(404, 'Member not found.')
    member_records.remove(record)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
