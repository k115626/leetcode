"""
解题思路：
1. 将数组排序，定义首尾指针，判断两个指针指定的值和与给定目标值的大小，
    若和大，尾指针向前移动一位，再判断
    若和小，首指针向后移动一位，再判断
    首尾指针相遇，跳出
2. 准备一个字典，遍历数组，取数据与目标的差值
    若差值在字典中，返回
    若差值不在字典中，将数据与下标存入字典中
"""


# # 思路1
# def twoSum(nums, target):
#     start_pr = 0
#     end_pr = len(nums) -1
#     nums = [(val, index)for index, val in enumerate(nums)]
#     nums.sort()
#     while start_pr < end_pr:
#         if nums[start_pr][0] + nums[end_pr][0] == target:
#             return [nums[start_pr][1], nums[end_pr][1]]
#         elif nums[start_pr][0] + nums[end_pr][0] > target:
#             end_pr -= 1
#         else:
#             start_pr += 1
#     return []


# 思路2
## 列表中有多个相同元素并不影响
def twoSum(nums, target):
    map_dict = dict()
    for index, val in enumerate(nums):        
        another = target - val
        if another in map_dict:
            return [index, map_dict[another]]
        else:
            map_dict[val] = index
    return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target= 9
    result = twoSum(nums, target)
    print(result)
    