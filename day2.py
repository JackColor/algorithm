# _*_ coding:utf-8 _*_
# __author__JackColor__
"""
7.
给定一个 32 位有符号整数，将整数中的数字进行反转 溢出问题

a = 123  321
b = -123  -321

"""


#  1
def test(num):
    s_num = str(num)[::-1] if num > 0 else "-" + str(abs(num))[::-1]
    s_num = int(s_num)
    if s_num > 0x7FFFFFFF:
        s_num = 0
    return s_num


# 2
def test2(num):
    mark = 1 if num > 0 else 0
    s_num = int(str(abs(num))[::-1])

    if s_num > 0x7FFFFFFF:
        s_num = 0
        return s_num

    s_num = s_num if mark else mark * s_num

    return s_num


if __name__ == '__main__':
    num = -120
    print(test2(num))
