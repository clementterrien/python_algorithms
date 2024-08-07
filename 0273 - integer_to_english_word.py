# This is a problem given by Leetcode.com
# https://leetcode.com/problems/integer-to-english-words/

import sys
from unittest import TestCase, main


class Solution:
    def __init__(self) -> None:

        self.map = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
            20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
            100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"
        }

    def number_to_words(self, number: int, recursion: bool = False) -> str:
        word: str = ''

        if number == 0 and not recursion:
            return "Zero"

        if number in self.map and number < 100:
            word += self.to_words(number)
            return self._format_word(word) if not recursion else word

        largest: int = self._get_largest(number)

        if largest < 100:
            word += self.to_words(largest)
            number -= largest

            if number:
                word += ' ' + self.number_to_words(number, recursion=True)
                return self._format_word(word) if not recursion else word

        str_largest: str = str(largest)
        first: str = self.number_to_words(self._get_unit(int(str_largest)), recursion=True)
        unit: str = self.to_words(self._get_significant_base(largest, round_to_one=True))
        number -= largest
        word += f"{first} {unit} "

        if number:
            word += ' ' + self.number_to_words(number, recursion=True)

        return self._format_word(word) if not recursion else word

    def _format_word(self, word: str) -> str:
        if not word:
            raise ValueError("word has not been set.")

        return ' '.join([x.title() for x in word.split()]).strip()

    def _get_significant_base(self, number: int, round_to_one: bool = False) -> int:
        str_number: str = str(number)
        number_of_digits_to_return: int = len(str_number) if len(str_number) < 4 else len(str_number) - (len(str_number)-1) % 3
        str_number = str_number[: number_of_digits_to_return]

        return int(f"{str_number[0] if not round_to_one else 1}{'0'*(len(str_number)-1)}")

    def _get_largest(self, number: int, round_to_one: bool = False) -> int:
        str_number: str = str(number)
        if len(str_number) <= 3:
            return int(f"{str_number[0] if not round_to_one else 1}{'0'*(len(str_number)-1)}")

        unit: int = self._get_unit(number)

        return int(f"{self._get_unit(number) if not round_to_one else 1}{'0'*(len(str_number)-len(str(unit)))}")

    def _get_unit(self, number: int) -> int:
        str_number: str = str(number)
        if len(str_number) < 4:
            number_of_digits_to_return = 1
        elif len(str_number) % 3 == 0:
            number_of_digits_to_return = 3
        else:
            number_of_digits_to_return = len(str_number) % 3

        return int(str_number[:number_of_digits_to_return])

    def to_words(self, number: int) -> str:
        if number in self.map:
            return f" {self.map[number]}"
        else:
            raise ValueError("No word mapping for this integer")


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_number_to_words_with_unit(self) -> None:
        for i in range(10):
            self.assertEqual(self.solution.number_to_words(i), self.solution.map[i].title())

    def test_number_to_words_with_tenth(self) -> None:
        test_cases: list[tuple[int, str]] = [
            (23, "Twenty Three"),
            (42, "Forty Two"),
            (55, "Fifty Five")
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution.number_to_words(entry), waited)

    def test_number_to_words_with_hundreds(self) -> None:
        test_cases: list[tuple[int, str]] = [
            (100, "One Hundred"),
            (300, "Three Hundred"),
            (142, "One Hundred Forty Two"),
            (555, "Five Hundred Fifty Five")
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution.number_to_words(entry), waited)

    def test_number_to_words_with_thousands(self) -> None:
        test_cases: list[tuple[int, str]] = [
            (1000, "One Thousand"),
            (12345, "Twelve Thousand Three Hundred Forty Five"),
            (956999, "Nine Hundred Fifty Six Thousand Nine Hundred Ninety Nine"),
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution.number_to_words(entry), waited)

    def test_number_to_words_with_millions(self) -> None:
        test_cases: list[tuple[int, str]] = [
            (1000000, "One Million"),
            (67234567, "Sixty Seven Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
            (999999999, "Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine"),
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution.number_to_words(entry), waited)

    def test_number_to_words_with_billions(self) -> None:
        test_cases: list[tuple[int, str]] = [
            (1000000000, "One Billion"),
            (999999999999, "Nine Hundred Ninety Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine"),
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution.number_to_words(entry), waited)

    def test_get_significant_base(self) -> None:
        for num, result in zip([1, 23, 456, 5874, 10223, 9679691], [1, 20, 400, 5000, 1000, 9000000]):
            self.assertEqual(self.solution._get_significant_base(num), result)

        for num, result in zip([1, 23, 456, 5874, 10223, 9679691], [1, 10, 100, 1000, 1000, 1000000]):
            self.assertEqual(self.solution._get_significant_base(num, round_to_one=True), result)

    def test_get_unit(self) -> None:
        test_cases: list[tuple] = [
            (2, 2),
            (30, 3),
            (100, 1),
            (100000, 100),
            (2000, 2),
            (25000, 25),
            (480000, 480),
            (9456834, 9),
            (16456834, 16),
            (121456834, 121),
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution._get_unit(entry), waited)

    def test_get_largest(self) -> None:
        test_cases: list[tuple] = [
            (1, 1),
            (9, 9),
            (15, 10),
            (111, 100),
            (1245, 1000),
            (10000, 10000),
            (100000, 100000),
            (2000, 2000),
            (25000, 25000),
            (480000, 480000),
            (9456834, 9000000),
            (16456834, 16000000),
            (121456834, 121000000),
        ]
        for entry, waited in test_cases:
            self.assertEqual(self.solution._get_largest(entry), waited)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(Solution().number_to_words(int(sys.argv[1])))
    else:
        main()
