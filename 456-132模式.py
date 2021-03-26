"""
解题思路:
单调栈
"""


def find132pattern(self, nums: List[int]) -> bool:
    n = len(nums)
    left_min = [float('inf')] * n  
    # 定义一个长度为nums并且值全为'inf'的数组
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], nums[i - 1])  # 生成一个位置到左边界取最小值的列表
    stack = []
    # 定义一个空栈
    for j in range(n-1, -1 , -1):
        numsk = float('-inf')
        while stack and stack[-1] < nums[j]:
            numsk = stack.pop()
        if left_min[j] < numsk:
            return True
        stack.append(nums[j])
    return False

    
