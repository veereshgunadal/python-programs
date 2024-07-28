class Solution:
    def two_sum(self, nums, target):
        data = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value not in data:
                data.update({nums[i]: i})
            else:
                return [data[value], i]

s = Solution()
print(s.two_sum([2,7,11,15], 9))
print(s.two_sum([3,2,4], 6))
print(s.two_sum([3,3], 6))