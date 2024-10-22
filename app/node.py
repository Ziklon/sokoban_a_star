
from .constants import MOVEMENTS, MOVEMENT_NAMES
from .utils import is_valid

class Node:
    def __init__(self,\
                 player_pos,\
                 boxes, path=[],\
                 heuristic=0):
        self.player_pos = player_pos
        self.boxes = boxes
        self.path = path
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __hash__(self):
        return hash(self.identifier())
    
    def identifier(self):
        return (self.player_pos, tuple(self.boxes))

    def __eq__(self, other):
        return self.player_pos == other.player_pos and\
              self.boxes == other.boxes

    def __is_valid(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

    def __repr__(self):
      return f"player_pos:{self.player_pos}, boxes:{self.boxes}, last_direction: {self.last_direction}, steps: {self.steps}, heuristic: {self.heuristic}"
    

