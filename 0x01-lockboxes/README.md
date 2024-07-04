# Lockboxes Project

## Description
This project involves solving the problem of determining if all boxes in a list of locked boxes can be opened. Each box contains keys to other boxes. The goal is to write a Python method that determines if all the boxes can be unlocked.

## Concepts and Resources
To efficiently tackle this problem, it's essential to have a solid understanding of several key concepts:

### Lists and List Manipulation
- Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

### Graph Theory Basics
- Although not explicitly required, knowledge of graph theory (especially traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful, as the boxes and keys can be thought of as nodes and edges in a graph.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/linear-algebra/alternate-bases/graph-theory/v/graph-intro)

### Algorithmic Complexity
- Understanding the time and space complexity of your solution is important for writing more efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

### Recursion
- Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

### Queue and Stack
- Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-in-python/)

### Set Operations
- Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

## Task
### 0. Lockboxes
Write a method that determines if all the boxes can be opened.

#### Prototype
```python
def canUnlockAll(boxes)
