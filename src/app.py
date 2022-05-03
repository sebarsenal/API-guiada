from flask import Flask, jsonify, request
app = Flask(__name__)
todos = [{"label": "Comprar fruta", "done": False},
         {"label": "Comprar arroz", "done": False}]


@app.route('/todos', methods=['GET'])
def hello_world():
    #return '<h1>Lista</h1>'
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
