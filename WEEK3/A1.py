
moves = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}

class Node:
  def __init__(self,state,parent=None,action=None,g=0,h=0,f=0):
    self.state=state
    self.parent=parent
    self.action=action
    self.g=g
    self.h=h
    self.f=f

  def __lt__(self,other):
    return self.f<other.f

  def heuristic(self):
    self.h = 0
    for i in range(9):
      if self.state[i] == 0:
        continue
      elif self.state[i] != goal[i]:
        self.h += 1
    self.f = self.g + self.h
    return self.f

  def get_neighbors(self):
    neighbours = []
    blank = self.state.index(0)

    for action,(dr,dc) in moves.items():
      nr,nc = blank//3 + dr,blank %3 + dc
      if 0<=nr<3 and 0<=nc<3:
        new_state = self.state[:]
        new_state[blank],new_state[nr*3+nc] = new_state[nr*3+nc],new_state[blank]
        neighbours.append(Node(new_state,self,action,self.g+1))

    for node in neighbours:
      node.heuristic()
    return neighbours

def display(state):
  for i in range(3):
    print(state[i*3:i*3+3])
  print()
def a_star_search(start_state, goal_state):
    global goal
    goal = goal_state
    
    start_node = Node(start_state, g=0)
    start_node.heuristic()
    
    
    open_list = [start_node]
    closed_list = set()
    
    while open_list:
        # Find the node with the lowest f value manually
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        
        state_tuple = tuple(current_node.state)
        
        if current_node.state == goal:
            path = []
            curr = current_node
            while curr.parent:
                path.append((curr.action, curr.state))
                curr = curr.parent
            path.reverse()
            return path, current_node.g
            
        closed_list.add(state_tuple)
        
        for neighbor in current_node.get_neighbors():
            neighbor_tuple = tuple(neighbor.state)
            if neighbor_tuple in closed_list:
                continue
                
        
            better_already_exists = False
            for node in open_list:
                if node.state == neighbor.state and node.f <= neighbor.f:
                    better_already_exists = True
                    break
            
            if not better_already_exists:
                open_list.append(neighbor)
                
    return path, -1

start = [1, 2, 3, 0, 4, 6, 7, 5, 8]
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
path, cost = a_star_search(start, target)
print(f"Goal reached in {cost} moves!")
for action, state in path:
    print(f"Move {action}:")
    display(state)