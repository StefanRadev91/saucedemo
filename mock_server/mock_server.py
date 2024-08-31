from flask import Flask, request, jsonify

app = Flask(__name__)

people = {}

@app.route('/people', methods=['POST'])
def add_person():
    data = request.json
    person_id = data.get('id')
    people[person_id] = data
    return jsonify({
        "message": "Person added successfully",
        "person": data
    }), 201

@app.route('/people/<person_id>', methods=['GET'])
def get_person(person_id):
    person = people.get(person_id)
    if person:
        return jsonify(person), 200
    else:
        return jsonify({"message": "Person not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)