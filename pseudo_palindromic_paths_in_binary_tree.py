from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def pseudo_palindromic_count(node=None, path=1, counts=None):
    if counts is None:
        counts = [0 for _ in range(10)]

    if not node:
        return 0

    if node.left or node.right:
        new_count = counts[:]
        new_count[node.val] ^= 1
        return (pseudo_palindromic_count(node.left, path + 1, new_count) +
                pseudo_palindromic_count(node.right, path + 1, new_count))

    else:
        new_count = counts[:]
        new_count[node.val] ^= 1
        return 0 if sum(new_count) > path % 2 else 1


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return pseudo_palindromic_count(root)
