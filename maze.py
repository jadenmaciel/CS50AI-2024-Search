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
# This function creates a frontier that is going to represent using a list. Which is an empty list, there's nothing in my frontier to begin with. 
class StackFrontier():
    def __init__(self):
        self.frontier = []


# def add(self, node): Creates a new action (a function) called 'add'.
# self.frontier.append(node) This is the instruction for the add action. 
# self.frontier: Go find the list named frontier that belongs to me (self).
# .append(node): This is a command for lists. It simply means, "add the item (node) to the very end of the list.
# I have an add function that adds something to the frontier
# As by appending it to the end of the list. 

    def add(self, node):
        self.frontier.append(node)


# This code gives your StackFrontier another new skill: the ability to check if it's already holding an item with a specific state.
# def contains_state(self, state): This line creates the new action named contains_state. 
# To use this skill, you have to tell it what state you are looking for (e.g., you're looking for a state called "river").
# for node in self.frontier: It quickly peeks at every single item (node) inside its frontier list, one by one.
# node.state == state: For each item, it checks if that item's stored state is the same as the state you're asking about. This check gives a True or False answer for each item.
# any(...): This part looks at all the True/False answers. If it finds even one True answer, it immediately stops and shouts "Yes!" (or returns True). 
# If it checks all the items and only finds False answers, it shouts "Nope!" (or returns False).
# In short, this function lets you ask your StackFrontier if it contains an item with a certain state, and it gives you a simple True or False answer.
# I have a function that checks if the frontier contrains a particular state.

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

# I have an empty function that checks if the frontier is empty. If the frontier is empty, that just means the lenght of the frontier is zero. 

    def empty(self):
        return len(self.frontier) == 0

# I have a function for removing something from the frontier. I can't remove somethiing from the frontier if the frontier is empty. 

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")