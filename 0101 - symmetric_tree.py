# This is a problem given by Leetcode.com
# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional
from unittest import TestCase, main

from utils.tree_node import TreeNode


class Solution:

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        """ Check whether a binary tree is symmetric around its center.

            A binary tree is symmetric if the left and right subtrees are mirror images
            of each other. This method uses a recursive helper function to compare
            corresponding nodes in the left and right subtrees.

            Args:
                root (Optional[TreeNode]): The root node of the binary tree.

            Returns:
                bool: True if the tree is symmetric, False otherwise.
        """
        def is_mirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif (left is None) != (right is None):
                return False
            if right != left:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_is_symmetric_valid_case(self) -> None:
        case_1 = TreeNode().create_tree([1, 2, 2, 3, 4, 4, 3])
        self.assertTrue(self.solution.is_symmetric(case_1))

    def test_is_not_symmetric_due_to_structure(self) -> None:
        case_2 = TreeNode().create_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.solution.is_symmetric(case_2))

    def test_is_not_symmetric_due_to_values(self) -> None:
        case_3 = TreeNode().create_tree([1, 2, 2, 3, 4, 3, 4])
        self.assertFalse(self.solution.is_symmetric(case_3))

    def test_is_symmetric_empty_tree(self) -> None:
        case_4 = None
        self.assertTrue(self.solution.is_symmetric(case_4))

    def test_is_symmetric_single_node(self) -> None:
        case_5 = TreeNode().create_tree([1])
        self.assertTrue(self.solution.is_symmetric(case_5))

    def test_is_not_symmetric_three_levels(self) -> None:
        case_6 = TreeNode().create_tree([1, 2, 2, None, 3, None, 3])
        self.assertFalse(self.solution.is_symmetric(case_6))

    def test_is_symmetric_even_nodes(self) -> None:
        case_7 = TreeNode().create_tree([1, 2, 2, None, 3, 3, None])
        self.assertTrue(self.solution.is_symmetric(case_7))


if __name__ == "__main__":
    main()
