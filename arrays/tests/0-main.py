#!/usr/bin/python3

from subarray import Solution

def main():
    sol = Solution()

    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # Output: 2
    print(sol.minSubArrayLen(4, [1, 4, 4]))           # Output: 1
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0

if __name__ == "__main__":
    main()
