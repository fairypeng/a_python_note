"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum

"""


class Solution(object):
    def twoSum1(self, nums, target):
        """两层循环,简单粗暴"""
        for i in range(len(nums)):
            for n in range(i+1, len(nums)):
                if nums[i] + nums[n] == target:
                    return i, n

    def twoSum2(self, nums, target):
        """一次循环获取所有的索引，将索引与值拼成一个字典，求出目标值与当前值的差值，遍历num，判断差值在不在字典里面"""
        index = [i for i in range(len(nums))]
        data_dict = dict(zip(nums, index))
        for nu in range(len(nums)):
            difference = target - nums[nu]
            if difference in data_dict.keys():
                return nu, data_dict[difference]

    def twoSum3(self, nums, target):
        """创建一个字典，遍历数组，求出目标值与当前值的差值，如果差值在字典里面，返回"""
        data_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in data_dict.keys():
                return i, data_dict[difference]
            data_dict[nums[i]] = i


S = Solution()
nums = [2, 7, 11, 15]
target = 9
ret1, ret2 = S.twoSum1(nums, target)
print(ret1, ret2)

res1, res2 = S.twoSum2(nums, target)
print(res1, res2)

r1, r2 = S.twoSum3(nums, target)
print(r1, r2)

