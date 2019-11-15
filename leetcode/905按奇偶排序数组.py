#coding:utf-8
"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

 

示例：

输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 

提示：

1 <= A.length <= 5000
0 <= A[i] <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for a in A:
            if a % 2 == 0:
                even_list.append(a)
            if a % 2 == 1:
                odd_list.append(a)
        even_list.extend(odd_list)
        return even_list

    def sortArrayByParity2(self, A):
        ret = []
        for a in A:
            if a % 2 == 0:
                ret.insert(0, a)
            if a % 2 == 1:
                ret.insert(len(ret), a)
        return ret


s = Solution()
A = [3, 1, 2, 4]
print(s.sortArrayByParity(A))
print(s.sortArrayByParity2(A))
