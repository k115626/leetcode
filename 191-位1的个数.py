"""
解题思路:
1. 将二进制的每位与只有该位为1的二进制数做与运算，求和
2. n & (n-1)
    该表达式的作用是将n的最低位的1变为0
    n - 1 ==> 110000 变为 101111
"""


# 思路1
def hammingWeight(n):
    # num = 0
    # for i in range(32):
    #     num += n & (1 << i)

    num = sum(i for i in range(32) if n & (1 << i))
    return num


# 思路2
def hammingWeight(n):
    num = 0
    while n:
        n &= n - 1
        num += 1
    return num