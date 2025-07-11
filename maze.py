import sys

# Implementation of maze solving

# Class Node which keeps track of the state, the parent, and the action
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Class Stack Frontier
class StackFrontier():
    def __init__(self):
        self.frontier = []