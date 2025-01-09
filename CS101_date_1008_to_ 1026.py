# 以下1008
# # 数字方格
# n = int(input())
# # 0 <= a1，a2，a3 <= 0
# # a1 + a2 被 2 整除
# # a2 + a3 被 3 整除
# # a1 + a2 + a3 被5整除
# m = []
# for a1 in range(n,-1,-1):
#     for a2 in range(n,-1,-1):
#         for a3 in range(n,-1,-1):
#             if (a1 + a2 + a3) % 5 == 0 and (a1 + a2) % 2 == 0 and (a2 + a3) % 3 == 0:
#                 m.append(a1 + a2 + a3)
# print(max(m))
import math
from os.path import split
from sys import prefix

# # 双向喜欢
# # n个人，q组单项喜欢关系
# n, q = map(int, input().split())
# # x, y = 喜欢别人，被喜欢
# x, y = [0] * q, [0] * q
# flag = 0
# for i in range(q):
#     x[i], y[i] = map(int, input().split())
# for i in range(q):
#     for j in range(q):
#         if x[i] == y[j] and x[j] == y[i]:
#             print("Yes")
#             flag = 1
#             break
#     if flag == 1:
#         break
# if flag == 0:
#     print("No")

# 以下1009

# # 三方喜欢
# # # n个人，q组单项喜欢关系
# n, q = map(int, input().split())
# # # x, y = 喜欢别人，被喜欢
# x, y = [0] * q, [0] * q
#
# flag = 0
#
# for i in range(q):
#     x[i], y[i] = map(int, input().split())
# flag = 0
#
# people = set(x)
# # print(people)
# dict = {}
#
# for person in people:
#     loved = []
#     for i in range(q):
#         if x[i] == person:
#             loved.append(y[i])
#     dict[person] = loved
#
# # print(dict)
#
# for a in people:
#     loved_a = dict.get(a)
#     for b in loved_a:
#         loved_b = dict.get(b,"none")
#         if loved_b != 'none':
#             for c in loved_b:
#                 loved_c = dict.get(c,'none')
#                 if loved_c != 'none':
#                     if a in loved_c:
#                         print("Yes")
#                         flag = 1
#                         break
#         if flag == 1:
#             break
#     if flag == 1:
#         break
# if flag == 0:
#     print("No")

# # 生理周期
# # p, e, i : 体力高峰，感情高峰，智力高峰
# # p, e, i 周期为 23，28, 33
# case = 0
# while True:
#     p, e, i, d = map(int, input().split())
#     import math
#     # all函数用于判断某个迭代器（eg 列表，元组，集合等）是否每个元素都为真
#     # while not all(x== -1 for x in [p,e,i,d]):
#     if p + e + i + d != -4:
#
#         #  先把p、e、i变成d之后第一次出现peak的天数（按照当年的的一天开始计算）
#         if p < d:
#             x = math.ceil((d - p) / 23)
#             p = p + 23*x
#         else:
#             x = math.floor((p - d) / 23)
#             p = p - 23*x
#
#         if e < d:
#             y = math.ceil((d - e) / 28)
#             e = e + 28*y
#         else:
#             y = math.floor((e - d) / 28)
#             e = e - 28*y
#
#         if i < d:
#             z = math.ceil((d - i) / 33)
#             i = i + 33*z
#         else:
#             z = math.floor((i - d) / 33)
#             i = i - 33*z
#
#         # print(p,e,i)
#
#         for x in range(1, math.ceil(21253/23) + 1):
#             if (p + 23*x - e) % 28 == 0 and (p + 23*x - i) % 33 == 0:
#                 day = p + 23*x
#                 case += 1
#                 print(f"Case {case}: the next triple peak occurs in {day-d} days.")
#                 break
#     else:
#         break

# 以下1010
# # 一〇交错
# s = list(input())
# s = list(map(int,s))
# n = len(s)
# count = 0
# count_max = 0
# for i in range(n-1):
#     if s[i] + s[i+1] == 1:
#         count += 1
#     else:
#         count_max = max(count_max,count+1)
#         count = 0
# count_max = max(count_max,count+1)
# print(count_max)

# # 进程检测
# # k组测试输入
# k = int(input())
# # 定义一个取并集用的函数
# # def union_set(*sets):
# #     return set.union(*sets)
#
# for _ in range(k):
#     # n个进程
#     n = int(input())
#
#     s = [0] * n
#     d = [0] * n
#     intervals = [[]] * n
#
#     for i in range(n):
#         s[i], d[i] = map(int,input().split())
#         intervals[i] = (s[i],d[i])
#
#     intervals.sort(key = lambda x : x[1])
#     tests = 0
#     while True:
#         if len(intervals) == 0:
#             break
#         # elif len(intervals) == 1:
#         #     tests += 1
#         #     break
#         else:
#             d = intervals[0][1]
#
#             # x存的是s比当前d小的所有interval，之后要剔除掉
#             x = [interval for interval in intervals if interval[0] <= d]
#             # intervals现在存的是intervals剔除掉x之后剩下的intervals
#             intervals = [interval for interval in intervals if interval not in x]
#             tests += 1
#
#     print(tests)

