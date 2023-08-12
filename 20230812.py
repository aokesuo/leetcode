# -*- coding: utf-8 -*-
"""
Filename: 20230812.py
Author: Your Name
Email: your.email@example.com
Date Created: 2023/8/12
File Description:
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
"""

"""
解题思路：
其实主要考虑主线和副线即可，其实就是找到规律就可以，下面的代码中
i == j 就表示从00开始的那一条线， 这一条其实就是第n行的第n列 
 i + j == n - 1 表示从0，-1开始的 这里就是因为行数和列数相加，肯定被总长度多1，所以他只要是总长度-1一样就可以了
 
第二种：主要是吧所有线都提取了，不做判断等等，汇总完毕后
通过(n & 1)判断是奇数还是偶数，如果是奇数，就需要删除一次中间重复的值
"""


class Solution:
    def diagonal_sum(self, mat) -> int:
        n = len(mat)
        return sum(mat[i][j] for i in range(n) for j in range(n) \
                   if i == j or i + j == n - 1)

    def diagonal_sum_not2(self, mat) -> int:
        n = len(mat)
        total = 0
        mid = n // 2
        for i in range(n):
            total += mat[i][i] + mat[i][n - 1 - i]
        return total - mat[mid][mid] * (n & 1)


if __name__ == '__main__':
    mats = [[6, 3, 1, 10, 7, 4],
            [4, 10, 1, 9, 5, 10],
            [5, 5, 7, 3, 8, 5],
            [2, 7, 6, 4, 7, 6],
            [7, 9, 6, 1, 8, 5],
            [1, 7, 9, 5, 8, 4]]
    __count__ = Solution().diagonal_sum_not2(mats)
    print(__count__)
