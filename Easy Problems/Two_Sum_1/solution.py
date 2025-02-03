"""
                                                1. Two Sum
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

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


def solution(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


def solutionChatGPT(nums: list, target: int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i


print(solution(nums=[2, 7, 11, 15], target=9))
print(solution(nums=[3, 2, 4], target=6))
print(solution(nums=[3, 3], target=6))
