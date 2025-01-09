# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

先把p e i变成d之后第一次出现peak的天数（按照当年的第一天开始算）

然后找到他们共同出现peak的第一天（按照当年的第一天开始计算）

最后减去d，就得到了以d为第一天开始算的他们共同出现peak的第一天

代码：

```python
# 生理周期
# p, e, i : 体力高峰，感情高峰，智力高峰
# p, e, i 周期为 23，28, 33
case = 0
while True:
    p, e, i, d = map(int, input().split())
    import math
    # all函数用于判断某个迭代器（eg 列表，元组，集合等）是否每个元素都为真
    # while not all(x== -1 for x in [p,e,i,d]):
    if p + e + i + d != -4:

        #  先把p、e、i变成d之后第一次出现peak的天数（按照当年的的一天开始计算）
        if p < d:
            x = math.ceil((d - p) / 23)
            p = p + 23*x
        else:
            x = math.floor((p - d) / 23)
            p = p - 23*x

        if e < d:
            y = math.ceil((d - e) / 28)
            e = e + 28*y
        else:
            y = math.floor((e - d) / 28)
            e = e - 28*y

        if i < d:
            z = math.ceil((d - i) / 33)
            i = i + 33*z
        else:
            z = math.floor((i - d) / 33)
            i = i - 33*z

        # print(p,e,i)

        for x in range(1, math.ceil(21253/23) + 1):
            if (p + 23*x - e) % 28 == 0 and (p + 23*x - i) % 33 == 0:
                day = p + 23*x
                case += 1
                print(f"Case {case}: the next triple peak occurs in {day-d} days.")
                break
    else:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-27 17.49.11](/Users/jiangwenyi/Desktop/截屏2024-10-27 17.49.11.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

制造低价的武器，如果没钱，卖出高价的武器

卖一个武器肯定可以买至少一个武器

剩下最后一个武器的时候，能造就造，不能造也不卖

但是

代码：

```python
# 军备竞赛
# p：起始经费
p = int(input())
# costs：每张图的制作成本，同时也是卖价
costs = list(map(int, input().split()))
costs.sort()
n = len(costs)

# 制造低价的武器，如果没钱，卖出高价的武器
# 双指针，i从低价往高价，j从高价往低价
# 指针指在 i，j 上时，自己拥有的是 i 个武器，敌国拥有的是 n - j  个武器

# 如果有足够的武器，卖一个武器一定能买至少一个武器
# 剩下最后一个武器的时候，能造就造，造不起也不要卖
i, j = 0, n-1
own = 0
enemy = 0
# 第一个图必须得造，如果不能造那么就直接结束
if costs[0] <= p:
    p -= costs[0]
    i = 1
    own += 1

    while i < j:
        if costs[i] <= p:
            p -= costs[i]
            i += 1
            own += 1

        else:
            p += costs[j]
            j -= 1
            enemy += 1

    # 这里出了while i < j 的循环
    if costs[i] <= p:
        own += 1
        print(own-enemy)
    else:
        print(own-enemy)
else:
    print(0)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-27 19.31.13](/Users/jiangwenyi/Desktop/截屏2024-10-27 19.31.13.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

就是从小到大排这些时间

给每个时间绑定一个label（学生编号）

然后用prefix来计算每个学生等待的时间

最后计算每个学生的平均等待时间

代码：

```python
# 排队做实验v0.2
n = int(input())
times = list(map(int, input().split()))
students = list(range(1,n+1))
stu_time = [[] for _ in range(n)]
for i in range(n):
    stu_time[i] = [students[i],times[i]]
stu_time.sort(key = lambda x : x[1])
for i in range(n):
    print(stu_time[i][0], end =' ')
print()
wait = [0] * n
prefix = [0]
for i in range(n-1):
    prefix.append(prefix[-1] + stu_time[i][1])

average = sum(prefix)/n
print(f"{average:.2f}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-28 00.47.44](/Users/jiangwenyi/Desktop/截屏2024-10-28 00.47.44.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

首先把Haab日期转换为“第几天”

然后计算这天是哪个年份的

然后计算这天是这个年份的“第几天”

然后用13和20的模去算cycle的组合，但是注意余0的情况实际上要记为13 和 20

代码：

```python

# Maya Calendar
n = int(input())


month_names = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
              'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
cycle_names = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat',
               'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban',
               'eznab', 'canac', 'ahau']
print(n)

for _ in range(n):
    date = input().split()
    date[0] = int(date[0][:-1])
    date[2] = int(date[2])
    # print(date)
    day = date[0] + 1
    month = month_names.index(date[1])
    year = date[2]
    # print(day, month, year)

    date = day + 20 * month + 365 * year

    # print(date)
    year = (date-1) // 260
    date -= year * 260

    cycle_number = date % 20 if date % 20 != 0 else 20
    number = date % 13 if date % 13 != 0 else 13
    cycle = cycle_names[cycle_number - 1]

    print(f"{number}" + ' ' + cycle + ' ' + f"{year}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-10-28 02.34.35](/Users/jiangwenyi/Desktop/截屏2024-10-28 02.34.35.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这周在赶每日选做，1010以前的全部做完了，但是1010及以后的只做了这次作业的前四题，之后再补一补

这周做题慢，主要原因是代码里出现了很低级的错误检查不出来，比如maya calendar里忘记加上第19个月份的名字，军备竞赛里检验制造第一个武器，如果制造忘记减去成本，生理周期里的周期对应关系搞混了之类的错误

这种小错误很容易检查不出来，因为注意检查的总是算法和临界条件

下次记得要早点用测试数据来检查，可以省去很多心力和时间

