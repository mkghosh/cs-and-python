# Problem Set 1

<br>

## 词频统计

题目描述为接受一个全小写字符串 `s`, 统计一个单词出现的次数.

参考实现 `src/freqCount.py`. 这里在原题的基础上进行了一点小修改,
接受多个关键字组成的任意一维序列, 返回 `{keyword: count}` 组成的字典.


## 字母序子串

题目描述为设有一全小写字符串 `s`, 输出其中由字母顺序组成的最长的子字符串.
存在并列的情况下输出第一个字符串.

该题的基本思路是:

- 从第一个字符开始遍历字符串,
- 同时不断比较当前字符和下一个字符的大小,
- 直到当前字符比下一个字符大的情况下终止一次遍历,
- 然后遍历范围不断后移 (遍历范围使用字符串切片操作确定).
- 所有的结果汇总到一个序列中, 然后按题目要求返回其中相应的元素.

参考实现 `src/alphaSub.py`
