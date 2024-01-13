from colorama import Fore, Style
import random

# print("Enter size on maze")
# n = int(input())

# start = (Fore.GREEN + "S" + Style.RESET_ALL)
# wall = (Fore.RED + "▓" + Style.RESET_ALL)
# open = (Fore.BLUE + "◌" + Style.RESET_ALL)
# path = (Fore.GREEN + "◍" + Style.RESET_ALL)
# end = (Fore.GREEN + "E" + Style.RESET_ALL)
# percent = (n * n) * (1 / 4)
# percent = int(percent)

# maze = []


def mazes(maze, n):
    for i in range(n):
        r = []
        for j in range(n):
            r.append(open)
        maze.append(r)
    for _ in range(percent):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        maze[i][j] = wall
    maze[0][0] = start
    maze[n - 1][n - 1] = end


def find_path(maze):
    queue = [((0, 0), [])]
    visited = set()

    while queue:
        (x, y), path = queue.pop(0)
        if maze[x][y] == end:
            return True, path + [(x, y)]  # Return the path if the end is reached
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] != wall and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(x, y)]))
                visited.add((nx, ny))

    return False, []


def mark_path(maze, paths):
    for x, y in paths:
        maze[x][y] = path
    maze[0][0] = start
    maze[n-1][n-1] = end


def display_maze(maze, n):
    for i in range(n):
        for j in range(n):
            print(maze[i][j], end=" | ")
        print()


# mazes(maze, n)
# found, paths = find_path(maze)
# if found:
#     mark_path(maze, paths)
# print(found)

# display_maze(maze, n)

n = int(input("Enter the size of the maze (n x n): "))
start = (Fore.GREEN + "S" + Style.RESET_ALL)
wall = (Fore.RED + "▓" + Style.RESET_ALL)
open = (Fore.BLUE + "◌" + Style.RESET_ALL)
path = (Fore.GREEN + "◍" + Style.RESET_ALL)
end = (Fore.GREEN + "E" + Style.RESET_ALL)
percent = (n * n) * (1 / 4)
percent = int(percent)

maze = []

print("Generated Maze:")
print()
mazes(maze, n)
display_maze(maze, n)
print()       
while True:
    print("1. Print the path")
    print("2. Generate another puzzle")
    print("3. Exit the Game")

    choose = int(input("Enter you choice 1/2/3: "))
    print()
    if choose==1:
        found, paths = find_path(maze)
        if found:
            mark_path(maze, paths)
            print("Maze with Path:")
            print("Path found: ")
            print()
            display_maze(maze, n)
        else:
            print("Path not found!")
        print()

    if choose==2:
        n = int(input("Enter the size of the maze (n x n): "))
        start = (Fore.GREEN + "S" + Style.RESET_ALL)
        wall = (Fore.RED + "▓" + Style.RESET_ALL)
        open = (Fore.BLUE + "◌" + Style.RESET_ALL)
        path = (Fore.GREEN + "◍" + Style.RESET_ALL)
        end = (Fore.GREEN + "E" + Style.RESET_ALL)
        percent = (n * n) * (1 / 4)
        percent = int(percent)
        maze = []
        print("Generated Maze:")
        print()
        mazes(maze, n)
        display_maze(maze, n)
        print()


    if choose==3:
        break




