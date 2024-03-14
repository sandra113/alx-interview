#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """This method determines if all the boxes can be opened"""
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
