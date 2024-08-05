#!/bin/bash

# Ask for exercise details
read -p "Enter the number of the exercise: " exercise_number
read -p "Enter the name of the exercise: " exercise_name
read -p "Enter the link of the exercise: " exercise_link
read -p "Enter the name of the solution main method: " solution_method

formatted_exercise_number=$(printf "%04d" $exercise_number)

# Format the exercise name to create a valid Python file name
file_name="${formatted_exercise_number} - $(echo ${exercise_name} | tr ' ' '_' | tr '[:upper:]' '[:lower:]').py"

file_content=$(cat <<EOF
# This is a problem given by Leetcode.com
# ${exercise_link}

from unittest import TestCase, main


class Solution:
    
    def ${solution_method}(self) -> None:
        return


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_${solution_method}_valid_case(self) -> None:
        case_1 = None
        self.assertEqual(self.solution.${solution_method}(case_1), None)

if __name__ == "__main__":
    main()
EOF
)

# Create the file and write the content
echo "$file_content" > "$file_name"

echo "File $file_name created successfully."