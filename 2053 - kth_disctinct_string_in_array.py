import logging
from unittest import TestCase, main


class Solution:

    def get_kth_distinct_str(self, arr: list[str], k: int) -> str:
        """ Returns the k-th distinct string from the given list of strings.

            A distinct string is defined as a string that appears exactly once in the list.
            The method returns the k-th distinct string based on the order of their first occurrence.

            Parameters:
            arr (list[str]): The list of strings to process.
            k (int): The 1-based index specifying which distinct string to return.

            Returns:
            str: The k-th distinct string if it exists, otherwise an empty string.

            Raises:
            ValueError: If any element in `arr` is not a string.
        """
        if not all([isinstance(x, str) for x in arr]):
            raise ValueError("arr must be an array of str.")
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer")
        
        unique: list[str] = [x for x in arr if arr.count(x) == 1]
        
        if k > len(unique):
            logging.warning(f"get_kth_distinct_str: No {k}(th) disting str found in given array.")
            return ""
        else:
            return unique[k-1]


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_get_kth_distinct_str_returns_the_kth_unique_value_case_1(self) -> None:
        array: list[str] = ['d', 'b', 'c', 'b', 'c', 'a']

        k_th: int = 1
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'd')
        k_th = 2
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'a')

    def test_get_kth_distinct_str_returns_the_kth_unique_value_case_2(self) -> None:
        array: list[str] = ["aaa", "aa", "a"]

        k_th: int = 1
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'aaa')
        k_th = 2
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'aa')
        k_th = 3
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'a')

    def test_get_kth_distinct_str_returns_the_kth_unique_value_case_3(self) -> None:
        array: list[str] = ["a", "b", "a"]

        k_th: int = 1
        self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), 'b')
        k_th = 2
        
        with self.assertLogs(level="WARNING") as logs:
            self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), '')
            self.assertEqual(logs.records[0].message, f"get_kth_distinct_str: No {k_th}(th) disting str found in given array.")
    
    def test_get_kth_distinct_str_with_invalid_arr(self) -> None:
        invalid_arr_1 = [1, 2]
        k_th = 1

        with self.assertRaises(ValueError) as captured:
            self.solution.get_kth_distinct_str(invalid_arr_1, k_th) # type: ignore
        
        self.assertEqual(str(captured.exception), "arr must be an array of str.")

        invalid_arr_2: list[int | str] = ['a', 'b', 'c', 2]

        with self.assertRaises(ValueError) as captured:
            self.solution.get_kth_distinct_str(invalid_arr_2, k_th) # type: ignore
        
        self.assertEqual(str(captured.exception), "arr must be an array of str.")

    def test_get_kth_distinct_str_with_invalid_kth(self) -> None:
        arr: list[str] = ['a', 'b', 'c']
        k_th = 0

        with self.assertRaises(ValueError) as captured:
            self.solution.get_kth_distinct_str(arr, k_th) # type: ignore
        
        self.assertEqual(str(captured.exception), "k must be a positive integer")

        k_th = 'u' # type: ignore

        with self.assertRaises(ValueError) as captured:
            self.solution.get_kth_distinct_str(arr, k_th) # type: ignore
        
        self.assertEqual(str(captured.exception), "k must be a positive integer")

    def test_get_kth_distinct_str_returns_empty_string_and_warns_when_k_th_is_not_found(self) -> None:
        array: list[str] = ['d', 'b', 'c', 'b', 'c', 'a']

        k_th: int = 3
        with self.assertLogs(level="WARNING") as logs:
            self.assertEqual(self.solution.get_kth_distinct_str(array, k_th), '')
            self.assertEqual(logs.records[0].message, f"get_kth_distinct_str: No {k_th}(th) disting str found in given array.")


if __name__ == "__main__":
    main()
