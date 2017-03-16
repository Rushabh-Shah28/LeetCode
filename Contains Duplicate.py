class Solution(object):
    def containsDuplicate(self, nums):
        counts = dict()
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
            
        for key,value in counts.iteritems():
            if counts[key]>1:
                return True
        
        return False