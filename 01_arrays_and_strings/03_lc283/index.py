class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Role of J:
        1. Stores the number of non-zero elements 
        2. move the non-zero items to the front of the array
        """
        j=0
        for num in nums:
            if (num != 0):
                nums[j] = num
                j += 1
        
        # Assign zero to every element after j position
        for x in range(j, len(nums)):
            nums[x] = 0