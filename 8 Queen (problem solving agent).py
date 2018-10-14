
# coding: utf-8
#@author: Falguni Das Shuvo




class Problem:
    
    initial_state = [None, None, None, None, None, None, None, None]
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col = [0,1,2,3,4,5,6,7]
    
    def check_if_attacked(self, state):  # returns True if attacked
        try:
            index = state.index(None) - 1  
        except ValueError:
            index = 7

        if index == 0:
            return False

        for i in range(0,index):
            if (state[i][0] == state[index][0]) or (state[i][1] == state[index][1]):
                return True  #row and column attack check
            if abs(ord(state[i][0]) - ord(state[index][0])) == abs(int(state[i][1]) - int(state[index][1])): 
                return True #diagonal attack detect
        return False
    
    def actions(self, state):
        all_actions = []
        #find the first (leftmost) None position
        try:
            index = state.index(None)  # returns the first index on None or raises ValueError in None is not found
        except ValueError:
            return [state]
        for i in range(0,8):
            next_state = state[:]
            next_state[index] = Problem.row[index] + str(i)
            if not self.check_if_attacked(next_state):
                all_actions.append(next_state)
        return all_actions

    
    def result(self, state, action):
        return action

    
    
    def goal_test(self, state):
        try:
            state.index(None)
            return False
        except ValueError:
            return True
   
    def step_cost(self, par_state=None, action=None, child_state=None):
        return 0






class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost





def child_node(problem, parent, action):
    state = problem.result(parent.state, action)
    path_cost = parent.path_cost + problem.step_cost(parent.state, action)
    return Node(state, parent, action, path_cost)
    





def compare(node):
    return node.path_cost

class Frontier:
    def __init__(self):
        self.p_queue = []
    
    def is_empty(self):
        return len(self.p_queue) == 0
    
    def insert(self, node):
        self.p_queue.append(node)
        self.p_queue = sorted(self.p_queue, key=compare, reverse=True)
    
    def pop(self):
        return self.p_queue.pop()
    
    def contains_state(self, state):
        for node in self.p_queue[:]:
            if node.state == state:
                return True
        return False
    
    def replace_if_higher_path_cost_with_same_state(self,node):
        for i in range(len(self.p_queue)):
            if self.p_queue[i].state == node.state:
                if self.p_queue[i].path_cost > node.path_cost:
                    self.p_queue[i] = node
   





def uniform_cost_search(problem):
    node = Node(problem.initial_state.copy(),None, None, 0)
    frontier = Frontier()
    frontier.insert(node)
    explored = []
    n=1
    
    while True:
        if frontier.is_empty():
            return "failure"
        node = frontier.pop()
        #print("popped from frontier")
        if problem.goal_test(node.state):
            print (str(n) +" "+ str(node.state))
            paint(node.state)
            n = n+1
        explored.append(node.state)
        for action in problem.actions(node.state):
            #print(action)
            child = child_node(problem, node, action)
            if (child.state not in explored) and (not frontier.contains_state(child.state)):
                frontier.insert(child)
                #print('inserted in frontier')
            else:
                frontier.replace_if_higher_path_cost_with_same_state(child)





def paint(state):
    print("  _ _ _ _ _ _ _ _ ")
    for i in range(7,-1,-1):
        prnt_str = str(i)
        for j in range(0,8):
            prnt_str = prnt_str + "|"
            if int(state[j][1]) == i :
                prnt_str = prnt_str + "Q"
            else:
                prnt_str = prnt_str + " "
        prnt_str = prnt_str + "|"
        print(prnt_str)
    #print(" - - - - - - - - ")
    print("  a b c d e f g h ")
            





problem = Problem()

uniform_cost_search(problem)

