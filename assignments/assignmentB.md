# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>姜文宜</mark>



**说明：**

1）⽉考： AC1<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

不能同时更新最大值和最小值，因为必须先买进再抛掉，所以一定是在暂定的最小值之后再往后一个个找最大值，再实时更新最大利润

先假设第一天买进（第一天是暂定的最小值）、第一天抛出，再一个个往后遍历。如果第i天抛出可以获得更大的利润，就将最大利润更新为第i天的值-暂定最小值。

随时更新暂定最小值和暂定最大利润。

代码：

```python
 # 股民老张
a = list(map(int,input().split()))
# 因为抛掉一定在买进之后，所以如果当天的股价低于之前的最低股价，就有可能买进会得到更大收益
# 买进之后，再看之后是否应该抛掉
min_price = a[0]
max_profit = 0
for price in a:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price-min_price)
print(max_profit)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-10 22.59.31](/Users/jiangwenyi/Desktop/截屏2024-12-10 22.59.31.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

如果有一个鸡排时间很长，那么就一直把它放在锅里占一个位置

最好有很多时间很长的鸡排一直放在里面占着位置

所以要从大到小排列，挑出最大的那些（也就是在其他t更小的鸡排都煎熟的情况下还没有煎熟的那些），用他们来占位置

代码：

```python
# 煎鸡排
# k个位置
n,k=map(int,input().split())
t=list(map(int,input().split()))
# 煎鸡排需要的总时间
s = sum(t)
# 每块鸡排分到的时间是s/k
t.sort(reverse=True)
for a in t:
    if a>s/k:
        s-=a
        k-=1
print("%.3f"%(s/k))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-12-10 23.54.39](/Users/jiangwenyi/Desktop/截屏2024-12-10 23.54.39.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

有负数的情况下要拿出，拿出最小的那个负数

但是可以不管有没有负数直接考虑拿出最小的情况，如果不拿出比拿出要大，那就保留不拿出的那个就行

代码：

```python
l=list(map(int,input().split(',')))
n=len(l)
def solve():
    k=max(l)
    if k<0:
        return k
    la1=[-float('inf')]*n
    la2=la1[:]
    la1[0]=l[0]
    la2[-1] = l[-1]
    for i in range(1,n):
        la1[i]=max(la1[i-1]+l[i],l[i])
        la2[n-i-1]=max(la2[n-i]+l[n-i-1],l[n-i-1])
    ans=max(la1)
    for i in range(1,n-1):
        ans=max(ans,la1[i-1]+la2[i+1])
    return ans
print(solve())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-10 23.57.07](/Users/jiangwenyi/Desktop/截屏2024-12-10 23.57.07.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

希望左手上的数较大、右手上的数较小的大臣排在队伍的前面，这点月考的时候想到了，但是不知道到底怎么量化这个“较大”“较小”，看看别人的代码怎么量化的

代码：

```python
n=int(input())
a,b=map(int,input().split())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
from functools import cmp_to_key
def compare(a1, b1, a2, b2):
    return (max(1 / b1, a1 / b2) >= max(1 / b2, a2 / b1)) - \
           (max(1 / b1, a1 / b2) < max(1 / b2, a2 / b1))
def compare_wrapper(x, y):
    return compare(x[0], x[1], y[0], y[1])
l = sorted(l, key=cmp_to_key(compare_wrapper))
ans=a//l[0][1]
for i in range(1,n):
    a*=l[i-1][0]
    b*=l[i-1][1]
    ans=max(ans,a//l[i][1])
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-11 00.12.33](/Users/jiangwenyi/Desktop/截屏2024-12-11 00.12.33.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

很难的一次月考，就连E也不太简单

正在努力做每日选做，跟不上，不知道还有20天能不能补天啊，但是也没有太多时间花在上面，还有专业课和其他的事情

每日选做现在都是先看代码，看懂思路，然后按照自己的思路复写一遍，类似复述。但是有的时候会发现自己的实现思路会和答案的有点出入。我总是觉得自己的更直观（不是废话吗），但是看上去”补丁“会比较多。就怕考试的时候没有测试数据，不好打那些补丁。



