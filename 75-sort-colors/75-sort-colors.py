class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0, 0, 0]
        
        for num in nums:
            count_arr[num] = count_arr[num] + 1
        for i in range(len(nums)):
            if i + 1 <= count_arr[0]:
                nums[i] = 0
            elif i + 1 <= count_arr[0] + count_arr[1]:
                nums[i] = 1
            else:
                nums[i] = 2