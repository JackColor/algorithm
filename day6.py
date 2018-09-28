# _*_ coding:utf-8 _*_
# __author__JackColor__


"""
20

内容描述

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

示例1：
输入: "()"
输出: true

示例2：
输入: "()[]{}"
输出: true

示例3：
输入: "(]"
输出: false

示例4：
输入: "([)]"
输出: false

示例5：
输入: "{[]}"
输出: true


"""

lookup_left = ["(", "[", "{"]

lookup_right = [")", "]", "}"]


def valid(string: str):
    stack = []
    for s in string:

        if s in lookup_left:

            stack.append(s)
        elif s in lookup_right:
            last_s = stack.pop()

            if last_s == "(" and s != ")":
                return False

            elif last_s == "[" and s != "]":
                return False

            elif last_s == "{" and s != "}":
                return False

    return stack == []


if __name__ == '__main__':
    res = valid("([])[]{}")
    print(res)
