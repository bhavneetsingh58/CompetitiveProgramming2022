
class Solution:    
    def findDuplicate(self, nums: list[int]) -> int:
	
        def store(nums: list[int], cur: int) -> int:
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)
        
        return store(nums, 0)

l1 = [1,2,3,1]
obj1 = Solution()
print(obj1.findDuplicate(l1))