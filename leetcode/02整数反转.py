"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
eg:
输入：123
输出:321

输入：-123
输出：-321

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [(−2)^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer

"""

class Solution(object):
    def reverse(self, x):
        """这个思路是将int转成str """
        if x == 0:
            return x
        if x > 0:
            str_x = str(x)
            reverse_str_x = str_x[::-1]
            reverse_x = int(reverse_str_x)
            if reverse_x < ((-2) ** 31) or reverse_x > ((2 ** 31) - 1):
                return 0
        else:
            str_x = str(x)
            reverse_str_x = str_x[::-1]
            reverse_str_x = "-" + reverse_str_x.replace("-","")
            reverse_x = int(reverse_str_x)
            if reverse_x < ((-2) ** 31) or reverse_x > ((2 ** 31) - 1):
                return 0
        return reverse_x

    def reverse2(self,x):
        """取余再除以10向下取整，这样可以逆序获取数字的各个位，再迭代乘以10就能计算出逆序数了"""
        flag = 1 if x >= 0 else -1
        new_x = 0
        abs_x = abs(x)
        while abs_x:
            new_x = new_x * 10 + abs_x % 10
            abs_x //= 10
        new_x = flag * new_x
        if new_x < pow(-2,31) or new_x > pow(2,31):
            return 0
        else:
            return new_x


s = Solution()
data = s.reverse(-1230)
print data
datas = s.reverse2(-1230)
print datas
