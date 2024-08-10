# Sudoku Solver in Flask using Backtracking.

---

## Installation.

>1. Clone this repository to your computer.

```git
git clone https://github.com/Gozfrth/Sudoku.git
```

>2. Move into the project folder.

```
cd Sudoku-Solver-in-Flask/
```

>3. Create virtual environment.

```
python -m venv env
```

>4. Activate the virtual environment.

On Ubuntu
```
source env/Scripts/activate
```

On Windows
```
env\Scripts\activate.bat
```

>5. Install requirements.

```
pip install -r requirements.txt
```

>6. Run the Flask app.

```
flask run
```

>7. Now open your web browser and go to http://localhost:5000/ to view the app.

---


## Description.

>## What is Backtracking?

**Backtracking** is an algorithm that uses a form of depth-first search to incrementally build a solution to a problem. At each step of the search, the algorithm generates a single successor to the current state, rather than all possible successors. If the successor leads to a solution, the algorithm terminates successfully. If the successor leads to a dead end or failure, the algorithm backtracks to the previous state and tries a different path. This process continues until a solution is found or all possible paths have been explored. Backtracking is commonly used to solve problems that involve making a sequence of decisions, such as finding a path in a maze or solving a Sudoku puzzle. Backtracking makes use of Recursion, as it allows the algorithm to store the state at each instance and can easily backtrack when necessary.

> ### How this code uses Backtracking.

In the Flask app here, I employed a module `mymod.py`. The grid to be solved can be passed as an argument to this module, which returns the solution grid.

```python
def solve(grid):
    temp = find_zero(grid)
    if not temp:
        print('done')
        return True
    else:
        row, col = temp
    for n in range(1, 10):
        if is_legal(grid, row, col, n):
            grid[row][col] = n
            if solve(grid):
                return True
            grid[row][col] = 0
    return False
 ```

`find_zero()` is a function that checks for an empty position on the grid. It either returns a tuple containing the row and column of the empty cell or Null, stored in a temporary variable `temp`. If there are no empty cells, it naturally means that the problem has been solved and returns success. Now if there is an empty cell, the variables `row` and `grid` store the position of the empty cell on the board. 
Using a for loop iterating from 1 to 9, we check if the number present in the position (row,column) in the grid is legal using the `is_legal()` function.
Now, we call the `solve()` function recursively by passing the new grid as an argument to it. It returns `True` if there are no empty cells on the grid and returns `False` if there are no numbers from 1 to 9 that can be legally placed in the empty cell.
If the function returns False, it resets the current cell to 0 and then backtrack to the previous state of the grid and checks for other numbers that satisfy the conditions.
This is how the program uses backtracking to solve a Sudoku grid.

>## Making the App.

>![empty grid](https://github.com/Gozfrth/Sudoku/blob/main/images/empty_grid.png)

>>This is what the App looks like (running on Chrome). This format is achieved using the html `<table>` tags. We use nested tables to divide the grid into nine 3x3 grids only for ease in reading and inputting the numbers.

```html
<table class="box">
    <tr>
        <td><input type="text" class ="b1" id="00"></td>
        <td><input type="text" class ="b1" id="01"></td>
        <td><input type="text" class ="b1" id="02"></td>
    </tr>
    <tr>
        <td><input type="text" class ="b1" id="10"></td>
        <td><input type="text" class ="b1" id="11"></td>
        <td><input type="text" class ="b1" id="12"></td>
    </tr>
    <tr>
        <td><input type="text" class ="b1" id="20"></td>
        <td><input type="text" class ="b1" id="21"></td>
        <td><input type="text" class ="b1" id="22"></td>
    </tr>
</table>
```

This code snippet represents just one box (3x3 table). We use `input` tags to input elements into a cell and each input cell has an id attribute where each id name corresponds to the cells position in the 9x9 grid (row,column). This is done so that we can assign the respective values into a two-dimensional array that represents the grid, in Javascript.

```Javascript
for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            temp = i +''+j;
            grid[i][j] = parseInt(document.getElementById(temp).value);
            index++;
        }
    }
```

`temp` is a javascript variable storing the row-column combination that is passed in the `getElementById()` function.

>![problem grid](https://github.com/Gozfrth/Sudoku/blob/main/images/problem_grid.png)

>>After entering the numbers into each cell, all we need to do is click the `Submit` button. The problem I used here was picked off of https://sudoku.com/evil/.

```Javascript

$.ajax({
        url:"http://localhost:5000/test",
        type:"POST",
        contentType: "application/json",
        data: s,
        success: function(response)
```

This is a jQuery AJAX request which sends a POST request to the URL *http://localhost:5000/test* along with JSON data `s`. The `success` function is executed when the response is successfully received from the server. 

```python
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
```

In `app.py`, The route `'/'` returns the HTML file `index.html` in the `static` folder using the render_template function from Flask. The POST request is a route `'/test'` that accepts a JSON object from the Javascript AJAX request. The `mymod.sol()` function is called to solve the puzzle, and the solution is returned as a JSON response to Javascript using the jsonify function from Flask.

Now all thats left to do is to show the solved grid in the App. This can be done by using a for loop and iterating through all rows and columns.
```Javascript
document.getElementById(temp).value = solution[i][j];
```
where `solution` is the 9x9 solution grid.

>![solved grid](https://github.com/Gozfrth/Sudoku/blob/main/images/solved_grid.png)
>> The solved Sudoku grid appears quickly because we have implemented Backtracking.


>### Side-notes.
>This was my first personal project and I'm satisfied with how it's come out. There are still countless ways I could improve this code (reducing the size of the html code as it is very repetitive at the moment is the most obvious one to me). This was also the first time I used Flask, and I followed quite a few tutorials on youtube, some of which are:
>[this](https://www.youtube.com/watch?v=6plVs_ytIH8&ab_channel=PythonSimplified),
>[this](https://www.youtube.com/watch?v=Ax_xwLybUME&ab_channel=DataAnalyticsIreland) and
>[this](https://www.youtube.com/watch?v=eqUwSA0xI-s&ab_channel=TechWithTim).
># END.
