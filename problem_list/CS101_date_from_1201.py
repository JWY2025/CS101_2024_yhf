# 1225
# 19岁生日礼物
# n = int(input())
# for _ in range(n):
#     s = input()
#     if '19' in s:
#         print("Yes")
#         continue
#     if int(s) % 19 == 0:
#         print("Yes")
#         continue
#     print("No")

# 1202
# 最长公共子序列
# 动态规划
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         len1 = len(text1)
#         len2 = len(text2)
#         # dp[i][j]：text1的前i个字符和text2的前j个字符的最长公共子序列
#         dp = [[0] * (len2+1) for _ in range(len1+1)]
#         for i in range(1,len1+1):
#             for j in range(1,len2+1):
#                 # 第i个字符的索引是i-1
#                 ind_i = i-1
#                 ind_j = j-1
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#                 if text1[ind_i] == text2[ind_j]:
#                     dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])
#         return dp[-1][-1]

# # 1201
# # 放苹果
# t = int(input())
# for _ in range(t):
#     m,n = map(int,input().split())
#     # 0~n列，0～m行
#     # dp[i][j]：i个果子分到j个盘子里的方法数
#     dp = [[0] * (n+1) for _ in range(m+1)]
#
#     # 0个果子分配到1～n个盘子里，都是1种分法
#     dp[0] = [0] + [1] * n
#
#     # 1～m个果子分到0个盘子里，都是0种分法
#     for k in range(1,m+1):
#         dp[k][0] = 0
#
#
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             # 如果果子大于盘子
#             if i >= j:
#                 # 果多盘少，i个果分j个盘 = 每个盘里至少有一个果 + 至少有一个盘没有果
#                 dp[i][j] = dp[i - j][j] + dp[i][j - 1]
#             # 如果果子小于盘子
#             else:
#                 # 盘多果少，只会用到前i个盘子
#                 dp[i][j] = dp[i][i]
#     print(dp[m][n])

# dfs（递归）好理解
# def count_ways(m, n):
#     # 如果只有一个盘子，只能有一种分法
#     if n == 1:
#         return 1
#     # 如果苹果数为0，只有一种分法：所有盘子空
#     if m == 0:
#         return 1
#     # 如果盘子数大于苹果数，最多只需用前m个盘子分苹果
#     if n > m:
#         return count_ways(m, m)
#     # 分为两种情况：至少每个盘子放一个苹果；有盘子空着
#     return count_ways(m, n - 1) + count_ways(m - n, n)

#
# t = int(input())  # 测试数据数目
# results = []
# for _ in range(t):
#     m, n = map(int, input().split())
#     results.append(count_ways(m, n))
# # 输出结果
# for res in results:
#     print(res)

# 1204
# 快速堆猪
# from collections import deque
# import heapq
# import sys
#
# queue = deque([])
# heap = []
#
# for a in sys.stdin:
#     if not a:
#         break
#     if a[1] == 'o' and queue:
#         removed = queue.pop()
#         if removed == heap[0]:
#             heapq.heappop(heap)
#     elif a[1] == 'u':
#         n = int(a[5:])
#         queue.append(n)
#         # 只有被更新的最小值会被push入heap中
#         # 这里使用了短路求值特性，也就是说如果not heap是False(heap 是空的)，那么就不会求 heap[0]
#         # 有两种情况会加入元素：heap为空，或者n比原来的最小值小
#         if not heap or n <= heap[0]:
#             heapq.heappush(heap,n)
#     elif a[0] == 'm' and queue:
#         print(heap[0])

# 1203
# 编辑距离
# https://leetcode.cn/problems/edit-distance/solutions/188223/bian-ji-ju-chi-by-leetcode-solution/
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n = len(word1)
#         m = len(word2)
#
#         # 有一个字符串为空串
#         if n * m == 0:
#             return n + m
#
#         # DP 数组
#         D = [[0] * (m + 1) for _ in range(n + 1)]
#
#         # 边界状态初始化
#         # word2空/word1空，那么编辑距离就是另外一个word字串的长度
#         for i in range(n + 1):
#             D[i][0] = i
#         for j in range(m + 1):
#             D[0][j] = j
#
#         # 因为对称性，其实只有三种操作：在A中加入一个字符/在B中加入一个字符/A替换一个字符
#         # 计算所有 DP 值
#         # dp[i][j]：word1的前i个字符 和 word2的前j个字符 变成一样需要的编辑距离
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 # A中加一个字符
#                 left = D[i - 1][j] + 1
#                 # B加一个字符
#                 down = D[i][j - 1] + 1
#                 # A中替换一个字符（如果本来两个字符就是一样的，那么不用加一步；如果两个字符不一样，那么要加一步）
#                 left_down = D[i - 1][j - 1]
#                 if word1[i - 1] != word2[j - 1]:
#                     left_down += 1
#                 D[i][j] = min(left, down, left_down)
#
#         return D[n][m]

