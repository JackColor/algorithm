# _*_ coding:utf-8 _*_
# __author__JackColor__


"""
14
编写一个函数来查找字符串数组中最长的公共前缀字符串。

如果没有公共前缀，则返回空字符串""。

例1：

输入：["flower","flow","flight"]
 输出： “fl”
例2：

输入： ["dog","racecar","car"]
 输出： “”
 说明：输入字符串中没有公共前缀。


注意：所有给定的输入都是小写字母a-z。
"""

s = ["flower", "flow", "flight"]



def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    for i in range(len(strs[0])):  #: 比较都是跟开头的的第一个字符比较 所以用第一个做依据
        for str in strs:
            #: 第一个判断是 如果我循环的每个字符串的长度比当前 i 小
            #: 证明接下来str不可能再有值了所以return

            #:第一个条件满足，则 判断第二个条件
            #: 第一个字符串当前的i索引的字母u与当前正在循环的str不相等 就直接return

            #: 都满足就继续循环
            if len(str) <= i or strs[0][i] != str[i]:
                return strs[0][:i]
    return strs[0]




# s = ["flower", "flow", "flight"]

"""
解法2:
dp[i]代表前i+1个字符串的最大前缀串，
如果第i+2个字符串不以dp[i]为前缀，就去掉dp[i]的最后一个字符再试一次
都去完了那么dp[i+1]肯定就是空串了，也就等于这时候的dp[i]，因为dp[i]的每个字符已经被去完了

"""



def longestCommonPrefix2(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    dp = [strs[0]]*len(strs)
    for i in range(1,len(strs)):
        #: 1  ,  2
        while not strs[i].startswith(dp[i-1]):
            dp[i-1] = dp[i-1][:-1]
        dp[i] = dp[i-1]
    return dp[-1]


#: 3 os.path.commonprefix()


if __name__ == '__main__':
    import os

    res = longestCommonPrefix2(s)
    print(res)

    ss = ["sss"] *3

