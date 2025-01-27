"""Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 """
class Solution(object):
    def firstMissingPositive(self, nums):
       
        index_i = 0
        for index_j in range(len(nums)):
        	if nums[index_j] <= 0:
        		nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
        		index_i += 1

        for index in range(index_i, len(nums)):
        	if abs(nums[index]) - 1 < len(nums) and nums[abs(nums[index]) - 1] > 0:
        		nums[abs(nums[index]) - 1] =  -nums[abs(nums[index]) - 1]

        for index in range(nums):
        	if nums[index] > 0:
        		return index + 1
        return len(nums) + 1
