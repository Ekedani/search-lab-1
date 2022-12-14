# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    initial_state = problem.getStartState()
    visited_nodes = [initial_state]
    # Uncomment this for using matrix instead of list
    # visited_nodes = [[False] * (problem.walls.width - 1) for i in range(problem.walls.height - 1)]
    # visited_nodes[initial_state[1]][initial_state[0]] = True
    search_queue = Queue()

    search_queue.push((initial_state, []))
    while not search_queue.isEmpty():
        current_node, current_path = search_queue.pop()

        if problem.isGoalState(current_node):
            return current_path

        successors = problem.getSuccessors(current_node)
        for node in successors:
            # Uncomment this for using matrix instead of list
            # if not visited_nodes[node[0][1]][node[0][0]]:
            if node[0] not in visited_nodes:
                search_queue.push((node[0], current_path + [node[1]]))
                visited_nodes.append(node[0])
                # Uncomment this for using matrix instead of list
                # visited_nodes[node[0][1]][node[0][0]] = True

    # Valid path was not found
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueueWithFunction

    # Too unwieldy to be lambda, sadly
    def priority_function(node):
        return heuristic(node[0], problem) + problem.getCostOfActions(node[1])

    initial_state = problem.getStartState()
    closed_nodes = set()
    open_queue = PriorityQueueWithFunction(priority_function)

    open_queue.push((initial_state, []))
    while not open_queue.isEmpty():
        current_node, current_path = open_queue.pop()

        if current_node in closed_nodes:
            continue

        if problem.isGoalState(current_node):
            return current_path

        closed_nodes.add(current_node)
        successors = problem.getSuccessors(current_node)
        for node in successors:
            if node[0] not in closed_nodes:
                open_queue.push((node[0], current_path + [node[1]]))

    # Valid path was not found
    return []


def greedyAStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    from util import PriorityQueueWithFunction

    initial_state = problem.getStartState()
    closed_nodes = set()
    # We just ignore cost of actions to make it greedy
    open_queue = PriorityQueueWithFunction(lambda node: heuristic(node[0], problem))

    open_queue.push((initial_state, []))
    while not open_queue.isEmpty():
        current_node, current_path = open_queue.pop()

        if current_node in closed_nodes:
            continue

        if problem.isGoalState(current_node):
            return current_path

        closed_nodes.add(current_node)
        successors = problem.getSuccessors(current_node)
        for node in successors:
            if node[0] not in closed_nodes:
                open_queue.push((node[0], current_path + [node[1]]))

    # Valid path was not found
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
greedy_astar = greedyAStarSearch
