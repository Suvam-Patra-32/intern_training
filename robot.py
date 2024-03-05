def move_forward(x, y, direction):
    move = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    dx, dy = move[direction]
    return x + dx, y + dy, direction

def rotate_clockwise(direction):
    rotate = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    return rotate[direction]

if __name__ == "__main__":
    x = int(input("Enter initial X coordinate: "))
    y = int(input("Enter initial Y coordinate: "))
    direction = input("Enter initial direction (N, E, S, W): ")
    commands = input("Enter commands (e.g., FRFF): ")
   
    actions = {
        'F': move_forward,
        'R': lambda x, y, d: (x, y, rotate_clockwise(d))
    }