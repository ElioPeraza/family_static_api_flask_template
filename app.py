from flask import Flask, request, jsonify
from datastructure import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

@app.route('/')
def hello():
    return 'API SERVER IS UP!!'

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.json
    if not member_data or 'first_name' not in member_data or 'age' not in member_data or 'lucky_numbers' not in member_data:
        return jsonify({"error": "Invalid data"}), 400
    jackson_family.add_member(member_data)
    return jsonify(member_data), 201

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": True}), 200  # Eliminación exitosa
    else:
        return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
