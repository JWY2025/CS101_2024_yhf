# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```python
def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # 初始化 dp 数组
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    # 动态规划填表
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 输入
n = int(input())
# 输出结果
print(count_ways(n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-03 21.21.22](/Users/jiangwenyi/Desktop/截屏2024-12-03 21.21.22.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：



代码：

```python
def count_ways(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    
    # 初始化 dp 数组
    dp = [0] * (N + 1)
    dp[0] = 1  # 从地面开始有一种方法
    
    # 计算 dp 数组
    for i in range(1, N + 1):
        for j in range(i):
            dp[i] += dp[j]
    
    return dp[N]

# 读取输入
N = int(input().strip())

# 计算结果并输出
print(count_ways(N))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-12-03 21.13.43](/Users/jiangwenyi/Desktop/截屏2024-12-03 21.13.43.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：



代码：

```python
MOD = 1000000007
 
def precompute_dp(k, max_n):
    """
    预计算 dp 数组，其中 dp[i] 表示在第 i 天吃饭的所有可能方式。
    """
    dp = [0] * (max_n + 1)
    dp[0] = 1  # 边界条件：0 天只有一种方式（什么都不做）
 
    for i in range(1, max_n + 1):
        # 如果 i >= 1，则可以从 i-1 过渡
        dp[i] = (dp[i] + dp[i - 1]) % MOD
        # 如果 i >= k，则可以从 i-k 过渡
        if i >= k:
            dp[i] = (dp[i] + dp[i - k]) % MOD
 
    # 计算前缀和，方便快速回答区间查询
    for i in range(1, max_n + 1):
        dp[i] = (dp[i] + dp[i - 1]) % MOD
 
    return dp
 
def solve(t, k, queries):
    """
    使用预计算的 dp 数组快速解决每个查询。
    """
    # 找到查询中最大的 b 值，作为 dp 的上限
    max_n = max(b for _, b in queries)
    dp = precompute_dp(k, max_n)
 
    results = []
    for a, b in queries:
        # 使用前缀和快速计算区间结果
        result = (dp[b] - dp[a - 1]) % MOD
        results.append(result)
 
    return results
 
# 读取输入
t, k = map(int, input().split())  # t 表示查询数量，k 表示至少要间隔 k 天
queries = [tuple(map(int, input().split())) for _ in range(t)]
 
# 计算结果并输出
results = solve(t, k, queries)
for result in results:
    print(result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-03 21.32.21](/Users/jiangwenyi/Desktop/截屏2024-12-03 21.32.21.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：



代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        for i in range(len(s)):
            odd_len = self.expandAroundCenter(s, i, i)
            even_len = self.expandAroundCenter(s, i, i + 1)
            max_len = max(odd_len, even_len)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-03 22.03.17](/Users/jiangwenyi/Desktop/截屏2024-12-03 22.03.17.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

看了看正则表达式

重新开始每日选做

读了一遍学期初的讲义 发觉自己其实有一些基础trick不会，比如常用的一些list、string、set的操作，读完了觉得自己武器库里又多了一些装备
