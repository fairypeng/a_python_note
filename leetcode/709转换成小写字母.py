#coding:utf-8
"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

 

示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/to-lower-case

对所有65～90之间的进行加32运算，最后拼接就行
"""



class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

    def toLow(self,str):
        ret = ""
        for s in str:
            if ord(s) in range(65,91):
                ret += chr(ord(s) + 32)
            else:
                ret += s
        return ret

s = Solution()
print(s.toLowerCase("Hello"))
print(s.toLow("Hello"))
