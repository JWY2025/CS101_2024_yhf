# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

每个1应该有4条边

但是和其他1共边就会少一条边（对两个1来说都是这样）

代码：

```python
# 岛屿周长
n, m = map(int,input().split())
grid = [[0] * (m+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m+2)]

perimeter = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if grid[i][j] == 1:
            perimeter += 4 - (grid[i+1][j] + grid[i-1][j] + grid[i][j+1] + grid[i][j-1])

print(perimeter)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-19 17.37.40](/Users/jiangwenyi/Desktop/截屏2024-11-19 17.37.40.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

就是撞壁就转90度

代码：

```python

def generate_spiral_matrix(n):
    # 初始化 n×n 的矩阵
    matrix = [[0] * n for _ in range(n)]
    
    # 定义方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_idx = 0  # 当前方向的索引
    
    # 初始位置
    row, col = 0, 0
    
    # 填充矩阵
    for num in range(1, n * n + 1):
        matrix[row][col] = num
        
        # 计算下一个位置
        next_row = row + directions[direction_idx][0]
        next_col = col + directions[direction_idx][1]
        
        # 检查下一个位置是否在矩阵范围内且未被访问过
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            # 改变方向
            direction_idx = (direction_idx + 1) % 4
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]
        
        # 移动到下一个位置
        row, col = next_row, next_col
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# 读取输入
n = int(input())

# 生成螺旋矩阵
spiral_matrix = generate_spiral_matrix(n)

# 输出结果
print_matrix(spiral_matrix)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-19 23.06.02](/Users/jiangwenyi/Desktop/截屏2024-11-19 23.06.02.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：

计算每个路口投放炸弹可以清除的垃圾总数

读取的时候记得按照有垃圾的路口来读取（即，出现一个有垃圾的路口，就把这个路口周围d距离的路口加上i）

找可清除的数量最多的路口

找可清除的数量最多的路口的时候，是随时更新max，如果发现新的一个路口比max大，就把那个新的路口设为max，并且把计数归1

代码：

```python
# 垃圾炸弹
d = int(input())
n = int(input())
# 加保护圈
location = [[0 for _ in range(1024+40+1)] for _ in range(1024+40+1)]
# 读每个路口的数据，记得加20
for _ in range(n):
    x, y, k = map(int,input().split())
    x = x + 20
    y = y + 20
    for i in range(x-d,x+d+1):
        for j in range(y-d,y+d+1):
            location[i][j] += k

count = 0
max_clear = 0

for i in range(20,1024+20+1):
    for j in range(20,1024+20+1):
        if location[i][j] > max_clear:
            max_clear = location[i][j]
            count = 1
        elif location[i][j] == max_clear:
            count += 1

print(count,max_clear)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-19 17.38.53](/Users/jiangwenyi/Desktop/截屏2024-11-19 17.38.53.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

看每个元素结尾的最长序列

类似拦截导弹的dp

代码：

```python
def longest_wiggle_subsequence(nums):
    if len(nums) < 2:
        return len(nums)
    
    up = down = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    
    return max(up, down)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:n+1]))

    result = longest_wiggle_subsequence(nums)
    print(result)

main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![截屏2024-11-19 23.12.00](/Users/jiangwenyi/Desktop/截屏2024-11-19 23.12.00.png)

### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

事情总是很多，计概一拖再拖

开始尝试使用ai或者题解来学习，不再死磕，也许是会好一点吧

知道了解思路和别人写的方法，比自己硬想应该要“学习“得快一点，但是“练习”得少一些

但是权衡下来还是先这样试试看吧。



