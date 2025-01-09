
# 1027
# arena of greed
# 两人都要play optimally
# 当奇数时，只能取1个
# 当偶数时，为了“控场”，最优策略应该是保证对手只能取1个
# 所以，如果当前这个偶数的一半是个奇数，那么就取一半
# 如果当前这个偶数的一半是偶数，那就取一个，这样对手下一轮也只能取一个，再下一局的一半一定是个奇数
# 这其实谁先控到场谁赢
# 4是个特殊的情况，应该拿一半

# 一次性读取输入 一次性输出 可以缩短时间
# 自己写的版本是pypy3 也AC不了的
# 这是Time limit exceeded版本
# def optimize(n):
#     if n & 1 == 1:
#         return 1
#     if n & 1 == 0:
#         if n == 4:
#             return 2
#         else:
#             if (n // 2) & 1 == 1:
#                 return n // 2
#             else:
#                 return 1
#
# import sys
# input = sys.stdin.read
# # ns = [int(sys.stdin.readline().strip()) for _ in range(t)]
#
# data = input().split()
# # print(data)
# t = int(data[0])
# ns = list(map(int,data[1:]))
# # print(ns)
#
# ans = []
# for i in range(t):
#     n = ns[i]
#     original_n = n
#     self = 0
#     opponent = 0
#     if n & 1 == 1:
#         while n > 0:
#             opponent += optimize(n)
#             n -= optimize(n)
#             if n > 0:
#                 n -= 1
#         self = original_n - opponent
#         ans.append(self)
#     else:
#         while n > 0:
#             self += optimize(n)
#             n -= optimize(n)
#             if n > 0:
#                 n -= 1
#         ans.append(self)
# # print(*ans, sep='\n')
#
# print('\n'.join(map(str, ans)))
#
#
# # 这是题解pypy3能过的版本
# # 其实就是不需要调用那个optimize函数！
# import sys
# input = sys.stdin.read
#
# def solve(n):
#     f = s = 0  # To distinguish between first and second hands.
#     # fs就是先后手的标志
#     fs = True
#
#     if n & 1:
#         n -= 1
#         fs = False
#
#     while n:
#         if n == 4:
#             f += 3
#             s += 1
#             n = 0  # Special case
#         elif n == 1:
#             f += 1
#             n = 0
#         elif (n // 2) & 1:  # The First Situation
#             f += n // 2
#             s += 1
#             n = (n // 2) - 1
#         else:  # The Second Situation
#             f += 1
#             s += 1
#             n -= 2
#     ans.append([s + 1, f][fs])
#
# data = input().split()
# t = int(data[0])
# coins = list(map(int, data[1:t + 1]))
#
# ans = []
# for i in coins:
#     if i == 1:
#         ans.append(1)
#     else:
#         solve(i)
#
# print('\n'.join(map(str, ans)))
#



# 拦截导弹
# # 找最长的非递增子序列
# # 应该按“以某一个结尾”来找
# # 因为以第i个元素结尾的最长的非递增子序列有两个可能产生的方式
# # 1.可能是之前的某个非递增序列加上第i个元素形成的
# # 2.可能是i-1及之前结尾的最长的的非递增序列（也就是 加上第i个元素并不能让最长长度更新）
# def max_non_ascending(k,heights):
#     # 初始化一个dp数组
#     dp = [1] * k
#     # 找以第i个元素结尾的最长非递增序列
#     for i in range(1,k):
#         for j in range(i):
#             if heights[i] <= heights[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     # return以所有元素结尾的最长的非递增序列
#     return max(dp)
#
# k = int(input())
# heights = list(map(int, input().split()))
#
# result = max_non_ascending(k,heights)
# print(result)


# 1028
# # gold rush
# from functools import lru_cache
# @lru_cache(maxsize=None)
#
# # def dfs(n,m):
# #     if n == m:
# #         return True
# #     if n < m or n % 3 != 0:
# #         return False
# #     if dfs((n//3)*2, m):
# #         return True
# #     if dfs(n//3,m):
# #         return True
# #     # 如果上面的都不满足，那么return False（因为def里面只能出现一个return）
# #     return False
#
#
# # 这个是一样的
# def dfs(n,m):
#     if n == m:
#         return True
#     elif n < m or n % 3 != 0:
#         return False
#     elif dfs((n//3)*2, m):
#         return True
#     elif dfs(n//3,m):
#         return True
#     # 如果上面的都不满足，那么return False（因为def里面只能出现一个return）
#     else:
#         return False
#
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#
#     if dfs(n,m):
#         print("YES")
#     else:
#         print("NO")

# 数字三角形
# # 用2d list记录三角形，
# # 然后从倒数第二排开始更改，将每个数改成下面两个可以加上的数的最大和，就能往上推出最大路径。
# 从某个元素开始，最大的路径和就是它下面的路径和比较大
# n = int(input())
# tri = []   # triangle
#
# for i in range(n):
#     tri.append(list(map(int, input().split())))
# # 第i行编号是0~i(i+1个数）
# for i in range(n-2,-1,-1):
#     for j in range(i+1):
#         tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
#
# print(tri[0][0])

