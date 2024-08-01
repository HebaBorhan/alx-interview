#!/usr/bin/python3
"""Unlock boxes"""


def canUnlockAll(boxes):
    """Unlock boxes"""
    n = len(boxes)
    opened_boxes = set()
    keys = set()
    queue = [0]
    
    while queue:
        box_index = queue.pop()
        if box_index not in opened_boxes:
            opened_boxes.add(box_index)
            for key in boxes[box_index]:
                if key not in keys:
                    queue.append(key)
                keys.add(key)
    
    return len(opened_boxes) == n
