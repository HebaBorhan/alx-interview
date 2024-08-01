#!/usr/bin/python3
"""Unlock boxes"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])
    queue = list(boxes[0])

    while queue:
        key = queue.pop()
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            for new_key in boxes[key]:
                if new_key not in keys:
                    keys.add(new_key)
                    queue.append(new_key)

    return len(opened_boxes) == n
