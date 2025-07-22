from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int]) -> list:
        
        res = []
        if len(nums)<=2:
            return res
        
        if len(nums)==3:
            return nums[0] + nums[1] + nums[2]
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            low = i+1
            high = len(nums) - 1
            
            while low<high:
                temp_sum = nums[i]+nums[low]+nums[high]
                if temp_sum > 0:
                    high-=1
                elif temp_sum < 0:
                    low+=1
                else:
                    if [nums[i],nums[low],nums[high]] not in res:
                        res.append([nums[i],nums[low],nums[high]])
                    low+=1
                    while (nums[low]==nums[low-1] and low<high):
                        low+=1
        return res
    
s = Solution()
print(s.threeSumClosest([-1,2,1,-4]))

print(s.threeSumClosest([1,1,1,0]))

print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5]))