#!/usr/bin/python3
"""
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.You may assume that each
 input would have exactly one solution, and you may not use the same element twice.
 """
# solution
"""
1. initialize an empty hashmap
2. iterate through the array 'nums' and for each element:
calculate the component('target - current_element')
check if the complement exists in the hashmap, if it does,
return the indices[index_of_complement, current_index]
otherwise store the element in the hashmap with its index
3. if no such pair is found, return an empty list or
 handle it according to the problem constraints
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #initialize empty dictionary to store elements and their indices
        num_dict = {}

        #traverse throught the array using enumerate to get both index and value
        for index, num in enumerate(nums):
            #calculate the complement for current element
            complement = target - num

            #check if complement exists in the dictionary
            if complement in num_dict:
                #return indices of the two numbers
                return [num_dict[complement], index]
            #store current element and its index in the dictionary
            num_dict[num] = index

        return []
