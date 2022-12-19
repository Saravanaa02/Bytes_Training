class Solution(object):
    def firstMissingPositive(self, nums):
        max_pos = len(nums)
        i = 0
        for n in nums:
            k = n
            while k<=max_pos and k>0 and k!=nums[k-1]:
                temp = nums[k-1]
                nums[k-1] = k
                k = temp
        while i<max_pos:
            if nums[i] != (i+1):
                break
            i += 1
        return i+1
