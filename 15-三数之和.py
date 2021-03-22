"""
解题思路:
1. 类似于两数之和，利用双指针
"""


def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            return result
        # 重复跳过，避免重复解
        if i > 0 and nums[i] == nums[i-1]:
            continue
        L = i + 1
        R = len(nums) - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                result.append([nums[i], nums[L], nums[R]])
                # 左右边界值重复的话，循环直至不再重复
                L += 1
                R -= 1
                while (L < R and nums[L] == nums[L-1]):
                    L += 1
                while (L < R and nums[R] == nums[R+1]):
                    R -= 1
            elif nums[i] + nums[L] + nums[R] > 0:
                R -= 1
            else:
                L += 1
    return result


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    result = threeSum(nums)
    print(result)

