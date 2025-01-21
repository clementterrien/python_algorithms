from typing import Any, Generator
from unittest import TestCase, main


class ListNode:

    min_val: int = -100
    max_val: int = 100

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, list):
            return super().__eq__(value)
        else:
            return list(self) == value

    def __iter__(self) -> Generator[int, Any, None]:
        current = self
        while current:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        return str(self.val)

    @property
    def val(self) -> int:
        return self._val

    @val.setter
    def val(self, val: int) -> int:
        if not isinstance(val, int):
            raise ValueError('val must be an integer.')
        if val > self.max_val:
            raise ValueError(f"val must be inferior to {self.max_val} included.")
        if val < self.min_val:
            raise ValueError(f"val must be superior to {self.min_val} included.")

        self._val = val

        return self._val

    def generate_list_node_from_int_list(self, nums: list[int]) -> "ListNode":
        """ Generates a linked list from a given list of integers, using the current `ListNode` as the head.

            Args:
                nums (list[int]): A list of integers to populate the linked list. The first integer
                                will be assigned to the current node (`self`), and subsequent integers
                                will form the rest of the linked list.

            Returns:
                ListNode: The head of the constructed linked list (i.e., the current node `self`).

            Example:
                If `nums = [1, 2, 3]` and the current `ListNode` is the head:

                Initial state:
                    self = ListNode(val=0)

                After calling `generate_list_node_from_int_list(nums)`:
                    self = ListNode(val=1) -> ListNode(val=2) -> ListNode(val=3)

            Notes:
                - The method modifies the `self` node and appends new nodes to it.
                - Assumes that `nums` is not empty. If `nums` is empty, it will raise an `IndexError`
                when trying to access `nums[0]`.
                - The resulting linked list will follow the order of integers in `nums`.

            Raises:
                ValueError: If given nums is empty or contains non integer elements.
        """
        if not isinstance(nums, list) or not all([isinstance(x, int) for x in nums]):
            raise ValueError("nums must be a list of integers.")
        if not nums:
            raise ValueError("nums can't be empty.")

        current = self
        self.val = nums[0]

        for num in nums[1:]:
            current.next = ListNode(val=num)
            current = current.next

        return self

    def to_integer(self, reverse: bool = True) -> int:
        """ Convert the linked list's node values into a single integer.

            This method traverses the linked list, collects the node values,
            and concatenates them to form an integer. The order of concatenation
            can be controlled using the `reverse` parameter.

            Args:
                reverse (bool): Determines the order of concatenation.
                                - If `True`, the node values are concatenated in reverse order.
                                - If `False`, the node values are concatenated in their original order.
                                Default is `True`.

            Returns:
                int: The integer formed by concatenating the node values.

            Raises:
                ValueError: If the linked list is empty.

            Example:
                Given a linked list: 1 -> 2 -> 3

                - `to_integer(reverse=True)` returns `321`
                - `to_integer(reverse=False)` returns `123`

            Notes:
                - This method assumes that all node values are single-digit integers.
                - Leading zeros in the linked list will be preserved in the resulting integer.
        """
        as_list = list(self)
        if reverse:
            as_list.reverse()
        return int(''.join(map(str, as_list)))


class TestListNode(TestCase):
    def setUp(self):
        """Set up a ListNode instance for testing."""
        self.node = ListNode()

    def test_val_setter_valid(self):
        """Test setting val within the allowed range."""
        self.node.val = 50
        self.assertEqual(self.node.val, 50)

    def test_val_setter_above_max(self):
        """Test setting val above the maximum allowed value."""
        with self.assertRaises(ValueError) as context:
            self.node.val = 150
        self.assertEqual(str(context.exception), "val must be inferior to 100 included.")

    def test_val_setter_below_min(self):
        """Test setting val below the minimum allowed value."""
        with self.assertRaises(ValueError) as context:
            self.node.val = -1000
        self.assertEqual(str(context.exception), "val must be superior to -100 included.")

    def test_val_setter_non_integer(self):
        """Test setting val to a non-integer value."""
        with self.assertRaises(ValueError) as context:
            self.node.val = "string"
        self.assertEqual(str(context.exception), "val must be an integer.")

    def test_generate_list_node_from_int_list_valid_input(self):
        """Test generating a linked list from a valid list of integers."""
        nums = [1, 2, 3]
        expected_values = [1, 2, 3]
        self.node.generate_list_node_from_int_list(nums)
        result = list(self.node)
        self.assertEqual(result, expected_values)

    def test_generate_list_node_from_int_list_empty_list(self):
        """Test generating a linked list from an empty list."""
        with self.assertRaises(ValueError) as context:
            self.node.generate_list_node_from_int_list([])
        self.assertEqual(str(context.exception), "nums can't be empty.")

    def test_generate_list_node_from_int_list_non_integer_elements(self):
        """Test generating a linked list from a list with non-integer elements."""
        nums = [1, 'two', 3]
        with self.assertRaises(ValueError) as context:
            self.node.generate_list_node_from_int_list(nums)
        self.assertEqual(str(context.exception), "nums must be a list of integers.")

    def test_generate_list_node_from_int_list_single_element(self):
        """Test generating a linked list from a list with a single integer."""
        nums = [42]
        expected_values = [42]
        self.node.generate_list_node_from_int_list(nums)
        result = list(self.node)
        self.assertEqual(result, expected_values)

    def test_to_integer_normal_order(self):
        """Test converting linked list to integer in normal order."""
        node = ListNode().generate_list_node_from_int_list([1, 2, 3])
        self.assertEqual(node.to_integer(reverse=False), 123)

    def test_to_integer_reverse_order(self):
        """Test converting linked list to integer in reverse order."""
        node = ListNode().generate_list_node_from_int_list([1, 2, 3])
        self.assertEqual(node.to_integer(reverse=True), 321)

    def test_to_integer_single_node(self):
        """Test converting a single-node linked list to integer."""
        node = ListNode().generate_list_node_from_int_list([5])
        self.assertEqual(node.to_integer(reverse=False), 5)
        self.assertEqual(node.to_integer(reverse=True), 5)

    def test_to_integer_with_leading_zeros(self):
        """Test converting linked list with leading zeros to integer."""
        node = ListNode().generate_list_node_from_int_list([0, 1, 2])
        self.assertEqual(node.to_integer(reverse=False), 12)
        self.assertEqual(node.to_integer(reverse=True), 210)


if __name__ == "__main__":
    main()
