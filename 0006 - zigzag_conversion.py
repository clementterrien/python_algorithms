# This is a problem given by Leetcode.com
# https://leetcode.com/problems/zigzag-conversion

from unittest import TestCase, main


class Solution:

    def convert(self, string: str, n_rows: int) -> str:
        """ Converts a given string into a zigzag pattern on a specified number of rows
            and reads it row by row to produce the output string.

            Args:
                string (str): The input string to be converted. Must consist of English letters,
                            ',' and '.' with a length between 1 and 1000 (inclusive).
                n_rows (int): The number of rows for the zigzag pattern. Must be an integer between 1 and 1000 (inclusive).

            Raises:
                ValueError: If `string` is not a valid string with a length between 1 and 1000.
                ValueError: If `string` contains characters other than English letters, ',' or '.'.
                ValueError: If `n_rows` is not an integer or is not between 1 and 1000.

            Returns:
                str: The zigzag-converted string read row by row.

            Example:
                Input:
                    string = "PAYPALISHIRING", n_rows = 3
                Output:
                    "PAHNAPLSIIGYIR"

                Explanation:
                The zigzag pattern with 3 rows would be:
                    P   A   H   N
                    A P L S I I G
                    Y   I   R
                Reading row by row gives "PAHNAPLSIIGYIR".
        """
        if not (isinstance(string, str) and 1 <= len(string) <= 1000):
            raise ValueError("Given string must contain between 1 and 1000 chars included.")
        if not all([x.isalpha() or x in [',', '. '] for x in string]):
            raise ValueError("Given string must consists of English letters, ',' and '.'..")
        if not (isinstance(n_rows, int) and 1 <= n_rows <= 1000):
            raise ValueError("n_rows must be an int between 1 and 1000 included.")

        if n_rows == 1 or n_rows >= len(string):
            return string

        final = ""

        array: list[list[str]] = [["0" for _ in range(len(string))] for _ in range(n_rows)]
        i_row: int = 0
        i_col: int = 0

        for s in string:
            array[i_row][i_col] = s
            if i_row != 0 and (array[i_row-1][i_col] == "0" or i_row == n_rows-1):
                i_row -= 1
                i_col += 1
            else:
                i_row += 1

        for row in array:
            final += ''.join([x for x in row if x != "0"])

        return final


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_convert_valid_case_1(self) -> None:
        string = "THISIS"
        self.assertEqual(self.solution.convert(string, n_rows=1), "THISIS")
        self.assertEqual(self.solution.convert(string, n_rows=2), "TIIHSS")
        self.assertEqual(self.solution.convert(string, n_rows=3), "TIHSSI")
        self.assertEqual(self.solution.convert(string, n_rows=4), "THSIIS")
        self.assertEqual(self.solution.convert(string, n_rows=5), "THISSI")
        self.assertEqual(self.solution.convert(string, n_rows=6), "THISIS")
        self.assertEqual(self.solution.convert(string, n_rows=7), "THISIS")

    def test_convert_valid_case_2(self) -> None:
        string = "THISISALONGSTRINGFORTHISTEST"
        self.assertEqual(self.solution.convert(string, n_rows=1), "THISISALONGSTRINGFORTHISTEST")
        self.assertEqual(self.solution.convert(string, n_rows=2), "TIIAOGTIGOTITSHSSLNSRNFRHSET")
        self.assertEqual(self.solution.convert(string, n_rows=3), "TIOTGTTHSSLNSRNFRHSETIAGIOIS")
        self.assertEqual(self.solution.convert(string, n_rows=4), "TATOTHSLSRFRSEIIOGIGTISSNNHT")

    def test_convert_valid_case_3(self) -> None:
        string = "PAYPALISHIRING"
        self.assertEqual(self.solution.convert(string, n_rows=4), "PINALSIGYAHRPI")

    def test_convert_with_invalid_string(self):
        with self.assertRaises(ValueError):
            self.solution.convert(string=1, n_rows=2)
        with self.assertRaises(ValueError):
            self.solution.convert(string='', n_rows=2)
        with self.assertRaises(ValueError):
            self.solution.convert(string='h'*1001, n_rows=2)
        with self.assertRaises(ValueError):
            self.solution.convert(string='hello world', n_rows=2)

    def test_convert_with_invalid_n_rows(self):
        with self.assertRaises(ValueError):
            self.solution.convert(string='thisisatest', n_rows='error')
        with self.assertRaises(ValueError):
            self.solution.convert(string='thisisatest', n_rows=0)
        with self.assertRaises(ValueError):
            self.solution.convert(string='thisisatest', n_rows=1001)


if __name__ == "__main__":
    main()
