from flask import Flask, request, jsonify, render_template
import mymod
from flask_cors import CORS


app = Flask(__name__, static_url_path='/static')
CORS(app)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/test', methods=['POST'])
def test():

    data = request.get_json()  # Get the JSON data from the POST request
    grid = data

    # Solve the Sudoku puzzle
    solution_grid = mymod.sol(grid)
    
    response = jsonify(solution=solution_grid)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')

    return response


if __name__ == '__main__':
    app.run(debug=True)