# # 以下1011
# # 四面楚歌
# n, m = map(int, input().split())
# matrix = [ [] for _ in range(n)]
# max_num = 0
# for i in range(n):
#     matrix[i] =  list(map(int, input().split()))
# for i in range(n):
#     for j in range(m):
#         x = matrix[i][j]
#         A = matrix[0][j]
#         B = matrix[i][m-1]
#         C = matrix[n-1][j]
#         D = matrix[i][0]
#         ABCD = 1000 * A + 100 * B + 10 * C + D
#         num = x * ABCD
#         max_num = max(max_num, num)
# print(max_num)

# # 二维矩阵上的卷积运算
# # m，n：行，列
# # p，q：行，列
# m, n, p, q = map(int, input().split())
#
# matrix = [[] for _ in range(m)]
# convolution = [[] for _ in range(p)]
# result = [[0 for _ in range(n+1-q)] for _ in range(m+1-p)]
#
# for i in range(m):
#     matrix[i] = list(map(int, input().split()))
# for i in range(p):
#     convolution[i] = list(map(int, input().split()))
#
# current_row = 0
# current_col = 0
#
# current_result_row = 0
# current_result_col = 0
#
# while current_row < m-p+1:
#     while current_col < n-q+1:
#         current_matrix = matrix[current_row:current_row + p]
#         for i in range(p):
#             current_matrix[i] = current_matrix[i][current_col:current_col+q]
#
#         for i in range(p):
#             for j in range(q):
#                 result[current_result_row][current_result_col] += current_matrix[i][j] * convolution[i][j]
#
#         current_col += 1
#         current_result_col += 1
#     current_col = 0
#     current_result_col = 0
#     current_row += 1
#     current_result_row += 1
# for i in range(m-p+1):
#     for j in range(n-q+1):
#         print(result[i][j], end=' ')
#     print()

# 以下1012
# # 军备竞赛
# # p：起始经费
# p = int(input())
# # costs：每张图的制作成本，同时也是卖价
# costs = list(map(int, input().split()))
# costs.sort()
# n = len(costs)
#
# # 制造低价的武器，如果没钱，卖出高价的武器
# # 双指针，i从低价往高价，j从高价往低价
# # 指针指在 i，j 上时，自己拥有的是 i 个武器，敌国拥有的是 n - j  个武器
#
# # 如果有足够的武器，卖一个武器一定能买至少一个武器
# # 剩下最后一个武器的时候，能造就造，造不起也不要卖
# i, j = 0, n-1
# own = 0
# enemy = 0
# # 第一个图必须得造，如果不能造那么就直接结束
# if costs[0] <= p:
#     p -= costs[0]
#     i = 1
#     own += 1
#
#     while i < j:
#         if costs[i] <= p:
#             p -= costs[i]
#             i += 1
#             own += 1
#
#         else:
#             p += costs[j]
#             j -= 1
#             enemy += 1
#
#     # 这里出了while i < j 的循环
#     if costs[i] <= p:
#         own += 1
#         print(own-enemy)
#     else:
#         print(own-enemy)
# else:
#     print(0)

# # 序列合并
# n, m = map(int,input().split())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# for x in B:
#     A.append(x)
# A.sort()
# for i in range(n+m-1):
#     print(A[i],end = ' ')
# print(A[-1])

# # 以下1013
# # 因材施教
# n, m = map(int, input().split())
# r = list(map(int, input().split()))
# r.sort()
# diff = []
# for i in range(n-1):
#     diff.append(r[i+1]-r[i])
# # m个班，n个人
# # 先放n个人 一人一个班
# # 然后剩下的n-m个人必须放到已经有其他人在的班里
# # 每个班级的差异都是几个相邻的人的差异加起来
# # 所以前后作差，共有n-1个差
# # 找出最小的n-m个差，就让这几个差成为某些班级的差异
# # 这n-m个差的和就是哦那最小的总体差异
# diff.sort()
# print(sum(diff[:n-m]))

# # 2-sum-双指针
# n, k = map(int,input().split())
# A = list(map(int,input().split()))
# i, j = 0, n-1
# count = 0
# while i < j:
#     if A[i] + A[j] == k:
#         count += 1
#         i += 1
#         j -= 1
#     elif A[i] + A[j] > k:
#         j -= 1
#     else:
#         i += 1
# print(count)

