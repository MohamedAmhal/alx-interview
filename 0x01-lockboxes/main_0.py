#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1, 2, 3, 4], [], [], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[1], [2], [3], [4], [5], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 2, 3], [4, 5], [6], [7], [], [], [], [8], [9]]
print(canUnlockAll(boxes))  # True

boxes = [[], [1], [2], [3], [4]]
print(canUnlockAll(boxes))  # False

boxes = [[1], [], [0], [2], [3]]
print(canUnlockAll(boxes))  # False


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 2, 3, 4], [], [], [], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 2, 3], [], [], [], [5]]
print(canUnlockAll(boxes))  # False

boxes = [[]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # True


