# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>姜文宜 元培学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：



代码：

```python
def dfs(matrix, x, y, visited):
    # 检查边界条件
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == '.' or visited[x][y]:
        return 0

    # 标记当前格子为已访问
    visited[x][y] = True
    area = 1  # 当前格子算作面积1

    # 遍历周围的8个方向
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # 跳过自身
            area += dfs(matrix, x + dx, y + dy, visited)
    
    return area

def find_max_area(matrix):
    n, m = len(matrix), len(matrix[0])
    visited = [[False] * m for _ in range(n)]
    max_area = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'W' and not visited[i][j]:
                current_area = dfs(matrix, i, j, visited)
                max_area = max(max_area, current_area)

    return max_area

# 读取输入
import sys
input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    N, M = map(int, data[index:index+2])
    index += 2
    matrix = [list(data[index+i]) for i in range(N)]
    index += N
    results.append(find_max_area(matrix))

# 输出结果
print("\n".join(map(str, results)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-26 21.59.12](/Users/jiangwenyi/Desktop/截屏2024-11-26 21.59.12.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：



代码：

```python
from collections import deque

def bfs(matrix, start, target):
    m, n = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
    queue = deque([(start, 0)])  # 队列存储当前坐标和步数
    visited = set([start])  # 记录已访问过的坐标
    
    while queue:
        (x, y), steps = queue.popleft()
        
        # 如果找到了藏宝点
        if matrix[x][y] == target:
            return steps
        
        # 向四个方向尝试移动
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and matrix[nx][ny] != 2:  # 检查边界、是否已访问、是否陷阱
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    return "NO"  # 如果没有找到藏宝点

# 读取输入
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

# 起点是左上角
start = (0, 0)
target = 1  # 藏宝点

# 执行BFS并输出结果
result = bfs(matrix, start, target)
print(result)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-26 22.08.30](/Users/jiangwenyi/Desktop/截屏2024-11-26 22.08.30.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
def is_valid(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def dfs(board, x, y, move_count, visited, n, m):
    if move_count == n * m:
        return 1  # 如果已经遍历了所有的格子，则找到一条有效路径
    
    count = 0
    # 马可以走的8个方向
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n, m, visited):
            visited[nx][ny] = True
            count += dfs(board, nx, ny, move_count + 1, visited, n, m)
            visited[nx][ny] = False  # 回溯
    
    return count

def find_paths(n, m, x, y):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True  # 标记起始位置为已访问
    return dfs(None, x, y, 1, visited, n, m)

# 读取输入
import sys
input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    n, m, x, y = map(int, data[index:index+4])
    index += 4
    results.append(find_paths(n, m, x, y))

# 输出结果
print("\n".join(map(str, results)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-26 22.10.04](/Users/jiangwenyi/Desktop/截屏2024-11-26 22.10.04.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>







### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：



代码：

```python
squares = set()
i = 1
while i ** 2 < 10 ** 9:
    squares.add(i ** 2)
    i += 1
def dfs(idx):
    if idx == len(digits):
        return True

    num = 0
    for i in range(idx, len(digits)):
        num = num * 10 + digits[i]
        if num in squares:
            if dfs(i + 1):
                return True
    return False

A = int(input())
digits = list(map(int, str(A)))
if dfs(0):
    print('Yes')
else:
    print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-26 22.19.02](/Users/jiangwenyi/Desktop/截屏2024-11-26 22.19.02.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业都先给ai做一遍 让它讲讲思路。然后把标签上的东西告诉ai，让它给我分步讲讲是什么思路。感觉自己根本不如ai。