# # 以下是1014
# # taxi
# n = int(input())
# s = list(map(int, input().split()))
# four = [x for x in s if x == 4]
# three = [x for x in s if x == 3]
# two = [x for x in s if x == 2]
# one = [x for x in s if x == 1]
# taxi = len(four)
# taxi += len(three)
# import math
# taxi += math.ceil(len(two)/2)
# rest = len(three) + 2*(math.ceil(len(two)/2) - math.floor(len(two)/2))
# if len(one)<= rest:
#     print(taxi)
# else:
#     taxi += math.ceil((len(one) - rest)/4)
#     print(taxi)

# # saruman's army
# while True:
#     r, n = map(int, input().split())
#     if r + n == -2:
#         break
#     else:
#         x = list(map(int, input().split()))
#         x.sort()
#
#         current_diff = 0
#         count = 0
#
#     while len(x) > 0:
#         while len(x) > 1:
#             diff = x[1] - x[0]
#             if current_diff + diff <= r:
#                 current_diff += diff
#                 x.pop(0)
#             else:
#                 count += 1
#                 current_diff = 0
#                 break
#
#         if len(x) == 1:
#             print(count + 1)
#             break
#
#         while len(x) > 1:
#             diff = x[1] - x[0]
#             if current_diff + diff <= r:
#                 current_diff += diff
#                 x.pop(0)
#             else:
#                 current_diff = 0
#                 x.pop(0)
#                 break
#
#         if len(x) == 1:
#             if current_diff > 0:
#                 print(count)
#             else:
#                 print(count+1)
#             break

# # 以下是1015
# # interesting drink
# n = int(input())
# x = list(map(int, input().split()))
# x.sort()
# q = int(input())
#
# # 二分查找
# for _ in range(q):
#     m = int(input())
#     left = 0
#     right = n - 1
#
#     while left < right:
#         mid = (left + right)//2
#         if m >= x[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     # print(left,right)
#     if m >= x[left]:
#         drinks = left + 1
#     else:
#         drinks = left
#
#     print(drinks)

# 冲刺GPA的贪心之路
# h = int(input())
# m = int(input())
# pair = [[] for _ in range(m)]
# pair的每个集合为
# s：期望提高的分数,
# c：学分,
# s*c：“学分积”,
# 5/s：最多花多少小时复习
# for i in range(m):
#     s, c = map(float,input().split())
#     pair[i] = [s,c]
#     pair[i].append(s*c)
#     pair[i].append(5/s)
# pair.sort(key = lambda x:x[2], reverse = True)
# # print(pair)
# h = 2*h - 0.5 * m
# current = 0
# # 写法一
# end = 0
# while h - pair[0][3] >= 0:
#     h -= pair[0][3]
#     current += 5 * pair[0][1]
#     pair.pop(0)
#     if len(pair) == 0:
#         end = 1
#         break
# if end == 1:
#     print(f"{current:.1f}")
# else:
#     if h > 0:
#         current += h * pair[0][2]
#         print(f"{current:.1f}")

# # 写法二
# for lesson in pair:
#     if h - lesson[3] >= 0:
#         h -= lesson[3]
#         current += lesson[1] * 5
#     else:
#         if h > 0:
#             current += lesson[2] * h
#             break
# print(f"{current:.1f}")

# 以下是1016
# # XXXXX
# t = int(input())
# for _ in range(t):
#     n, x = map(int, input().split())
# #   n: number of elements in the array a
# #   x: the number Ehab hates
#     a = list(map(int, input().split()))
#     reversed_a = list(reversed(a))
#     # print(reversed_a)
#     a_sum_mod = sum(a) % x
# #   print(a_sum_mod)
#     current_length = n
#     if not a_sum_mod % x == 0:
#         print(current_length)
#     else:
#         flag = 0
#         for element in a:
#             if element % x == 0:
#                 current_length -= 1
#             else:
#                 length_begin = current_length - 1
#                 flag = 1
#                 # print(length_begin)
#                 break
#         current_length = n
#
#         if flag == 1:
#             for element in reversed_a:
#                 # print(element)
#                 if element % x == 0:
#                     current_length -= 1
#                     # print(current_length)
#                 else:
#                     length_end = current_length - 1
#                     print(max(length_begin, length_end))
#                     break
#         else:
#             print(-1)

# # 生存游戏
# n, m = map(int, input().split())
# cells = [[0 for _ in range(m+2)] for _ in range(n+2)]
# cells_new = [[0 for _ in range(m+2)] for _ in range(n+2)]
# # 加了一圈保护圈
# for i in range(1,n+1):
#     current_row = list(map(int, input().split()))
#     cells[i][1:m+1]  = current_row
#     cells_new[i][1:m+1] = current_row
#
# for row in range(1,n+1):
#     for col in range(1,m+1):
#         sum_around = cells[row-1][col] + cells[row+1][col] + cells[row][col-1] + cells[row][col+1] + cells[row-1][col-1] + cells[row-1][col+1] + cells[row+1][col-1] + cells[row+1][col+1]
#         if cells[row][col] == 1:
#             if sum_around < 2:
#                 cells_new[row][col] = 0
#             # elif sum_around == 2 or sum_around == 3:
#             #     cells[row][col] = 1
#             elif sum_around > 3:
#                 cells_new[row][col] = 0
#         else:
#             if sum_around == 3:
#                 cells_new[row][col] = 1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(cells_new[i][j],end=" ")
#     print()