# 1205
# 走山路
# Dijkstra算法：找有权图两点间的最短距离
# # 371ms
# import heapq
# # n*m 的矩阵，p个test
# n, m, p = map(int, input().split())
# mat = [list(input().split()) for _ in range(n)]
# directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
# anns = []
# for _ in range(p):
#     ans = 'NO'
#     x, y, xx, yy = map(int, input().split())
#
#     if mat[x][y] != '#' and mat[xx][yy] != '#':
#         # 使用一个字典来记录到达每个节点的最小消耗
#         dist = {(x, y): 0}
#         q = [(0, x, y)]  # (当前消耗, 当前行, 当前列)
#
#         while q:
#             s, i, j = heapq.heappop(q)
#
#             # 如果到达目标点，输出最小消耗
#             if i == xx and j == yy:
#                 ans = s
#                 break
#
#             # 扩展四个方向
#             for a, b in directions:
#                 ii, jj = i + a, j + b
#                 if 0 <= ii < n and 0 <= jj < m and mat[ii][jj] != '#':
#                     cost = s + abs(int(mat[ii][jj]) - int(mat[i][j]))
#
#                     # 如果找到更优路径，则更新距离并推入堆中
#                     if (ii, jj) not in dist or cost < dist[(ii, jj)]:
#                         dist[(ii, jj)] = cost
#                         heapq.heappush(q, (cost, ii, jj))
#
#     anns.append(ans)
#
# for _ in anns:
#     print(_)

# 174ms
# # 特别标准的dijkstra写法
# import heapq
# m, n, p = map(int, input().split())
# info = []
# for _ in range(m):
#     info.append(list(input().split()))
# directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#
# def dijkstra(start_r, start_c, end_r, end_c):
#     pos = []
#     dist = [[float('inf')] * n for _ in range(m)]
#     if info[start_r][start_c] == '#':
#         return 'NO'
#     dist[start_r][start_c] = 0
#     heapq.heappush(pos, (0, start_r, start_c))
#     while pos:
#         d, r, c = heapq.heappop(pos)
#         if r == end_r and c == end_c:
#             return d
#         # h是现在的高度
#         h = int(info[r][c])
#         for dr, dc in directions:
#             nr = r + dr
#             nc = c + dc
#             if 0 <= nr < m and 0 <= nc < n and info[nr][nc] != '#':
#                 if dist[nr][nc] > d + abs(int(info[nr][nc]) - h):
#                     dist[nr][nc] = d + abs(int(info[nr][nc]) - h)
#                     heapq.heappush(pos, (dist[nr][nc], nr, nc))
#     return 'NO'
#
# for _ in range(p):
#     x, y, z, w = map(int, input().split())
#     print(dijkstra(x, y,z,w))

# 1206
# 水淹七军
# bfs解法
# from collections import deque
# import sys
# input = sys.stdin.read
#
# # 判断坐标是否有效
# def is_valid(x, y, m, n):
#     return 0 <= x < m and 0 <= y < n
#
# # 广度优先搜索模拟水流
# def bfs(start_x, start_y, start_height, m, n, h, water_height):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     q = deque([(start_x, start_y, start_height)])
#     water_height[start_x][start_y] = start_height
#
#     while q:
#         x, y, height = q.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if is_valid(nx, ny, m, n) and h[nx][ny] < height:
#                 if water_height[nx][ny] < height:
#                     water_height[nx][ny] = height
#                     q.append((nx, ny, height))
#
# # 主函数
# def main():
#     data = input().split()  # 快速读取所有输入数据
#     idx = 0
#     k = int(data[idx])
#     idx += 1
#     results = []
#
#     for _ in range(k):
#         m, n = map(int, data[idx:idx + 2])
#         idx += 2
#         h = []
#         for i in range(m):
#             h.append(list(map(int, data[idx:idx + n])))
#             idx += n
#         water_height = [[0] * n for _ in range(m)]
#
#         i, j = map(int, data[idx:idx + 2])
#         idx += 2
#         i, j = i - 1, j - 1
#
#         p = int(data[idx])
#         idx += 1
#
#         for _ in range(p):
#             x, y = map(int, data[idx:idx + 2])
#             idx += 2
#             x, y = x - 1, y - 1
#             if h[x][y] <= h[i][j]:
#                 continue
#             bfs(x, y, h[x][y], m, n, h, water_height)
#
#         results.append("Yes" if water_height[i][j] > 0 else "No")
#
#     sys.stdout.write("\n".join(results) + "\n")
#
# if __name__ == "__main__":
#     main()
#
# # dfs解法
# import sys
#
# sys.setrecursionlimit(300000)
# input = sys.stdin.read
#
#
# # 判断坐标是否有效
# def is_valid(x, y, m, n):
#     return 0 <= x < m and 0 <= y < n
#
#
# # 深度优先搜索模拟水流
# def dfs(x, y, water_height_value, m, n, h, water_height):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if is_valid(nx, ny, m, n) and h[nx][ny] < water_height_value:
#             if water_height[nx][ny] < water_height_value:
#                 water_height[x][y] = water_height_value
#                 dfs(nx, ny, water_height_value, m, n, h, water_height)
#
#
# # 主函数
# def main():
#     data = input().split()  # 快速读取所有输入数据
#     idx = 0
#     k = int(data[idx])
#     idx += 1
#     results = []
#
#     for _ in range(k):
#         m, n = map(int, data[idx:idx + 2])
#         idx += 2
#         h = []
#         for i in range(m):
#             h.append(list(map(int, data[idx:idx + n])))
#             idx += n
#         water_height = [[0] * n for _ in range(m)]
#
#         i, j = map(int, data[idx:idx + 2])
#         idx += 2
#         i, j = i - 1, j - 1
#
#         p = int(data[idx])
#         idx += 1
#
#         for _ in range(p):
#             x, y = map(int, data[idx:idx + 2])
#             idx += 2
#             x, y = x - 1, y - 1
#             if h[x][y] <= h[i][j]:
#                 continue
#
#             dfs(x, y, h[x][y], m, n, h, water_height)
#
#         results.append("Yes" if water_height[i][j] > 0 else "No")
#
#     sys.stdout.write("\n".join(results) + "\n")
#
#
# if __name__ == "__main__":
#     main()

