# Importing the sys module, which provides access to system-specific parameters and functions
import sys

# Implementation of maze solving

# Blueprint called Node.
# Special instruction that runs automatically whenerver you create a new 'Node'.
# Self refers to the specific Node you are creating.
# The state stores it inside the Node. If you given a state of "Position A," it saves "Position A" as this Node's state.
# The parent is likely the Node that came right before this one. It helps you trace your steps backward.
# This stores the action that was taken to get from the parent Node to this new Node. For example, the action might be "move left."
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Blueprint called Stack Frontier.
# This is the special setup instruction. It automatically runs the moment you create a new StackFrontier.
# "Give this new backpack (self) an empty list ([]) and name that list frontier."
# Every time you create a StackFrontier, it starts out with its own empty list inside, ready for you to add things to it.
class StackFrontier():
    def __init__(self):
        self.frontier = []