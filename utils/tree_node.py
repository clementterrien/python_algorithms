# This is a problem given by Leetcode.com
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/

from typing import Any, Optional, Sequence
from unittest import TestCase, main


class TreeNode:
    """ This represents a Binary Tree Node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def create_tree(self, root: Sequence[Optional[int]]) -> "TreeNode":
        """ Create a binary tree from a list representing level-order traversal.
        """
        if not isinstance(root[0], int):
            raise ValueError('The first value of the sequence must be an int to buidl the binary')
        if not root:
            return self

        root_node = self
        root_node.val = root[0]

        queue = [root_node]
        index = 1

        while queue and index < len(root):
            node = queue.pop(0)

            # Set the left child
            if index < len(root) and root[index] is not None:
                left_val = root[index]
                assert isinstance(left_val, int)
                node.left = TreeNode(val=left_val)
                queue.append(node.left)

            index += 1

            # Set the right child
            if index < len(root) and root[index] is not None:
                right_val = root[index]
                assert isinstance(right_val, int)
                node.right = TreeNode(val=right_val)
                queue.append(node.right)

            index += 1

        return root_node

    def __iter__(self):
        """ In-order traversal of the binary tree.
            Yields:
                int: The next value in the in-order traversal of the tree.
        """
        if self.left:
            yield from iter(self.left)
        yield self.val
        if self.right:
            yield from iter(self.right)

    def __eq__(self, other: Any):
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val


class TestTreeNode(TestCase):

    def setUp(self) -> None:
        self.root_node = TreeNode()

    def check_node(self, node: Any, val: int, left: bool, right: bool) -> TreeNode:
        assert isinstance(node, TreeNode)
        self.assertEqual(node.val, val)

        if left:
            self.assertIsInstance(node.left, TreeNode)
        else:
            self.assertIsNone(node.left)

        if right:
            self.assertIsInstance(node.right, TreeNode)
        else:
            self.assertIsNone(node.right)

        return node

    def test_create_tree_case_1(self) -> None:
        root: list[Optional[int]] = [1, 2, 3, None, 4]
        tree: TreeNode = self.root_node.create_tree(root)

        # root (1)
        tree = self.check_node(tree, 1, True, True)
        # left (2)
        left_child = self.check_node(tree.left, 2, False, True)
        # right (3)
        _ = self.check_node(tree.right, 3, False, False)
        # left_right
        _ = self.check_node(left_child.right, 4, False, False)

    def test_create_tree_case_2(self) -> None:
        root: list[int] = [1, 2, 3, 4, 5, 6, 7]
        tree = self.root_node.create_tree(root)

        # root (1)
        tree = self.check_node(tree, 1, True, True)
        # root left (2)
        tree_left = self.check_node(tree.left, 2, True, True)
        # tree right (3)
        tree_right = self.check_node(tree.right, 3, True, True)
        # root left left (4)
        _ = self.check_node(tree_left.left, 4, False, False)
        # root left right (5)
        _ = self.check_node(tree_left.right, 5, False, False)
        # root right left (6)
        _ = self.check_node(tree_right.left, 6, False, False)
        # root right right (7)
        _ = self.check_node(tree_right.right, 7, False, False)


if __name__ == "__main__":
    main()
