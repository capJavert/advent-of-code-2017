p = [0, 0]
q = [0, 0]
x_span = 0
y_span = 0
target_square = 368078
current_square = 1
squares = {"00": 1}


def calculate_square_value(square):
    value = 0

    if str(square[0])+str(square[1]+1) in squares:
        value += squares[str(square[0])+str(square[1]+1)]

    if str(square[0]+1)+str(square[1]+1) in squares:
        value += squares[str(square[0]+1)+str(square[1]+1)]

    if str(square[0]+1)+str(square[1]) in squares:
        value += squares[str(square[0]+1)+str(square[1])]

    if str(square[0]+1)+str(square[1]-1) in squares:
        value += squares[str(square[0]+1)+str(square[1]-1)]

    if str(square[0])+str(square[1]-1) in squares:
        value += squares[str(square[0])+str(square[1]-1)]

    if str(square[0]-1)+str(square[1]-1) in squares:
        value += squares[str(square[0]-1)+str(square[1]-1)]

    if str(square[0]-1)+str(square[1]) in squares:
        value += squares[str(square[0]-1)+str(square[1])]

    if str(square[0]-1)+str(square[1]+1) in squares:
        value += squares[str(square[0]-1)+str(square[1]+1)]

    return value


def right():
    global squares
    global x_span
    global current_square
    x_span += 1

    for i in range(0, x_span):
        current_square += 1
        q[0] += 1

        squares[str(q[0])+str(q[1])] = calculate_square_value(q)

        if current_square == target_square:
            print("STEPS: ", abs(p[0] - q[0]) + abs(p[1] - q[1]))


def up():
    global squares
    global y_span
    global current_square
    y_span += 1

    for i in range(0, y_span):
        current_square += 1
        q[1] += 1

        squares[str(q[0])+str(q[1])] = calculate_square_value(q)

        if current_square == target_square:
            print("STEPS: ", abs(p[0] - q[0]) + abs(p[1] - q[1]))


def left():
    global squares
    global x_span
    global current_square
    x_span += 1

    for i in range(0, x_span):
        current_square += 1
        q[0] -= 1

        squares[str(q[0])+str(q[1])] = calculate_square_value(q)

        if current_square == target_square:
            print("STEPS: ", abs(p[0] - q[0]) + abs(p[1] - q[1]))


def down():
    global squares
    global y_span
    global current_square
    y_span += 1

    for i in range(0, y_span):
        current_square += 1
        q[1] -= 1

        squares[str(q[0])+str(q[1])] = calculate_square_value(q)

        if current_square == target_square:
            print("STEPS: ", abs(p[0] - q[0]) + abs(p[1] - q[1]))


def main():
    directions = (
        "RIGHT",
        "UP",
        "LEFT",
        "DOWN",
    )
    direction_actions = {
        "RIGHT": right,
        "UP": up,
        "LEFT": left,
        "DOWN": down
    }
    direction_index = 0

    while current_square < target_square:
        direction_actions[directions[direction_index]]()
        direction_index = (direction_index + 1) % 4

    for key, value in squares.items():
        if value > target_square:
            print("VALUE:", value)
            break


main()
