#def greet():
#    print('Hello World!')

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Replace this with the actual data you want to return
    data = {'message': 'Hello, this is your API response!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