# 以下是1017
# # bomb game
# a,b,k = map(int,input().split())
# hits = 0
# # 加保护圈
# # 最后只看中间的那一圈
# fields = [[1 for _ in range(49*2+b)] for _ in range(49*2+a)]
# for _ in range(k):
#     r,s,p,t = map(int,input().split())
#     half_p = (p-1)//2
#     row = r + 48
#     col = s + 48
#
#     if p > 2:
#         if t == 1:
#             hits += 1
#             for i in range(row-half_p, row+half_p+1):
#                 for j in range(col-half_p, col+half_p+1):
#                     fields[i][j] += 1
#
#         else:
#             for i in range(row-half_p, row+half_p+1):
#                 for j in range(col-half_p, col+half_p+1):
#                     fields[i][j] = 0
#
#     else:
#         if t == 1:
#             hits += 1
#             fields[row][col] += 1
#
#         else:
#             fields[row][col] = 0
#
# fields = fields[49:49+a][:]
#
# for i in range(a):
#     fields[i] = fields[i][49:49+b]
#
# possible = 0
#
# for row in fields:
#     for item in row:
#         if item == hits+1:
#             possible += 1
#
# print(possible)

# # 2048 game
# q = int(input())
# for _ in range(q):
#     flag = 0
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     numbers = [number for number in numbers if number <= 2048]
#     if sum(numbers) >= 2048:
#         print("YES")
#     else:
#         print("NO")


# # 以下1018
# # the delivery dilemma
# # 外卖是并行的，自取是串行的
# # 外卖时间短的会被时间长的覆盖掉
# t = int(input())
# for test in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     meals = [[] for _ in range(n)]
#     # meals[i][0] = a; meals[i][1] = b
#     for i in range(n):
#         meals[i] =[a[i],b[i]]
#     #  把meals按照a（外送时间）从大到小排
#     meals.sort(key = lambda x:x[0], reverse = True)
#     # 优先自己取外卖时间长的
#     if n > 1:
#         prefix_fetch_time = meals[0][1]
#         for i in range(1,n):
#             if i < n-1:
#                 if meals[i][0] < prefix_fetch_time:
#                     time = min(meals[i-1][0],prefix_fetch_time)
#                     break
#                 else:
#                     prefix_fetch_time += meals[i][1]
#                     time = prefix_fetch_time
#             else:
#                 if meals[i][0] < prefix_fetch_time:
#                     time = min(meals[i-1][0],prefix_fetch_time)
#                 else:
#                     prefix_fetch_time += meals[i][1]
#                     time = min(meals[i][0],prefix_fetch_time)
#
#         print(time)
#     else:
#         print(min(meals[0]))

# # solution 2
# t = int(input())
# for test in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     meals = [[] for _ in range(n)]
#     for i in range(n):
#         meals[i] = [a[i], b[i]]
#     #  把meals按照a（外送时间）从大到小排
#     meals.sort(key=lambda x: x[0], reverse=True)
#     prefix_fetch_time = 0
#     # 优先自己取外卖时间长的
#     for i in range(n):
#         prefix_fetch_time += meals[i][1]
#         if meals[i][0] <= prefix_fetch_time:
#             time = max(prefix_fetch_time - meals[i][1], meals[i][0])
#             break
#         else:
#             time = prefix_fetch_time
#
#     print(time)


# # # 以下是1019
# # 垃圾炸弹
# d = int(input())
# n = int(input())
# # 加保护圈
# location = [[0 for _ in range(1024+40+1)] for _ in range(1024+40+1)]
# # 读每个路口的数据，记得加20
# for _ in range(n):
#     x, y, k = map(int,input().split())
#     x = x + 20
#     y = y + 20
#     for i in range(x-d,x+d+1):
#         for j in range(y-d,y+d+1):
#             location[i][j] += k
#
# count = 0
# max_clear = 0
#
# for i in range(20,1024+20+1):
#     for j in range(20,1024+20+1):
#         if location[i][j] > max_clear:
#             max_clear = location[i][j]
#             count = 1
#         elif location[i][j] == max_clear:
#             count += 1
#
# print(count,max_clear)
#
# # solution2
# d = int(input())
# n = int(input())
# square = [[0]*1025 for _ in range(1025)]
# for _ in range(n):
#     x, y, k = map(int, input().split())
#     #for i in range(x-d if x-d >= 0 else 0, x+d+1 if x+d <= 1024 else 1025):
#       #for j in range(y-d if y-d >= 0 else 0, y+d+1 if y+d <= 1024 else 1025):
#     # 学一下这个方法！就不用总是保护圈了！
#     for i in range(max(x-d, 0), min(x+d+1, 1025)):
#         for j in range(max(y-d, 0), min(y+d+1, 1025)):
#           square[i][j] += k
#
# res = max_point = 0
# for i in range(0, 1025):
#   for j in range(0, 1025):
#     if square[i][j] > max_point:
#       max_point = square[i][j]
#       res = 1
#     elif square[i][j] == max_point:
#       res += 1
# print(res, max_point)


