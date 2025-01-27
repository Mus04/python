""" Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    
    Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
        	return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        result = 0
        while left < right:
        	if height[left] < height[right]:
        		if height[left] > leftMax:
        			leftMax = height[left]
        		else:
        			result += (leftMax - height[left])
        		left += 1
        	else:
        		if height[right] > rightMax:
        			rightMax = height[right]
        		else:
        			result += (rightMax - height[right])
        		right -= 1

        return result 
