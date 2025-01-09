# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>姜文宜 元培学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：



代码：

```python
def dfs(a,b):
    # 总定义a是多的，b是少的
    # 如果b<a<2b，那么没有操作空间，只能取b个石头，将a变成a-b
    # 达到a>=2b的状态后，谁先取谁就能获胜
    # 那么怎么算谁是达到a>=2b状态后先取的那个人呢？
    # 初始状态如果a>=2b，那么先手赢；
    # 如果初始状态不是a>=2b，那么先取一次，变成（b, a-b），成为新的初始状态。每多取一次，先后手转换一次。
    if a//b >= 2 or a == b:
        return True
    else:
        return not dfs(b, a-b)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if b>a:
        a, b = b, a

    if dfs(a,b):
        print("win")
    else:
        print('lose')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![截屏2024-12-17 23.27.54](/Users/jiangwenyi/Desktop/截屏2024-12-17 23.27.54.png)

### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：



代码：

```python
from math import ceil
n = int(input()) 
matrix = [0 for _ in range(n)] 
for i in range(n): 
    matrix[i] = [int(_) for _ in input().split()] 
ans = [0] * ceil(n/2) 
for i in range(n): 
    for j in range(n): 
        ans[min(i, j, n-1-i, n-1-j)] += matrix[i][j] 
print(max(ans))
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-12-17 23.40.58](/Users/jiangwenyi/Desktop/截屏2024-12-17 23.40.58.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

很神奇，我感觉dp好像都是储存的“某个情况下经过更新的最优解”本身，

这道题居然是储存的最大的health，而不是走到某瓶potion时能喝下的最大potions数量

dp代码提交了居然runtime error，等会儿查一查怎么回事

代码：

```python
n = int(input())
*potions, = map(int,input().split())
dp = [[-float('inf')]*(n+1) for _ in range(n+1)] # dp[走到第几瓶药][此时喝了几瓶药] = 能达到的最大健康值
dp[0][0] = 0

s = time.time()
for i in range(1,n+1):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if dp[i-1][j-1] + potions[i-1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + potions[i-1])
ans = max(j for j in range(n+1) if dp[n][j] >= 0)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：



代码：

```python
from collections import deque
import heapq
import sys

queue = deque([])
heap = []

for a in sys.stdin:
    if not a:
        break
    if a[1] == 'o' and queue:
        removed = queue.pop()
        if removed == heap[0]:
            heapq.heappop(heap)
    elif a[1] == 'u':
        n = int(a[5:])
        queue.append(n)
        if not heap or n <= heap[0]:
            heapq.heappush(heap,n)
    elif a[0] == 'm' and queue:
        print(heap[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-17 23.56.28](/Users/jiangwenyi/Desktop/截屏2024-12-17 23.56.28.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：



代码：

```python
import heapq

t = int(input())
for _ in range(t):
    grid = []
    r,c,k = map(int,input().split())
    s_found = False
    e_found = False
    for i in range(r):
        line = list(input())
        for j in range(c):
            if line[j] == '.':
                line[j] = 0
            elif not s_found and line[j] == 'S':
                xs = i
                ys = j
                s_found = True
                line[j] = 0
            elif not e_found and line[j] == 'E':
                xe = i
                ye = j
                e_found = True
                line[j] = 0
            else:
                line[j] = 1
        grid.append(line)
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heap = [(0,xs,ys)]
    inqueue = set((0,xs,ys))
    found = False
    while heap:
        d,x,y = heapq.heappop(heap)
        if (x,y) == (xe,ye):
            found = True
            break
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                nd = d+1
                if not nd % k == 0 and grid[nx][ny] == 1:
                    continue
                if (nd % k, nx, ny) in inqueue:
                    continue
                heapq.heappush(heap,(nd,nx,ny))
                inqueue.add((nd % k, nx, ny))

    if found:
        print(d)
    else:
        print('Oop!')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-17 23.57.07](/Users/jiangwenyi/Desktop/截屏2024-12-17 23.57.07.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

在赶每日选做，现在还差50多题，一天过8题，感觉有希望。

感觉看的题目多一点之后，对于dp的思路会更有理解。但是dfs和bfs还没有搞明白到底独特的优势在哪里。

这周发现了“具身认知”是真的有用。直接看题目思路和代码看不懂的时候，对着思路敲一遍代码，有的时候甚至不是自己去转化思路为python代码，而是一个模块一个模块一行行地敲题解里的代码，而不是复制粘贴，就明白许多。

如果发现自己没有办法理解为什么代码出错（找到自己和题解代码不一样的地方之后也没明白为什么自己的方式不对），可以贴给ai。但是ai往往会给很多你的代码错误的理由，其中很多都是不对的，要自己去筛选有用信息。

