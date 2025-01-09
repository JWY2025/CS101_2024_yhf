# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：



代码：

```python
# 假币问题
# 穷举做法：因为总共24种情况（12枚硬币，轻或重）
n = int(input())
for _ in range(n):
    inp = [input().split() for _ in range(3)]
    # print(inp)

    coins = [coin for coin in 'ABCDEFGHIJKL']

    for coin in coins:
        check_light = 1
        check_heavy = 1
        for case in inp:
            left = case[0]
            right = case[1]
            state = case[2]
            if (not (coin in left and state == "down")) and (not (coin in right and state == 'up')) and (not (coin not in right and coin not in left and state == 'even')):
                check_light = 0
            if (not (coin in left and state == "up")) and (not (coin in right and state == 'down')) and (not (coin not in right and coin not in left and state == 'even')):
                check_heavy = 0

            # print(check_light,check_heavy)
        if check_light == 0 and check_heavy == 0:
            continue
        if check_light == 1:
            print(f"{coin} is the counterfeit coin and it is light.")
            break
        if check_heavy == 1:
            print(f"{coin} is the counterfeit coin and it is heavy.")
            break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-23 12.40.57](/Users/jiangwenyi/Desktop/截屏2024-12-23 12.40.57.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：



代码：

```python
r, c = map(int, input().split())
node = []       
# height of each element，并且需要加一个保护圈（四周有高地）

node.append( [100001 for _ in range(c+2)] )
for _ in range(r):
    node.append([100001] +[int(_) for _ in input().split()] + [100001])
    
node.append( [100001 for _ in range(c+2)] )
# 四个方位dx，dy
# dp用来记录每个格子开始的最长路径长（一开始都是0）
dp = [[0]*(c+2) for _ in range(r+2)]
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]
# 如果算过了ij格子，那么就不用再算一次了
def dfs(i,j):
    if dp[i][j]>0:
        return dp[i][j]
# 如果没有遍历过ij格子，那么如果ij格子四周有比它矮的格子（i+dx, j+dy），就可以往下滑，并且ij格子开始的最长路径是1+（i+dx, j+dy）格子出发的最长路径
# 递归调用dfs函数
    for k in range(4):       
        if node[i+dx[k]][j+dy[k]] < node[i][j]:
            dp[i][j] = max( dp[i][j], dfs(i+dx[k], j+dy[k])+1 )

    return dp[i][j]
# 所有格子都经历一遍，ans是其中最大的一个路径
ans = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        ans = max( ans, dfs(i,j) )
# 加一是因为，最长的坡道最后还要滑下去一格（就是算数列的长度不是算间隔的多少）
print(ans+1)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-12-23 23.39.28](/Users/jiangwenyi/Desktop/截屏2024-12-23 23.39.28.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：



代码：

```python
from collections import deque
# 读取数据
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
a = []
# a是用来记录螃蟹位置的(a[0]是左边或下面的那个格子)
for i in range(n):
    for j in range(n):
        if mat[i][j] == 5:
            a.append([i, j])
# 由于遍历的关系，后面的i，j一定不会比前面的小           
lx = a[1][0] - a[0][0]
ly = a[1][1] - a[0][1]
# 四个方向
dire = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 初始化
v = [[0] * n for i in range(n)]

# deque是一种可以快速以O(1)的时间复杂度在头部或尾部插入元素的队列
def bfs(x, y):
    # 标记螃蟹初始的位置
    v[x][y] = 1
    quene = deque([(x, y)])
    while quene:
        x, y = quene.popleft()
        # \ 表示换行继续的意思
        if (mat[x][y] == 9 and mat[x + lx][y + ly] != 1) or \
                (mat[x][y] != 1 and mat[x + lx][y + ly] == 9):
            return 'yes'
        for i in range(4):
            dx = x + dire[i][0]
            dy = y + dire[i][1]
            if 0 <= dx < n and 0 <= dy < n and 0 <= dx + lx < n \
                    and 0 <= dy + ly < n and v[dx][dy] == 0 \
                    and mat[dx][dy] != 1 and mat[dx + lx][dy + ly] != 1:
                quene.append([dx, dy])
                v[dx][dy] = 1
    return 'no'


print(bfs(a[0][0], a[0][1]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-23 23.42.18](/Users/jiangwenyi/Desktop/截屏2024-12-23 23.42.18.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：



代码：

```python
L,n,m = map(int,input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)

def check(x):
    num = 0
    now = 0
    for i in range(1, n+2):
        if rock[i] - now < x:
            num += 1
        else:
            now = rock[i]
            
    if num > m:
        return True
    else:
        return False
lo, hi = 0, L+1
ans = -1
while lo < hi:
    mid = (lo + hi) // 2
    
    if check(mid):
        hi = mid
    else:               # 返回False，有可能是num==m
        ans = mid       # 如果num==m, mid可能是答案
        lo = mid + 1
        
#print(lo-1)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-12-23 23.54.11](/Users/jiangwenyi/Desktop/截屏2024-12-23 23.54.11.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

在做每日选做，这周学到了一种方法是给答案加注释，这样能很好地帮助自己理解每一步都在干什么

每日选做现在在1124，但是中间跳掉了两题比较难的，但是现在又觉得可能没那么难，刚刚又在想

不知道有没有可能在考试前做完所有的每日选做，还有30题2天，感觉有点悬但是至少可以拼一把

cheatsheet还没开始做，想看看别人是怎么做cheatsheet的

自己感觉应该放一些常用的库，然后放一些例题



