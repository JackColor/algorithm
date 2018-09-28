# _*_ coding:utf-8 _*_
# __author__JackColor__

"""
9
内容描述

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶: 122  221

你能不将整数转为字符串来解决这个问题吗？

"""

num = 1001
x = 12421

# revertNumber = 0
# while x > revertNumber:
#     #  每次把 刚才x//10的给反转回来 每次都把前一个数保存的基础上乘10 然后 + 上 1
#     revertNumber = revertNumber * 10 + x % 10  # x % 10 拿到除以10的余数
#     print("----+++>", x)
#     print("---->", revertNumber)
#     x //= 10  # 得到 x 除以 10 的整除的 整数部分  123//10 = 12
#
# print(x)
# print(revertNumber)


def ttest1(x):
    if x < 0:
        return False
    revertNumber = 0
    while x > revertNumber:
        #: 每次把 刚才x//10的给反转回来 每次都把前一个数保存的基础上乘10 然后 + 上 1
        revertNumber = revertNumber * 10 + x % 10  # x % 10 拿到除以10的余数
        print("----+++>", x)
        print("---->", revertNumber)
        x //= 10  #: 得到 x 除以 10 的整除的 整数部分  123//10 = 12

    return x == revertNumber or x / 10 == revertNumber


if __name__ == '__main__':
    pass
