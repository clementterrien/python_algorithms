# This is a problem given by Leetcode.com
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

from unittest import TestCase, main


class Solution:
    """ Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
        A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

        Constraints:
            - m == mat.length
            - n == mat[i].length
            - 1 <= n, m <= 50
            - 1 <= matrix[i][j] <= 105.
            - All elements in the matrix are distinct.
    """

    def lucky_numbers(self, matrix: list[list[int]]) -> list[int]:
        """ Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
            A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

            Args:
                matrix (list[list]): An [m x n] matrix of distinct numbers

            Returns:
                int: The element of the matrix such that it is the minimum element in its row and maximum in its column.
        """
        assert isinstance(matrix, list) and all([isinstance(row, list) for row in matrix]), "The matrix is not valid."

        min_rows = [min(row) for row in matrix]

        max_columns = []

        for col_i in range(len(matrix[0])):
            column = []
            for row_i in range(len(matrix)):
                column.append(matrix[row_i][col_i])
            max_columns.append(max(column))

        common_elements = list(set(min_rows) & set(max_columns))

        return [common_elements[0]] if len(common_elements) > 0 else []


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_1(self):
        case_1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
        self.assertEqual(self.solution.lucky_numbers(case_1), [15])

    def test_case_2(self):
        case_2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
        self.assertEqual(self.solution.lucky_numbers(case_2), [12])

    def test_case_3(self):
        case_3 = [[7, 8], [1, 2]]
        self.assertEqual(self.solution.lucky_numbers(case_3), [7])


if __name__ == "__main__":
    main()
