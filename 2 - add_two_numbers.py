# This is a problem given by Leetcode.com
# https://leetcode.com/problems/add-two-numbers/description/

from typing import Generator, Sequence
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self) -> Generator[int, None, list]:
        current = self

        while current:
            yield current.val
            current = current.next

    def __eq__(self, value: object) -> bool:
        """ For testing purpose, allows to compare the ListNode to a list.
        """
        if not isinstance(value, list):
            return super().__eq__(value)
        else:
            return list(self) == value

    def __int__(self) -> int:
        return int(''.join(map(str, list(self))))

    def __repr__(self) -> str:
        return str(list(self))

    @property
    def val(self) -> int:
        return self._val

    @val.setter
    def val(self, value: int) -> int:
        if not 0 <= value <= 9:
            raise ValueError("value for list node must be between 0 and 9 included.")
        self._val = value
        return self._val

    def build_from_int_sequence(self, sequence: Sequence[int]) -> "ListNode":
        if self.next:
            raise ValueError("This list node has already a node as next.")
        if not all(isinstance(x, int) for x in sequence):
            raise ValueError("sequence must be an int iterable.")

        current: "ListNode" = self
        current.val = sequence[0]

        for num in sequence[1:]:
            new_node = ListNode(val=num)
            current.next = new_node
            current = new_node

        return self

    def get_number(self, reverse: bool = True) -> int:
        as_list = list(self)
        if reverse:
            as_list.reverse()
        return int(''.join(map(str, as_list)))


class Solution:

    def add_two_numbers(self, linked_list_1: ListNode, linked_list_2: ListNode) -> ListNode:
        sum_result: int = linked_list_1.get_number() + linked_list_2.get_number()
        return ListNode().build_from_int_sequence([int(x) for x in reversed(str(sum_result))])


class TestListNode(TestCase):
    def setUp(self) -> None:
        self.list_node = ListNode()

    def test_build_from_int_sequence(self) -> None:
        case_1: list[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(self.list_node.build_from_int_sequence(case_1), case_1)


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_add_two_numbers_case_1(self) -> None:
        first_list: list[int] = [2, 4, 3]
        list_node_1: ListNode = ListNode().build_from_int_sequence(first_list)
        second_list: list[int] = [5, 6, 4]
        list_node_2: ListNode = ListNode().build_from_int_sequence(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [7, 0, 8])

    def test_add_two_numbers_case_2(self) -> None:
        first_list: list[int] = [0]
        list_node_1 = ListNode().build_from_int_sequence(first_list)
        second_list: list[int] = [0]
        list_node_2 = ListNode().build_from_int_sequence(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [0])

    def test_add_two_numbers_case_3(self) -> None:
        first_list: list[int] = [9,9,9,9,9,9,9]
        list_node_1 = ListNode().build_from_int_sequence(first_list)
        second_list: list[int] = [9,9,9,9]
        list_node_2 = ListNode().build_from_int_sequence(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [8,9,9,9,0,0,0,1])

if __name__ == "__main__":
    main()