# # Maya Calendar
# n = int(input())
#
#
# month_names = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
#               'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
# cycle_names = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat',
#                'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban',
#                'eznab', 'canac', 'ahau']
# print(n)
#
# for _ in range(n):
#     date = input().split()
#     date[0] = int(date[0][:-1])
#     date[2] = int(date[2])
#     # print(date)
#     day = date[0] + 1
#     month = month_names.index(date[1])
#     year = date[2]
#     # print(day, month, year)
#
#     date = day + 20 * month + 365 * year
#
#     # print(date)
#     year = (date-1) // 260
#     date -= year * 260
#
#     cycle_number = date % 20 if date % 20 != 0 else 20
#     number = date % 13 if date % 13 != 0 else 13
#     cycle = cycle_names[cycle_number - 1]
#
#     print(f"{number}" + ' ' + cycle + ' ' + f"{year}")

# spreadsheets
# 这题重点是正则表达式
# import re
# alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def solve(s):
#     if re.match(r'R\d+C\d+' ,s ):
#         r, c = map(int,s[1:].split("C"))
#         res = ''
#         while c > 0:
#             c, remainder = divmod(c,26)
#             if remainder == 0:
#                 remainder = 26
#                 c = c-1
#             res = alphabet[remainder-1] + res
#         return res + str(r)
#     else:
#         pos = 0
#         while not s[pos].isdigit():
#             pos += 1
#         res = "R" + s[pos:] + 'C'
#         c = 0
#         col = 0
#         # print(s[:pos])
#         # print(list(reversed(s[:pos])))
#         for ch in list(reversed(s[:pos])):
#             # 26进制
#             col += 26 ** c * (alphabet.index(ch) + 1)
#             c += 1
#         return res + str(col)
#
#
# n = int(input())
# for _ in range(n):
#     s = input()
#     print(solve(s))


# import re
# alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# def solve(s):
#     if re.match(r'R\d+C\d+' ,s ):
#         r, c = map(int,s[1:].split("C"))
#         res = ''
#         while c > 0:
#             c, remainder = divmod(c-1,26)
#             res = alphabet[remainder] + res
#         return res + str(r)
#     else:
#         pos = 0
#         while not s[pos].isdigit():
#             pos += 1
#         res = "R" + s[pos:] + 'C'
#         c = 0
#         col = 0
#         # print(s[:pos])
#         # print(list(reversed(s[:pos])))
#         for ch in list(reversed(s[:pos])):
#             # 26进制
#             col += 26 ** c * (alphabet.index(ch) + 1)
#             c += 1
#         return res + str(col)
#
# n = int(input())
# for _ in range(n):
#     s = input()
#     print(solve(s))


# import re
# def solve(s):
#     if re.match(r'R\d+C\d+', s):
#         r, c = map(int, s[1:].split('C'))
#         res = ''
#         while c:
#             c, remainder = divmod(c - 1, 26)
#             res = chr(65 + remainder) + res
#         return res + str(r)
#     else:
#         pos = 0
#         while not s[pos].isdigit():
#             pos += 1
#         res = 'R' + s[pos:] + 'C'
#         c = 0
#         for ch in s[:pos]:
#             c = c * 26 + ord(ch) - 64
#         return res + str(c)
#
# n = int(input().strip())
# for _ in range(n):
#     s = input().strip().split('\n')[0]
#     print(solve(s))


# 以下是1020
# n=int(input())
# a = list(map(int,input().split()))
# target_sum = sum(a)/3
# if target_sum == sum(a)//3:
#     pos1 = []
#     pos2 = []
#     # pos1 左边往右，pos2 右边往左
#     # 前缀和
#     prefix_sum = [0]
#     for num in a:
#         prefix_sum.append(prefix_sum[-1]+num)
#     for i in range(1,n+1):
#         if prefix_sum[i] == target_sum and i < n-1:
#             pos1.append(i)
#         if prefix_sum[i] == 2*target_sum and i < n:
#             pos2.append(i)
#     count = 0
#     for i in pos2:
#         for j in pos1:
#             if j < i:
#                 count+=1
#     print(count)
# else:
#     print(0)

