"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
    unique element appears only once. The relative order of the elements should be kept the same. Then return
    the number of unique elements in nums.
    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order
    they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Check for an empty list
            return 0

        replace = 1  # Initialize to 1 as the first element is always unique
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Corrected comparison
                replace += 1
        return replace


if __name__ == '__main__':
    sol = Solution()
