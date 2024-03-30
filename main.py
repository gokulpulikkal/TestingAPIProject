from flask import Flask, request, jsonify

app = Flask(__name__)

data = {}

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def create_data():
    request_data = request.json
    # Assuming the request data contains 'key' and 'value' fields
    key = request_data.get('key')
    value = request_data.get('value')
    if key is not None and value is not None:
        data[key] = value
        return jsonify({'message': 'Data created successfully'}), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400
    
@app.route('/data/<key>', methods=['GET', 'PUT'])
def manage_data(key):
    if request.method == 'GET':
        return jsonify({key: data.get(key, 'Key not found')})
    elif request.method == 'PUT':
        request_data = request.json
        # Assuming the request data contains 'value' field for updating the value
        value = request_data.get('value')
        if value is not None:
            data[key] = value
            print("Creating the value in the data base  ", data)
            return jsonify({'message': 'Data updated successfully'}), 200
        else:
            return jsonify({'error': 'Invalid request data'}), 400


if __name__ == "__main__":
    app.run(debug=True)