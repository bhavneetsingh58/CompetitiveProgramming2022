

class Solution(object):
    def findDuplicate(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = nums
        for i in l1:
            l1.remove(i)
            for j in l1:
                if(i == j):
                    return i
                
l1 = [1,2,3,1]
obj1 = Solution()
print(obj1.findDuplicate(l1))



