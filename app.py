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

    return jsonify(solution=solution_grid)


if __name__ == '__main__':
    app.run(debug=True)
