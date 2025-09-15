class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointer opposite sides
        # check area, then move in and re check
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            # check the hights if left is smaller then right then move left and vise versa
            area = (right - left)*(min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(area,maxArea)
        return maxArea