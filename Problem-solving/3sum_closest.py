from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        res = []
        if len(nums)<=2:
            return res
        
        if len(nums)==3:
            return nums[0] + nums[1] + nums[2]
        
        nums.sort()
        print(nums)
        
        c = float("inf")
        sum_ = 0
        for i in range(len(nums)):
            print(" ")
            print("i: ", i)
            
            # if i>0  and nums[i] == nums[i-1]:
            #     continue
            
            low = i+1
            high = len(nums) - 1
            
            while low<high:
                print("low", low)
                print("high", high)
                print(nums[i], nums[low], nums[high])
                temp_sum = nums[i]+nums[low]+nums[high]
                diff = abs(temp_sum - target)
                if diff < c:
                    c = diff
                    sum_ = temp_sum

                if temp_sum > target:
                    high-=1
                elif temp_sum < target:
                    low+=1
                else:
                    sum_ = temp_sum
                    return sum_
        return sum_
    
s = Solution()
s.threeSumClosest([-1,2,1,-4], 1)

print(s.threeSumClosest([1,1,1,0], -100))

print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))