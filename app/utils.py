
def is_valid(maze, x, y):
  return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

def heuristic(cur_boxes, cur_goals):
    h = 0
    for box in cur_boxes:
        h += min([abs(box[0] - goal[0]) + abs(box[1] - goal[1]) for goal in cur_goals])
    return h