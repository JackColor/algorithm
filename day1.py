"""
1. 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

> 示例：

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

nums = [2, 7, 11, 15]

target = 9


#  1
def test():
    for i in nums:
        for j in nums:
            if j == target - i:
                print(nums.index(j))
                print(nums.index(i))
                exit()


# 2
def test2():
    for n in nums:
        if target - n in nums and n is not target - n:
            print(nums.index(n), nums.index(target - n))
            return


# 3 把索引存放在 字典的val 中
def test3():
    lookup = dict()
    for index, v in enumerate(nums):
        print(index, v)
        if target - v in lookup:  # 判断 target-v 得到的val 是否在字典的 key 里面
            return 1
        lookup[v] = index  # val --- index
    return []


if __name__ == '__main__':
    print(test3())
