"""
解题思路:
1. 输入为有序数组，所以重复元素一定是相邻的
    定义一个快指针和一个慢指针
    判断快慢指针指定的值是否相等，相等快指针后移，不相等将值复制在慢指针的后一位，然后两指针均后移一位
"""


# 思路1
def removeDuplicates(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1



if __name__ == '__main__':
    nums = [1,1,1,1,1,]
    result = removeDuplicates(nums)
    print(result)