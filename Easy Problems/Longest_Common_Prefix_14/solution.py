"""
                                            14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longest_common_prefix(strs: list):
    res = ""
    if not strs:
        return ""
    for index in range(len(strs[0])):
        for word in strs:
            if index == len(word) or strs[0][index] != word[index]:
                return res
        res += strs[0][index]
    return res


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
