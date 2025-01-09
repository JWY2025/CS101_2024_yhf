# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：

首先找出电视机里所有价格为负的

然后把这些负价格的电视从小到大排列（sort）

最后从头开始取至多m个

代码

```python
# sale
[n,m]=list(map(int,input().split()))
prices = list(map(int,input().split()))
prices_negative = [price for price in prices if price <0]
prices_negative_sorted = sorted(prices_negative)
earn = 0
if len(prices_negative_sorted) >= m:
    earn = -sum(prices_negative_sorted[0:m])
else:
    earn = -sum(prices_negative_sorted)
print(earn)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-20 11.06.01](/Users/jiangwenyi/Desktop/截屏2024-10-20 11.06.01.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：

因为要求最少的硬币数量，肯定拿更多大面值的硬币，拿到超过一半为止

首先把硬币面值从大到小排序

然后从头开始一个个拿

拿到超过total/2停止

代码

```python
# twins
coins = int(input())
values = list(map(int, input().split()))
values = sorted(values,reverse=True)
taken = 0
iteration = 0
total = sum(values)
for i in range(coins):
    if taken <= total/2:
        taken += values[i]
        iteration = iteration + 1
    else:
        break
print(iteration)

```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-20 11.06.29](/Users/jiangwenyi/Desktop/截屏2024-10-20 11.06.29.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

横排和竖列里各有一个最小的数

这个数和对方的所有数相加，肯定比自己这边的其他数和对方的所有数相加要小

所以要的是横排和竖列里同样如此操作更小的那个

代码

```python
# chips on the board
tests = int(input())
for _ in range(tests):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    matrix = [a,b]
    smallest = min(sum(b)+n*min(a),sum(a)+n*min(b))
    print(smallest)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-20 11.07.01](/Users/jiangwenyi/Desktop/截屏2024-10-20 11.07.01.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

首先4人一组的先占一辆车

然后3人一组的再占一辆车，但是每辆车上空一个位置

然后2人一组的两组占一辆车，如果最后多出一组，就多两个位置

最后让1人一组的填空位置，如果坐不下再4人一辆车新占车

代码

```python
# taxi
# 和装箱问题的思路比较像
groups = int(input())
members = list(map(int, input().split()))

four = [x for x in members if x == 4]
three = [x for x in members if x == 3]
two = [x for x in members if x == 2]
one = [x for x in members if x == 1]

import math
taxi = len(four) + len(three) + math.ceil(len(two) / 2)
space = len(three) + 2 * (math.ceil(len(two)/2)-len(two)//2)
if space < len(one):
    rest = len(one) - space
    taxi += math.ceil(rest/4)

print(taxi)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-20 11.20.43](/Users/jiangwenyi/Desktop/截屏2024-10-20 11.20.43.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：



代码

```python


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：



代码

```python


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这星期没怎么做题目，其实也就做了月考的题目

但是做taxi这道题目的时候明显觉得自己的思路顺畅很多，原因是做过装箱了

所以刷题不仅是练习，更是一种积累思路的过程