# n=int(input())
# a = list(map(int,input().split()))
# from collections import deque
# prefix_sum = [0]
# for num in a:
#     prefix_sum.append(prefix_sum[-1]+num)
# prefix_sum = deque(prefix_sum)
# prefix_sum.popleft()
# target_sum = prefix_sum[-1]/3
#
# if target_sum == prefix_sum[-1]//3:
#     count = 0
#     s = 0
#     # 记录到2*target_sum的时候，加上它前面所有target_sum的数量
#     # s就是当前这个前缀和前面target_sum的数量
#     for i in range(n):
#         if i < n-2 and prefix_sum[i] == 2 * target_sum:
#             count += s
#         if i < n-1 and prefix_sum[i]==target_sum:
#             s += 1
#     print(count)
# else:
#     print(0)

# number of sequence
# 这个解法的问题在于 不是一个数字占一个位置，而是一个digit占一个位置
# import math
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     # k_min = (-3 + math.sqrt(1+8*n))
#     k_max = (-1 + math.sqrt(1+8*n))//2
#     k = math.floor(k_max)
#     # print(k)
#     n = n - (1+k) * k // 2
#     if n == 0:
#         n = k
#     print(n)

# # 正确解法
# # 生成递增的字符串序列
# # n * (n + 1) // 2 >= 2147483647。通过求解这个不等式，可以得到 n 的值约为 65535
#
# sequence = ""
# s = 0
# ss = 0
# sums = []
#
# for j in range(1, 33000):
#     sequence += str(j)  # 将当前数字转换为字符串并追加到序列中
#     s += len(str(j)) # 累加当前数字的长度
#     ss += s # 累加和（ss是当前的S1...Sj)有多少个digit
#     sums.append(ss)  # 将累加和(sums[i]是S1...Si总共有多少个digit)添加到列表中
#
# # 处理测试用例
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#
#     if n == 1:
#         print(1)
#     else:
#         # 在sums中，找到第一个大于n的digit位数
#         for i in range(len(sums)):
#             if sums[i] >= n:
#                 offset = n - sums[i - 1] - 1
#                 print(sequence[offset])
#                 break

# # 以下是1021
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a = [0] + a + [m]
# t = [0] * (n+2)
#
# # 首先计算出不插入任何a的时候，开灯的时间
# #     如果a的下标为奇数，那么就计算它和前一项的差，加到s（时间）s上
# for i in range(n+2):
#     if i & 1:
#         t[i] = t[i-1] + a[i]-a[i-1]
#     else:
#         t[i] = t[i-1]
#
# t_max = t[n+1]
#
# for i in range(1,n+2,2):
#     t_max = max(t_max, t[i]-1 + a[-1]-a[i]-(t[-1]-t[i]))
#
# print(t_max)

# radar installation
# 不要想着用位置不定的radar去覆盖island
# 要以位置固定的island为中心，画半径为d的圆去覆盖x轴上可能的radar中心位置
#
# import math
# def island_cover(x,y):
#     x_offset = math.sqrt(d**2 - y**2)
#     left = x - x_offset
#     right = x + x_offset
#     intervals_covered=[left,right]
#     return intervals_covered
#
# cases = 0
# while True:
#     n, d = map(int,input().split())
#     intervals = []
#
#     if n + d > 0:
#         cases += 1
#         radars = 0
#         xs = []
#         ys = []
#
#         for i in range(n):
#             x, y = map(int,input().split())
#             xs.append(x)
#             ys.append(y)
#
#         if max(ys) > d:
#             print(f"Case {cases}: {-1}")
#         else:
#             for i in range(n):
#                 intervals.append(island_cover(xs[i],ys[i]))
#
#             intervals.sort(key = lambda m : (m[1],m[0]) )
#             new_intervals = []
#
#
#             while len(intervals)>1:
#                 if intervals[0][1] >= intervals[1][0]:
#                     intervals[0][0] = intervals[1][0]
#                     intervals.pop(1)
#                 else:
#                     new_intervals.append(intervals[0])
#                     intervals.pop(0)
#
#             if len(intervals) == 1:
#                 new_intervals.append(intervals)
#
#             radars = len(new_intervals)
#
#             print(f"Case {cases}: {radars}")
#
#         input()
#
#     else:
#         break

# # 以下是1022
# # woodcutters
# # 是贪心算法，因为能砍就砍，不会有连锁反应（eg 如果第一棵树砍倒导致第二颗树不砍，不会影响第三颗树砍不砍）
# # 也就是说，每棵树能砍就砍，就可以达到最多能砍的树
# n = int(input())
# trees= []
# for i in range(n):
#     trees.append(list(map(int, input().split())))
# trees.sort()
# # 头尾两棵一定可以砍，往两侧倒就可以
# num_tree = 2
# # 中间的树，从左到右，能砍就砍，能往左倒就往左倒，不能往左倒就往右倒
# if n == 1:
#     print(1)
# else:
#     for i in range(1,n-1):
#         if trees[i][0]-trees[i][1] > trees[i-1][0]:
#             num_tree += 1
#         elif trees[i][0]+trees[i][1] < trees[i+1][0]:
#             num_tree += 1
#             trees[i][0] = trees[i][0]+trees[i][1]
#     print(num_tree)

