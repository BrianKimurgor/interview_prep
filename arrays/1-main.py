#!/usr/bin/python3

from two_sum import Solution

def main():
    sol = Solution()

    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(sol.twoSum([3, 3], 6))          # Output: [0, 1]


if __name__ == "__main__":
    main()
