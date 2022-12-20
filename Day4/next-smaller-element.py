class Solution:

    def immediateSmaller(self,arr,n):
        # code here
        
        for c in range(n-1):
            if arr[c]>arr[c+1]:
                arr[c] = arr[c+1]
            else:
                arr[c] = -1
        arr[n-1] = -1
