#!/usr/bin/python3

from duplicate import Solution
  # Test case 1: List with duplicates

def main():
    sol = Solution()
    nums1 = [1, 1, 2]
    print("Test Case 1:", sol.removeDuplicates(nums1))  # Expected output: 2 (Unique elements: 1 and 2)

    # Test case 2: List with duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print("Test Case 2:", sol.removeDuplicates(nums2))  # Expected output: 5 (Unique elements: 0, 1, 2, 3, and 4)

    # Test case 3: List with no duplicates
    nums3 = [1, 2, 3, 4, 5]
    print("Test Case 3:", sol.removeDuplicates(nums3))  # Expected output: 5 (All elements are unique)

    # Test case 4: Empty list
    nums4 = []
    print("Test Case 4:", sol.removeDuplicates(nums4))  # Expected output: 0 (No unique elements in an empty list)

if __name__ == "__main__":
    main()
