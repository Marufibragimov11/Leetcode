"""
                                            #1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


# My Solution
def two_sum(nums: list, target: int):
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if target == num + nums[j]:
                return i, j


print(two_sum(nums=[3, 2, 4], target=6))


# Solution given by ChatGPT
def two_sum_1(nums, target):
    num_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        # Check if the complement is in the dictionary
        if complement in num_dict:
            # If found, return the indices
            return [num_dict[complement], i]

        # If not found, add the current element to the dictionary
        num_dict[num] = i

    # If no solution is found
    return None


print(two_sum_1(nums=[2, 7, 11, 15], target=9))


# Solution from YouTube

def two_sum_2(nums: list, target: int):
    previous_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in previous_map:
            return [previous_map[diff], i]
        previous_map[n] = i
    return None
