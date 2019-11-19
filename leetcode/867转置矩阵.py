#coding:utf-8
"""
， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

 

示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
 

提示：

1 <= A.length <= 1000
1 <= A[0].length <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/transpose-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def transpose(A):
    m, n = len(A), len(A[0])
    r = [[0 for i in range(m)] for j in range(n)]
    # 不推荐使用临时变量 + 在矩阵A上直接修改. 这样代码不太好理解.
    for i in range(n):
        for j in range(m):
            r[i][j] = A[j][i]

    return r

def transpose1(A):
    return list(zip(*A))

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(transpose1([[1,2,3],[4,5,6],[7,8,9]]))

