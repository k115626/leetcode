"""
解题思路：
1. '滑动窗口'
    右边界不断的右移，只要没有重复的字符就不断扩充，碰到重复数字，左边界右移，直到走出重复数字
    每次滑动统计最大长度，更新最大长度
"""


def lengthOfLongestSubstring(s):
    max_length = 0
    current_str = []
    for i in s:
        if i not in current_str:
            current_str.insert(0, i)
            if max_length < len(current_str):
                max_length = len(current_str)
        else:
            while i in current_str:
                current_str.pop()
                if max_length < len(current_str):
                    max_length = len(current_str)
            current_str.insert(0, i)
    return max_length


if __name__ == '__main__':
    result = lengthOfLongestSubstring('aab')
    print(result)