"""
解题思路:
1. 设置两个指针，指向两个数组的头部
    数组长度是确定的，所以中位数的位置也是确定的
    比较两个指针指向的值，如果小，指针右移，弹出值
    弹出值的数量等于中位数的位置
2. 寻找第k小的数

"""


# # 思路1
# def findMedianSortedArrays(nums1, nums2):
#     import math
#     pr1 = 0
#     pr2 = 0
#     sum_len = len(nums1) + len(nums2)
#     if sum_len % 2 == 0:
#         mid_num = sum_len // 2 + 1
#     else:
#         mid_num = math.ceil(sum_len / 2)
#     new_nums = []
#     for i in range(mid_num):
#         if pr1 == len(nums1):
#             new_nums.extend(nums2[pr2: pr2+(mid_num - len(new_nums))])
#         elif pr2 == len(nums2):
#             new_nums.extend(nums1[pr1: pr1+(mid_num - len(new_nums))])
#         else:
#             if nums1[pr1] <= nums2[pr2]:
#                 new_nums.append(nums1[pr1])
#                 pr1 += 1
#             else:
#                 new_nums.append(nums2[pr2])
#                 pr2 += 1
#     if sum_len % 2 == 1:
#         return new_nums[-1]
#     else:
#         return sum(new_nums[-2:]) / 2


# 思路2
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums2, nums1 = nums1, nums2
    sum_len = len(nums1) + len(nums2)
    left, right, mid = 0, len(nums1), sum_len // 2


if __name__ == '__main__':
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = findMedianSortedArrays(nums1, nums2)
    print(result)

