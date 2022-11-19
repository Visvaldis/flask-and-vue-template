from flask import render_template, jsonify, request
from app import service


from app import app,APP_ROOT

@app.route('/')
def home():
    return render_template('index.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')


@app.route('/post',  methods=['POST'])
def post_example():
    if request.method == 'POST':
        model = request.get_json()
        data = service.mock_function(model)
        print(data, '\n\n\n')
        return data
  
@app.route('/get/<id>',  methods=['GET'])
def get_example(id):
    if request.method == 'GET':
        print("Request with id: ", id, '\n\n\n')
        result = {
            'data': {
            },
            'payload': ["Test", "payload"]
        }
        result['data'] = id
        return jsonify(result)