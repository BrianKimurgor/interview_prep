#!/usr/bin/python3
# Minimum Size Subarray Sum
"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or
equal to target. If there is no such subarray, return 0 instead.
"""
#solution
"""
1. initialize two pointers 'left' and 'right' both pointing to the
start of the array
2. use the pointers to create a sliding window and keep a running sum
of elements between 'left' and 'right' pointers
3. if the sum is less than the target, move the 'right pointer' to
the right to increase window size
4. If the sum is greater than or equal to the target, update the minimum
length if needed and move the left pointer to the right to decrease the
window size.
5. Continue this process until the right pointer reaches the end of the array.
6. Return the minimum length found or 0 if no subarray satisfies the condition.
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        : type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        min_len = float('inf')
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum >=target:
                min_len = min(min_len, right - left +1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