# 第二种解法
# 到某个元素截止，最大的路径和就是它头顶上的路径和比较大
# n = int(input())
# tri = [[0]+[int(_) for _ in input().split()]+[0] for i in range(n)]
# for i in range(1,n):
#         for key in range(1,i+2):
#                 tri[i][key] += max(tri[i-1][key-1], tri[i-1][key])
# print(max(tri[n-1]))

# 1029
# # cut ribbon
# n, a, b, c = map(int, input().split())
# dp = [0]+[float('-inf')]*n
#
# for i in range(1, n+1):
#     for j in (a, b, c):
#         if i >= j:
#             dp[i] = max(dp[i-j] + 1, dp[i])
#
# print(dp[n])

# # longest ordered sequence
# n = int(input())
# nums = list(map(int, input().split()))
# # 初始化dp数组，因为每个元素自己都能形成一个ordered sequence
# dp = [1] * n
# # 找以第i个元素结尾的元素
# for i in range(1,n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i],dp[j] + 1)
# print(max(dp))

# 1030
# # 小偷背包
# # n个物品，b个背包
# n,b = map(int,input().split())
# price = [0]+list(map(int,input().split()))
# weight = [0]+list(map(int,input().split()))
# bag = [[0] * (b+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,b+1):
#         if weight[i] <= j:
#             bag[i][j] = max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
#         else:
#             bag[i][j] = bag[i-1][j]
# print(bag[-1][-1])



# # Sereja and suffixes
# import sys
# input = sys.stdin.read
# data = input().split()
# n = int(data[0])
# m = int(data[1])
# array = list(map(int,data[2:2+n]))
# ls = list(map(int,data[2+n:]))
# # print(ls)
# tset = set()
# distinct = 0
# dp = []
# for num in reversed(array):
#     if num not in tset:
#         distinct += 1
#         tset.add(num)
#     dp.append(distinct)
# dp.reverse()
#
# ans = []
# for i in range(m):
#     l =  ls[i]
#     ans.append(dp[l-1])
# print('\n'.join(map(str,ans)))


# 需要从后往前寻找distinct numbers
# tset中存放的是从后到前的distinct number（因为set查找起来迅速）

# n,m=map(int,input().split()))
# array = list(map(int,input().split()))
# tset = set()
# distinct = 0
# dp = []
# for num in reversed(array):
#     if num not in tset:
#         distinct += 1
#         tset.add(num)
#     dp.append(distinct)
# dp.reverse()
#
# for _ in range(m):
#     l = int(input())
#     print(dp[l-1])


# 1031
# vacations
# n = int(input())
# # dp[i][0]：第i天如果rest，到第i天为止休息的最小天数
# # dp[i][1]；第i天如果contest，到第i天为止休息的嘴笑天数
# # dp[i][2]；第i天如果gym，到第i天为止休息的嘴笑天数
# dp = [[0 for _ in range(3)]] + [[float("inf")] * 3 for _ in range(n)]
# # print(dp)
# activities = list(map(int,input().split()))
# # print(activities)
# for i in range(1,n+1):
#     activity = activities[i-1]
#     if activity == 0:
#         dp[i][0] = min(dp[i-1]) + 1
#     if activity == 1:
#         dp[i][1] = min(dp[i-1][0], dp[i-1][2])
#         dp[i][0]= min(dp[i-1][0] + 1, dp[i-1][2] + 1, dp[i-1][1] + 1)
#     if activity == 2:
#         dp[i][2] = min(dp[i-1][0], dp[i-1][1])
#         dp[i][0] = min(dp[i-1][0] + 1, dp[i-1][1] + 1, dp[i-1][2] + 1)
#     if activity == 3:
#         dp[i][0] = min(dp[i-1][0]+1, dp[i-1][1]+1, dp[i-1][2]+1)
#         dp[i][1] = min(dp[i-1][0], dp[i-1][2])
#         dp[i][2] = min(dp[i-1][0], dp[i-1][1])
# print(min(dp[n]))

# # 公共子序列
#
# # dp[i][j]： x的前i个字母 & y的前j个字母 中的 最长公共子序列长度
# while True:
#     try:
#         x,y = input().split()
#     except EOFError:
#         break
#
#     xlen = len(x)
#     ylen = len(y)
#
#     # 要把第‘0’行第‘0’列设为0，因为下面需要用到dp[i-1][j]和dp[i][j-1]
#     # 这样直接从两个字符串的第一个字符开始就可以了，因为0行0列是0，所以直接加
#     dp = [[0] * (ylen+1) for _ in range(xlen+1)]
#
#     for i in range(1,xlen+1):
#         for j in range(1,ylen+1):
#             if x[i-1] == y[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
#     print(dp[-1][-1])


