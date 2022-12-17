class Solution(object):
    def majorityElement(self, nums):
        count, res = 0,0
        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count = count + 1
            else:
                count = count - 1
                
        return res
