goal = (1,2,3,4,5,6,7,8,0)
state = (0,7,1,3,8,5,6,4,2)

# function to create a new tuple represent new puzzle state
def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return tuple(state)

# function to find move of current puzzle state and return list
def move(state):
    neighbors = []
    i = state.index(0)
    if i not in [0, 1, 2]:  # Up
        neighbors.append(swap(state, i, i - 3))
    if i not in [6, 7, 8]:  # Down
        neighbors.append(swap(state, i, i + 3))
    if i not in [0, 3, 6]:  # Left
        neighbors.append(swap(state, i, i - 1))
    if i not in [2, 5, 8]:  # Right
        neighbors.append(swap(state, i, i + 1))
    return neighbors

# using the breath first search technique
def bfs(init_state, goal):
    queue = [[init_state]]
    close = set()
    while queue:
        path = queue.pop(0) 
        node = path[-1]
        if node == goal:
            output(path)
            return path

        for neighbor in move(node): 
            if neighbor not in close:
                new_path = list(path) 
                new_path.append(neighbor) 
                queue.append(new_path)
                close.add(node)

    print("No solution found")
    return None


# function that print the output
def output(path:list):
    print(f"Total Steps: {len(path) - 1}")
    for e,i in enumerate(path):
        print(f"{e}. Step:") if e > 0 else print(f"Starting point: ")
        print(f"[{i[0]} {i[1]} {i[2]}]\n[{i[3]} {i[4]} {i[5]}]\n[{i[6]} {i[7]} {i[8]}]")
        if e == len(path) -1:
            print("Finish!")
            
bfs(state, goal)