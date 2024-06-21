from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, depth, parent):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.depth = depth
        self.parent = parent

    def is_valid(self):
        if 0 <= self.missionaries <= 3 and 0 <= self.cannibals <= 3:
            if (self.missionaries == 0 or self.missionaries >= self.cannibals):
                if (self.missionaries == 3 or self.missionaries <= self.cannibals):
                    return True
        return False

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return (self.missionaries == other.missionaries and
                self.cannibals == other.cannibals and
                self.boat == other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __repr__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"

def get_successors(state):
    successors = []
    if state.boat == 1:
        new_states = [
            State(state.missionaries - 2, state.cannibals, 0, state.depth + 1, state),
            State(state.missionaries - 1, state.cannibals, 0, state.depth + 1, state),
            State(state.missionaries, state.cannibals - 2, 0, state.depth + 1, state),
            State(state.missionaries, state.cannibals - 1, 0, state.depth + 1, state),
            State(state.missionaries - 1, state.cannibals - 1, 0, state.depth + 1, state)
        ]
    else:
        new_states = [
            State(state.missionaries + 2, state.cannibals, 1, state.depth + 1, state),
            State(state.missionaries + 1, state.cannibals, 1, state.depth + 1, state),
            State(state.missionaries, state.cannibals + 2, 1, state.depth + 1, state),
            State(state.missionaries, state.cannibals + 1, 1, state.depth + 1, state),
            State(state.missionaries + 1, state.cannibals + 1, 1, state.depth + 1, state)
        ]
    for new_state in new_states:
        if new_state.is_valid():
            successors.append(new_state)
    return successors

def bfs(start_state):
    frontier = deque([start_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            return state
        explored.add(state)
        for successor in get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
    return None

def print_solution(solution):
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    for step in path:
        print(step)

initial_state = State(3, 3, 1, 0, None)
solution = bfs(initial_state)
if solution:
    print("Solution found:")
    print_solution(solution)
else:
    print("No solution exists.")
