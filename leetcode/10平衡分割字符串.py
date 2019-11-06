"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

 

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 2：

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 3：

输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".
 

提示：

1 <= s.length <= 1000
s[i] = 'L' 或 'R'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
"""


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = 0
        R = 0
        ret = 0
        for i in range(len(s)):
            if s[i] == "L":
                L += 1
            else:
                R += 1
            if L == R:
                ret += 1
        return ret

    def balancedStringSplit2(self, s):
        L_list = []
        R_list = []
        res = 0
        for i in s:
            if i == "L":
                L_list.append(i)
            if i == "R":
                R_list.append(i)
            if len(L_list) == len(R_list):
                res += 1
        return res


s = Solution()
str = "RLRRLLRLRL"
res = s.balancedStringSplit(str)
ret = s.balancedStringSplit2(str)
print(res, ret)

