from node import Node
import heapq
from .constants import MOVEMENTS, MOVEMENT_NAMES
from .utils import is_valid, heuristic

class Sokoban:
    def __init__(self, maze):
        self.maze = maze
        self.boxes = tuple(self.__find_positions('$'))
        self.goals = tuple(self.__find_positions('.'))
        self.player_pos = self.__find_positions('@')
        self.player_pos = self.player_pos[0] if self.player_pos else None
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.stats = {}

    def __find_positions(self, symbol):
      positions = []
      for r in range(self.rows):
          for c in range(self.cols):
              if self.maze[r][c] == symbol:
                positions.append((r, c))

      return sorted(positions)

    def __register_counters(self, metric_name):
       self.stats[metric_name] = self.stats.get(metric_name, 0) + 1
    
    def successors(self, node):
      for x, y in MOVEMENTS:
        new_x = node.player_pos[0] + x
        new_y = node.player_pos[1] + y
        if not is_valid(self.maze, new_x, new_y):
           continue

        new_boxes = list(self.boxes[:]) 

        if (new_x, new_y) in new_boxes:
            new_box_pos = (new_x + x , new_y + y)
            if not is_valid(self.maze, new_box_pos[0], new_box_pos[1]) or new_box_pos in new_boxes:
               continue
            new_boxes.remove((new_x, new_y))
            new_boxes.append(new_box_pos)
    
        new_boxes = tuple(sorted(new_boxes))
        new_path = self.path[:] + [((new_x, new_y), new_boxes)]
        new_heuristic = heuristic(new_boxes, self.goals)
        yield Node((new_x, new_y), new_boxes, new_path, new_heuristic)

    def execute(self):
      
      open_list = []
      heapq.heappush(open_list, Node(self.player_pos, self.boxes))
      closed_set = set()

      while open_list:
          self.__register_counters('total_node_size')
          cur_node = heapq.heappop(open_list)

          state = (cur_node.player_pos, tuple(cur_node.boxes))
          if state in closed_set:
              continue
          closed_set.add(state)

          # Verificamos si todas las cajas están en los objetivos
          if all(box in self.goals for box in cur_node.boxes):
              return cur_node.path  # Solución encontrada
          
          for child in self.successors(cur_node):
              new_state = (child.player_pos, tuple(child.boxes))
              if new_state not in closed_set:
                heapq.heappush(open_list, child)

      return None  # No se encontró solución