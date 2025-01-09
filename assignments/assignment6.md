# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

见代码注释

代码：

```python
# 汉诺塔
# init, temp, dest
n = int(input())
# 一个的时候，1步
moves = 1

# 有几个，就迭代几次
# 思路是把上面n-1个圆盘从A放到B柱子上，C是过渡柱子
# 然后把最大的圆盘（第n个）从A放到C柱子上
# 最后把n-1个圆盘从B放到C柱子上，A是辅助柱子
for i in range(1,n):
    moves = 2 * moves + 1

print(moves)
# 递归算法
# 常用技巧就是，定义一个函数，然后用这个函数处理n-1
# 但是需要处理到初始条件（在这题里是n=1)
def hanoi(n,init,temp,dest):
    if n == 1:
        print(f"{init}->{dest}")
    else:
        hanoi(n-1,init,dest,temp)
        print(init +"->"+ dest)
        hanoi(n-1,temp,init,dest)

hanoi(n,"A","B","C")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-02 23.48.31](/Users/jiangwenyi/Desktop/截屏2024-11-02 23.48.31.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

见代码注释

代码：

```python
# 全排列I
n = int(input())
# 思路是先排n-1的全排列
# 然后把n往n-1的全排列的每个位置里插入
# n的全排列有n!个
def permute(n):
    if n == 1:
        return [[1]]
    else:
        permutation_before = permute(n-1)
        permutation_current = []
        for i in range(len(permutation_before)):
            perm_deal_with = permutation_before[i]
            for j in range(1,len(perm_deal_with)):
                # 居然可以用这种方法连接列表！
                new_permutation = perm_deal_with[:j] + [n] + perm_deal_with[j:]
                permutation_current.append(new_permutation)
            new_permutation = perm_deal_with + [n]
            permutation_current.append(new_permutation)
            new_permutation = [n] + perm_deal_with
            permutation_current.append(new_permutation)
        permutation_current.sort()
        return permutation_current
permutations = permute(n)
for perm in permutations:
    for i in range(len(perm)-1):
        print(perm[i], end =' ')
    print(perm[-1])
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-03 01.02.40](/Users/jiangwenyi/Desktop/截屏2024-11-03 01.02.40.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

见代码注释

代码：

```python
# 拦截导弹
k = int(input())
h = list(map(int, input().split()))
# 找最长的不升序列
# 找以第i个导弹为结尾的最长不升序列，然后找这些序列中最长的一个
# 如果h[j]>=h[i]（j<i），那么第i个导弹就是可以加在以j个导弹结尾的不升序列后面的
# 称以第i个导弹结尾的最长不升序列长度为dp[i]
# 对于第i个导弹来说，总需要搜索在它之前的所有>=它的项目，然后对这些项目的dp[j]进行逐一检验，迭代dp[i]为最大的那一个
def longest(k,h):
    dp = [1] * k
    for i in range(1,k):
        for j in range(i):
            if h[j] >= h[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
print(longest(k,h))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-03 02.05.43](/Users/jiangwenyi/Desktop/截屏2024-11-03 02.05.43.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

是个“双层的”动态规划

能偷前i个物品时，最多能偷多少价值的物品

为了解决偷前i个物品时能偷的最大价值的问题，需要在能偷前i物品的情况下，假设背包最大承重为1～4时，各自能偷的最大价值（因为更大承重的背包能偷的最大价值依赖于更小承重的背包能偷的最大价值，即更新：偷还是不偷新的第i个物品价值更大）

代码：

```python
# 小偷背包
n, b = map(int, input().split())
prices = list(map(int, input().split()))
weights = list(map(int, input().split()))
dp = [[0 for _ in range(b+1)] for _ in range(n)]
# 相当于加了一个承重0磅的背包的列，为了让索引和真正的背包承重对应
for i in range(n):
    for j in range(1,b+1):
        if i == 0:
            weight_available = j
            if weights[i] <= weight_available:
                dp[i][j] = prices[i]
        else:
            weight_available = j
            if weights[i] <= weight_available:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+prices[i])
dp_max = 0
for i in range(n):
    current_row = dp[i]
    dp_max = max(dp_max,max(current_row))
print(dp_max)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-03 11.32.55](/Users/jiangwenyi/Desktop/截屏2024-11-03 11.32.55.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业题目蛮经典的，算法图解很生动，ai可以帮助我们一步一步讲解。这周每日选做到了1017。感想是，贪心算法比较符合直觉，recursion看了一下讲解后也稍微明白一点了，dp更难，特别是“双层的”dp，单层dp类似于前缀和问题，但是双层dp不看小偷背包还是比较难以理解。

每日选做进度稍微慢了点，但是有往前赶了。写代码会上瘾，这周熬了好几个两三点的夜都是因为写代码，及时反馈力量还是很强大。