# 1209
# potions(easy version)
# 建一个heap，heap最顶是最小的，也就是说如果有负的，最负的那个在堆顶
# 先使劲喝药，碰到一个喝一个，如果喝到负的就把最负的那个药吐出来(也就是相当于当时不喝那瓶药)
#
# 也就是，如果某刻被毒药毒死了，就看之前是否喝了更“不值”（毒性更大）的毒药，如果是，就不喝之前那个了。之前少喝一个肯定死不了。
# import heapq
#
# #处理输入,初始化
# n=int(input())
# potions=list(map(int,input().split()))
# health=0
# h=[]#小顶堆
#
# #dp
# for p in potions:
#     heapq.heappush(h,p)
#     health+=p
#     if health<0:
#         health-=heapq.heappop(h)
#
# #输出
# print(len(h))

# 1217
# 剪绳子
# 相当于把整个过程倒过来变为缝绳子，反正我们知道结束的时候肯定是L1L2...LN这些长度的N段绳子
n = int(input())
a = list(map(int, input().split()))
import heapq
heapq.heapify(a)
ans = 0
# 每次选择两段最短的绳子进行合并，这样的策略可以保证在每一步都尽可能地减少当前步骤的开销，从而达到全局最优解。
# 剪n-1下（缝n-1下）
for i in range(n-1):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    z = x + y
    heapq.heappush(a, z)
    ans += z
print(ans)

# 1223
# in love
'''
The claim is that if the answer exists, we can take the segment with 
the minimum right boundary and the maximum left boundary 
(let's denote these boundaries as 𝑟 and 𝑙). Therefore, if 𝑟<𝑙
, it is obvious that this pair of segments is suitable for us. 
Otherwise, all pairs of segments intersect because they have common 
points in the range 𝑙…𝑟.

先写了个超时的算法，然后看tutorial及其他人引入dict, heap的代码。
按照区间右端点从小到大排序。从前往后依次枚举每个区间。
假设当前遍历到的区间为第i个区间 [li, ri]，如果有li > ed，
说明当前区间与前面没有交集。
'''

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

minH = []
maxH = []
'''
defaultdict 的特别之处在于当访问一个不存在的键时，它会自动创建该键，并赋予默认值，这个默认值的类型由你在创建 defaultdict 时指定。

当你使用 defaultdict(int) 时，你实际上是在创建一个 defaultdict 对象，它会在遇到不存在的键时返回整数类型的默认值 0。

这是因为 int 类型在不带参数调用时（即 int()）会生成 0。
'''
ldict = defaultdict(int)
rdict = defaultdict(int)

n = int(input())

for _ in range(n):
    op, l, r = map(str, input().strip().split())
    l, r = int(l), int(r)
    if op == "+":
        ldict[l] += 1
        rdict[r] += 1
        # minH: 上界小顶堆
        # maxH：下界大顶堆
        heapq.heappush(maxH, -l)
        heapq.heappush(minH, r)
    else:
        ldict[l] -= 1
        rdict[r] -= 1

    '''
    使用 while 循环，将最大堆 maxH 和最小堆 minH 中出现次数为 0 的边界移除。
    通过比较堆顶元素的出现次数，如果出现次数为 0，则通过 heappop 方法将其从堆中移除。
    '''
    while len(maxH) > 0 >= ldict[-maxH[0]]:
        heapq.heappop(maxH)
    while len(minH) > 0 >= rdict[minH[0]]:
        heapq.heappop(minH)

    '''
    判断堆 maxH 和 minH 是否非空，并且最小堆 minH 的堆顶元素是否小于
    最大堆 maxH 的堆顶元素的相反数。
    '''
    if len(maxH) > 0 and len(minH) > 0 and minH[0] < -maxH[0]:
        print("Yes")
    else:
        print("No")
