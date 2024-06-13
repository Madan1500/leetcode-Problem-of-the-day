# Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-13


def minMovesToSeat(seats, students) -> int:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        difference = []
        students.sort()
        seats.sort()
        for i in range(len(seats)):
            difference.append(abs(students[i] - seats[i]))
        return sum(difference)

def minMovesToSeat(seats, students) -> int:
        # Time complexity: O(nlogn)
        # Space complexity: O(1)
        difference = 0
        students.sort()
        seats.sort()
        for i in range(len(seats)):
            difference += abs(students[i] - seats[i])
        return difference

# Test cases

# Test case 1
seats = [3, 1, 5]
students = [2, 7, 4]
# 4

# Test case 2
seats = [4, 1, 5, 9]
students = [1, 3, 2, 6]
# 7

# Test case 3
seats = [2, 1, 6, 2]
students = [1, 2, 3, 4]
# 3

print(minMovesToSeat(seats, students))