# # cipher
# # 置换计算有周期性
# # 把置换位置的算法用函数写出来
# # 位置x挪动t次到哪个位置，加密的secret keys是a
# def move(x, t, a):
#     for i in range(t):
#         x = a[x]
#     return x
#
# # 计算周期，即加密多少次后导致的效果是相同的
# # a中每个位置上的值映射多少次回到原来的值，a的长度为n
# def find_cir(a, n):
#     ret = []    # 保存每个位置的周期，即循环节
#     for i in range(n):
#         x = a[i]
#         cnt = 1
#         while x != i:
#             x = a[x]
#             cnt += 1
#         ret.append(cnt)
#     return ret
#
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     a = list(map(int, input().split()))
#     for i in range(n):
#         # 改成以0为开始的位置编号
#         a[i] -= 1
#     cir = find_cir(a, n)
#
#     while 1:
#         # st分为“k + message”
#         st = input().split(' ', 1)
#         k = int(st[0])
#         if k == 0:
#             break
#         st = list(st[1])
#         while len(st) < n:
#             st.append(' ')
#         ans = [''] * n
#         for i in range(n):
#             # 取模省略了之前的多次不必要计算
#             ans[move(i, k % cir[i], a)] = st[i]
#         print(''.join(ans))
#     print()

# # 以下是1023
# # maximal binary matrix
# n, k = map(int, input().split())
# num = [[0] * n for _ in range(n)]
# # 从左上角开始，行数优先从上到下排，对称着排
# # 如果剩下一个1，那只能排在对角线上尽量左上的位置
# # 排满了1还没用完，就输出-1
# for i in range(n):
#     for j in range(i, n):
#         if k > 1 and i != j:
#             num[i][j] = 1
#             num[j][i] = 1
#             k -= 2
#         elif k > 0 and i == j:
#             num[i][i] = 1
#             k -= 1
#
# if k == 0:
#     for row in num:
#         print(*row)
# else:
#     print("-1")

# 用自己的话写的
# n, k = map(int, input().split())
# num = [[0] * n for _ in range(n)]
# # 从左上角开始，行数优先从上到下排，对称着排
# # 如果剩下一个1，那只能排在对角线上尽量左上的位置
# # 排满了1还没用完，就输出-1
# for i in range(n):
#     for j in range(i, n):
#         if j == i:
#             if k > 0:
#                 num[i][i] = 1
#                 k -= 1
#         else:
#             if k > 1:
#                 num[i][j] = num[j][i] = 1
#                 k -= 2
#         if k == 0:
#             break
#     if k == 0:
#         break
# if k == 0:
#     for row in num:
#         print(*row)
# else:
#     print("-1")

# 排序
# 递增是小的字典序，递减是大的字典序
# 从右向左查找第一个升序对：
# 从序列的末尾开始向前遍历，找到第一个满足 nums[i] < nums[i + 1] 的索引 i。
# 如果找到了这样的 i，则说明 **从 i+1 到末尾是一个非递增序列** 。
# 从右向左查找第一个大于 nums[i] 的元素：
# 在已经找到的非递增序列中（即从 i+1 到末尾），再次从右向左查找第一个满足 nums[j] > nums[i] 的索引 j。
# 交换 nums[i] 和 nums[j]：将这两个位置的元素交换。
# 反转 i+1 到末尾的元素：由于这部分原本是非递增的，反转后会变成非递减，这是为了确保新的排列是所有可能的比当前排列大的排列中最小的一个。
# 如果没有找到升序对，说明当前排列已经是最大的了（整个序列是非递增的），那么下一个排列应该是最小的排列，可以通过直接反转整个序列来得到。


# def next_permutation(n,nums):
#     # Step 1: Find the first ascending pair from the right
#     i = n-2
#     while i>= 0 and nums[i]>nums[i+1]:
#         i -= 1
#     # Step 2: Find the first number larger than nums[i] from the right
#     # j一定存在，因为nums[i] < nums[i+1], j至少可以等于i+1
#     if i >= 0:
#         j = n-1
#         while nums[j] < nums[i]:
#             j -= 1
#     # Step 3: Swap nums[i] and nums[j]
#         nums[i], nums[j] = nums[j], nums[i]
#         # Step 4: Reverse the elements after index i
#         nums[i + 1:] = reversed(nums[i + 1:])
#     else:
#         nums.reverse()
#
# m = int(input())
# for _ in range(m):
#     n, k = map(int, input().split())
#     nums = list(map(int, input().split()))
#     for times in range(k):
#         next_permutation(n,nums)
#     print(*nums)


