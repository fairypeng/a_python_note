#coding:utf-8
"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

 



 

示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
 

注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keyboard-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findWords(self, words):
        l1 = 'qwertyuiopQWERTYUIOP'
        l2 = 'asdfghjklASDFGHJKL'
        l3 = 'zxcvbnmZXCVBNM'
        l1,l2,l3 = set(l1),set(l2),set(l3)
        final = []
        for i in range(len(words)):
            s = set(words[i])
            if s&l1 == s or s&l2==s or s&l3==s:
                final.append(words[i])
        return final

    def findWords2(self,words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
        return res


s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(s.findWords(words))
print(s.findWords2(words))
