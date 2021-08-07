from flask import Flask, render_template
app = Flask(__name__)

#For the 1st part of the Checkerboard assignment
@app.route('/')
def checkerboard1():
    board = generate_board(8, 8)
    return render_template('board.html', board = board)

# For the 2nd part of hte Checkerboard assignment
@app.route('/<int:height>')
def checkerboard2(height):
    board = generate_board(8, height)
    return render_template('board.html', board = board)

# For the 3rd part of the Checkerboard assignment
@app.route('/<int:width>/<int:height>')
def checkerboard3(width, height):
    board = generate_board(width, height)
    return render_template('board.html', board = board)


def generate_board(width, height):
    board = []
    for y in range(0, height):
        new_row = []
        for x in range(0, width):
            if (x + y) % 2 == 0:
                new_row.append(0)
            else:
                new_row.append(1)
        board.append(new_row)
    return board
if __name__ == "__main__":
    app.run(debug = True)