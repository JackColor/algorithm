# _*_ coding:utf-8 _*_
# __author__JackColor__


"""
27
给定排序的数组nums，和一个val值 就地删除val的值，返回数组的新长度。

不要为另一个数组分配额外的空间，你必须这样做修改输入数组就地用O（1）额外的内存。
"""
#:集合　可以用

nums = [1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7]

def solutions(val):
    # 循环看下 值是否在字典里面
    while val in nums:
        nums.remove(val)

print(nums)

"""
28
实现strStr

返回haystack中第一次出现针的索引，如果针不是haystack的一部分，则返回-1。

例1：

输入： haystack =“hello”，needle =“ll”
 输出： 2
 
例2：
输入： haystack =“aaaaa”，needle =“bba”
 输出： -1

"""

string = "helloll"


# print(string.find("lop"))


def solution(s):
    if not s:
        return 0
    neddle_len = len(s)
    n = 0
    while True:
        ss = string[n:neddle_len]
        if ss != s:
            n += 1
            neddle_len += 1
            if len(string) == neddle_len:
                return -1
        else:
            print(n)
            return


if __name__ == '__main__':
    # solution("lo")
    pass
"""
35 
给定排序数组和目标值，如果找到目标，则返回索引。如果没有，请返回索引按顺序插入的索引。

您可以假设数组中没有重复项。

例1：

输入： [1,3,5,6]，5
 输出： 2
例2：

输入： [1,3,5,6]，2
 输出： 1
例3：

输入： [1,3,5,6]，7
 输出： 4
例4：

输入： [1,3,5,6]，0
 输出： 0

"""
nn = [1, 3, 5, 6]
v = 4
index = 0
for i in nn:
    if i != v and i < v:
        index = nn.index(i) + 1
    elif i != v and i > v:
        index = nn.index(i)
        break
    else:
        index = nn.index(i)

print(index)
