class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        counter = collections.Counter(nums)
        
        if length<3:
            return counter.keys()
        
        result = []
        
        words = counter.most_common(3)
        
        for i in range(0,min(3,len(counter))):
            if words[i][-1]>length/3:
                result.append(words[i][0])
        return result