# 以下是1024
# Number Game
# 被Bob加过的数就没有办法被Alice在后续选取了，相当于被踢出了可选序列
# k-i+1是随着i增大递减的
# Alice的策略是每一局都删掉尽量大的数
# 可以考虑维护并更新一个可选的序列
# 最后一轮，i = k，k-i+1 = 1，所以Alice想要赢，最后一局必须拿走1
# Bob应该增加最小的数（尽可能地将可选序列中的1踢掉）
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     l.sort()
#     s = l.count(1)
#     if s == 0:
#         print(0)
#         continue
#     # 可选序列每轮至少少掉2个元素（一头一尾）
#     # 可选列表（最多是列表中的所有数字）全部被删完最多需要(n+1)//2轮
#     else:
#         k = min(s,(n+1)//2)
#         while True:
#             i = 1
#             available = [x for x in l if x <= k]
#             # print(available)
#             while len(available) > 0 and available.count(1) > 0:
#                 available.remove(1)
#                 if len(available) > 0:
#                     available.pop(-1)
#                 i += 1
#                 lim = k - i + 1
#                 available = [x for x in available if x<=lim]
#                 # print(available)
#                 # print(i)
#
#             if i == k+1:
#                 print(k)
#                 break
#             else:
#                 k -= 1


# # 以下是1025
# # 排队做实验v0.2
# n = int(input())
# times = list(map(int, input().split())
# students = list(range(1,n+1))
# stu_time = [[] for _ in range(n)]
# for i in range(n):
#     stu_time[i] = [students[i],times[i]]
# stu_time.sort(key = lambda x : x[1])
# for i in range(n):
#     print(stu_time[i][0], end =' ')
# print()
# wait = [0] * n
# prefix = [0]
# for i in range(n-1):
#     prefix.append(prefix[-1] + stu_time[i][1])
#
# average = sum(prefix)/n
# print(f"{average:.2f}")


# # round and round we go
# def gen_rotation(s,n):
#     return [s[i:]+s[:i] for i in range(n)]
# while True:
#     try:
#         s = input()
#         num = int(s)
#         n = len(s)
#         rotations = gen_rotation(s,n)
#         # print(rotations)
#         flag = 1
#         for multiplier in range(1,n+1):
#             result = str(num * multiplier).rjust(n,'0')
#             # print(result)
#             if result not in rotations:
#                 print(f"{s} is not cyclic")
#                 flag = 0
#                 break
#             else:
#                 continue
#         if flag == 1:
#             print(f"{s} is cyclic")
#     except EOFError:
#         break

# 以下是1026
# # 寻找离目标数最近的两数之和
# tar = int(input())  # target
# s = [int(x) for x in input().split()]
# s.sort()
#
# ans = 200000
# gap = 100000 - 2
#
# h = 0  # head
# t = len(s) - 1  # tail
#
# # 如果和大于target，那么就要让和变小一点才可能更靠近target，所以t要减一
# # 如果和小于target，那么就要让和变大一点才可能更靠近target，所以h要加一
# while h < t:
#     mid = s[h] + s[t]
#     if mid == tar:
#         ans = mid
#         break
#
#     # 如果mid和target的gap变小了，那么就应该实时更新ans和gap
#     if abs(mid - tar) < gap:
#         gap = abs(mid - tar)
#         ans = mid
#     if abs(mid - tar) == gap:
#         ans = min(ans, mid)
#
#     if mid > tar:
#         t -= 1
#     elif mid < tar:
#         h += 1
#
# print(ans)
#
# # 假币问题
# # 穷举做法：因为总共24种情况（12枚硬币，轻或重）
# n = int(input())
# for _ in range(n):
#     inp = [input().split() for _ in range(3)]
#     # print(inp)
#
#     coins = [coin for coin in 'ABCDEFGHIJKL']
#
#     for coin in coins:
#         check_light = 1
#         check_heavy = 1
#         for case in inp:
#             left = case[0]
#             right = case[1]
#             state = case[2]
#             if (not (coin in left and state == "down")) and (not (coin in right and state == 'up')) and (not (coin not in right and coin not in left and state == 'even')):
#                 check_light = 0
#             if (not (coin in left and state == "up")) and (not (coin in right and state == 'down')) and (not (coin not in right and coin not in left and state == 'even')):
#                 check_heavy = 0
#
#             # print(check_light,check_heavy)
#         if check_light == 0 and check_heavy == 0:
#             continue
#         if check_light == 1:
#             print(f"{coin} is the counterfeit coin and it is light.")
#             break
#         if check_heavy == 1:
#             print(f"{coin} is the counterfeit coin and it is heavy.")
#             break
#
