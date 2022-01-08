

class Solution(object):
    def findDuplicate(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        present = []
        for i in l1:
            if i in present:
                return i
            present.append(i)
                
l1 = [1,3,4,2,2]
obj1 = Solution()
print(obj1.findDuplicate(l1))



