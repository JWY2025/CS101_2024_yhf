# # 数的划分
# # dfs解法
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def separate(n,k):
#     if k > n:
#         return 0
#     if k == n:
#         return 1
#     if k == 1:
#         return 1
#     if n == 1:
#         return 1
#     # 如果划分出来的每个整数都大于1，那么就是separate(n-k, k)，相当于往每个盘子里先放一个苹果，然后再放剩下的n-k个苹果
#     # 如果划分出来有至少一个1，那么就是separate(n-1, k-1)，相当于先拿走一个1，然后将剩下的n-1个苹果分成k-1份
#     return separate(n-1,k-1) + separate(n-k,k)
# n, k = map(int,input().split())
# print(separate(n,k))

# 数的划分
# dp解法
# n, k = map(int, input().split())
# dp = [[0] * (k+1) for _ in range(n+1)]
# # dp[i][j]: 把i分为j份
# for i in range(1,min(n+1,k+1)):
#     dp[i][i] = 1
#
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if i > j:
#             dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
#
# print(dp[n][k])


# 定义栈的相关操作
# top = -1  # 栈顶位置
#
# def push(a, elem):
#     global top
#     # 压栈
#     a.append(elem)
#     top += 1
#
# def pop(a):
#     global top
#     # 出栈
#     if top == -1:
#         return
#     top -= 1
#
# def visit(a):
#     # 访问栈顶
#     if top != -1:
#         return a[top]
#     else:
#         return ' '  # 在栈为空时返回一个空格
#
# if __name__ == '__main__':
#     a = []
#     s = input()
#     length = len(s)
#
#     for i in range(length):
#         if s[i] == '(':
#             push(a, s[i])
#         else:
#             if s[i] == ')':
#                 if visit(a) == '(':
#                     pop(a)
#                 else:
#                     print("False at %d" % i)
#                     exit(0)
#
#     if top == -1:
#         print("True")
#     else:
#         print("False at %d" % i)

# def match(s, p):
#     n1 = len(s)
#     n2 = len(p)
#     i = 0
#     while i <= n1 - n2:
#         j = 0
#         while j < n2 and s[i+j] == p[j]:   # 【1】
#             j += 1
#         if j == n2:     # 【2】
#             return i
#         i += 1
#     return -1
#
# s = input()
# p = input()
# lenp = len(p)
# i = 0
# j = match(s, p)   # 【3】
# while j >= 0:
#     print(i + j, end=" ") # 【4】
#     i += j + lenp    # 【5】
#     j = match(s[i:], p)
#
# n = int(input())
# if n >= 1000:
#     print("输入的整数n必须小于1000")
# else:
#     nums = {}
#     for _ in range(n):
#         num = int(input())
#         if num in nums:
#             nums[num] += 1
#         else:
#             nums[num] = 1
#     count = 0
#     for num in nums:
#         if nums[num] == 1:
#             count += 1
#     print(f"不重复的整数数量是{count}")

# n, m = map(int,input().split())
# nums = {}
# for _ in range(n):
#     num = int(input())
#     if num in nums:
#         nums[num] += 1
#     else:
#         nums[num] = 1
# count = 0
# for num in nums:
#     if nums[num] > m:
#         count += 1
# print(count)

# m = [float(x) for x in input().split()]
#
# a = b = c = d = 0
# n = int(m[0])
# for i in range(1, n + 1):
#     c += m[i]
#     if i == 1:
#         a = b = m[i]
#     else:
#         if a < m[i]:
#             a = m[i]
#         if b > m[i]:
#             b = m[i]
# c /= n
# for i in range(1, n + 1):
#     d += (m[i] - c) * (m[i] - c)
# d /= n
#
# print(f"{a:.2f} {b:.2f} {c:.2f} {d:.2f}")


### 2、长整数整除问题：
'''
以字符串形式输入一个不超过 10000 位的正整数（超出 int 表示范围），判断其是否能被 22 整除， 能则输出"YES”，否则输出“NO”。
如果字符串中出现非数字字符，输出“Invalid input!”。请补充完善程序。
提示：
1: 语句 s = input() 表示读入字符串 s
2: 函数 len(s) 返回值为字符串 s 的长度
3: 字符 '0'~'9' 的 ASCII 码分别为 48 ~ 57
4: 整数被 11 整除当且仅当奇数位之和与偶数位之和的差被 11 整除。例如：
	13915 = 11 * 1265 --> (1+9+5)-(3+1)=11 --> 能被 11 整除
	465362 = 11 * 42305 + 7 --> (4+5+6)-(6+3+2)=4 --> 不能被 11 整除
5: 整数被 22 整除当且仅当同时被 2 和 11 整除
'''

# n = int(input())
# nums = []
# prefix_sums = [0]
# for _ in range(n):
#     prefix_sums.append(prefix_sums[-1] + int(input()))
# s_max = 0
# for i in range(1,n+1):
#     for j in range(i):
#         s = prefix_sums[i] - prefix_sums[j]
#         s_max = max(s,s_max)
# print(s_max)

# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))
# max_sum = current_sum = 0
# # 每个num都有两种选择：要么加入之前的子数组，要么自己开始一个新的子数组
# # 如果加入之前的子数组比自己开始一个新的子数组要优，那么就加入之前的子数组；否则自己开始一个新的子数组
# # max_sum是一个实时更新的量，用来保存至今为止最大的sum，不论当前num到底加入之前的子数组还是自己开始一个新的子数组
# for i in range(n):
#     num = nums[i]
#     if current_sum + num >= num:
#         max_sum = max(current_sum, max_sum)
#         current_sum += num
#     else:
#         max_sum = max(current_sum, max_sum)
#         current_sum = num
# max_sum = max(max_sum, current_sum)
# print(max_sum)

print(ord("9"))