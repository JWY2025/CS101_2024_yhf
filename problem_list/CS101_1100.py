# # fancy fence
# tests = int(input())
# for _ in range(tests):
#     angle = int(input())
#     if 360 % (180-angle) == 0:
#         print("YES")
#     else:
#         print("NO")
from pdb import line_prefix
from stringprep import b1_set

# # 简单的数学题
# tests = int(input())
# pos = []
# neg = []
# for x in range(1, 10**6 + 1):
#     original_x = x
#     while x % 2 == 0:
#         x = x // 2
#     if x == 1:
#         neg.append(original_x)
#     else:
#         pos.append(original_x)
# for _ in range(tests):
#     n = int(input())
#
#     for x in range(1,n+1):
#         original_x = x
#         while x % 2 ==0:
#                 x = x//2
#         if x == 1:
#             neg.append(original_x)
#         else:
#             pos.append(original_x)
#     print(sum(pos)-sum(neg))

# tests = int(input())
# lineup=[]
# for x in range(1, 10**6 + 1):
#     original_x = x
#     while x % 2 == 0:
#         x = x // 2
#     if x == 1:
#         lineup.append(-original_x)
#     else:
#         lineup.append(original_x)
# for _ in range(tests):
#     n = int(input())
#     print(sum(lineup[:n]))

# tests = int(input())
# import math
# for _ in range(tests):
#     n = int(input())
#     sum_all = (1 + n) * n // 2
#     x = math.floor(math.log2(n))
#     sum_2_power = 2 ** (x+1) - 1
#     print(sum_all-2*sum_2_power)

# # 单调递增序列
# n = int(input())
# lineup= list(map(int, input().split()))
# flag = 0
# for i in range(n):
#     if i < n-1:
#         if lineup[i+1] < lineup[i]:
#             flag = 1
# if flag == 1:
#     print("NO")
# else:
#     print("YES")

# # 二进制回文的整数
# x = int(input())
# bi_x = bin(x)[2:]
# bi_x_re = bi_x[::-1]
# if bi_x_re == bi_x:
#     print("Yes")
# else:
#     print("No")

# # 二进制回文的整数
# x = int(input())
# bi_x = bin(x)[2:]
# bi_x_re = bi_x[::-1]
# if bi_x_re == bi_x:
#     print("Yes")
# else:
#     print("No")

# # 水仙花数
# a,b = map(int,input().split())
# flag = 0
# string = ""
# for n in range(a,b+1):
#     original_n = n
#     hundred = n // 100
#     n = n % 100
#     ten = n // 10
#     n = n % 10
#     one = n
#     if original_n == hundred ** 3 + ten ** 3 + one ** 3:
#         string += f"{original_n}" + " "
#         flag = 1
# if flag == 0:
#     print("NO")
# else:
#     print(string[:-1])

# # 小朋友春游
# n = int(input())
# left = list(map(int, input().split()))
# lost = list(range(1,n+1))
# other = []
# for num in left:
#     if num <= n:
#        lost.remove(num)
#     else:
#         other.append(num)
# lost.sort()
# other.sort()
# for lost in lost:
#     print(lost, end= " ")
# print()
# for other in other:
#     print(other, end =" ")

# # 寻找元素对
# n = int(input())
# lineup = list(map(int, input().split()))
# k = int(input())
# count = 0
# for i in range(n):
#     for j in range(n):
#         if lineup[i] + lineup[j] == k:
#             count += 1
# print(count//2)

# # how old are you
# x = int(input())
# while x > 1:
#     if x % 2 != 0:
#         y = x * 3 +1
#         print("{}*3+1={}".format(x, y))
#         x=y
#     else:
#         y = x // 2
#         print("{}/2={}".format(x,y))
#         x=y

# # 等腰直角三角形II（这里是9.25的E）
# n = int(input())
# for row in range(n-1):
#     if row == 0:
#         print("*")
#     else:
#         print("*",end="")
#         for col in range(1,row):
#             print(" ",end = "")
#         print("*")
# for col in range(n):
#     print("*",end="")

# 装箱问题

# import math
# while True:
#     inp = list(map(int, input().split()))
#     rest_for_b = [0,5,3,1]
#     if sum(inp) == 0:
#         break
#     [a,b,c,d,e,f] = inp # a:1*1 b:2*2 // c:3*3 // d:4*4 e:5*5 f:6*6
#     boxes = d + e + f # 4*4 5*5 6*6 每个都先占一个箱子
#     boxes += math.ceil(c/4) # 3*3 4个一组 先占一个箱子 剩下的放一个箱子
#     space_for_b = d * 5 + rest_for_b [c % 4] # 每个d所在的箱子可以放5个b，如果c有没有放满的箱子，那么还能放b
#     if b>space_for_b:
#         boxes += math.ceil((b-space_for_b)/9)
#     space_for_a = boxes * 36 - 36 * f - 25 * e - 16 * d - 9 * c - 4 * b
#     if a > space_for_a:
#         boxes += math.ceil((a-space_for_a)/36)
#     print(boxes)

# # 日期加法
# year, month, day= map(int,input().split("-"))
# n = int(input())
# big_month = [1,3,5,7,8,10,12]
# small_month = [4,6,9,11]
# feb = 2
# day += n
# def isleap(year):
#     if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#         return True
#     else:
#         return False
# while day > 28:
#     if month in big_month:
#         if day > 31:
#             month += 1
#             day -= 31
#     elif month in small_month:
#         if day > 30:
#             month += 1
#             day -= 30
#     elif month == feb: # 其实就是2月
#         if isleap(year):
#             if day > 29:
#                 month += 1
#                 day -= 29
#         else:
#             if day > 28:
#                 month += 1
#                 day -= 28
#     while month > 12:
#         year += 1
#         month -= 12
#     if not (day > 29 and isleap(year) and month == feb) and not (day > 28 and isleap(year)==False and month == feb) and not (day > 31 and month in big_month) and not (day > 30 and month in small_month):
#         break
# print(f"{year}-{month:02}-{day:02}")

# # the drunk jailer
# tests = int(input())
# for _ in range(tests):
#     n = int(input())
#     state = [0 for _ in range(n)]
#     for round in range(n):
#         for i in range(n):
#             if (i+1) % (round+1) == 0:
#                 state[i] = not(state[i])
#     print(sum(state))

# # T-primes
# n = int(input())
# inp = list(map(int,input().split()))
# import math
# # 欧拉筛的核心在于 每个合数都是通过自己的最小质因数筛掉的
# def euler_sieve(limit):
#     primes = []
#     # is_prime是标记每个2～limit的数字是不是素数的
#     # is_prime[num-2]代表的是num的属性
#     # 可以先把所有数标记成素数
#     # 后续把合数标记为False（筛掉）
#     is_prime = [True] * (limit-1)
#     # 在2～limit中从小到大找素数
#     for num in range(2,limit+1):
#         if is_prime[num-2]:
#             # 找到一个素数就加进primes
#             primes.append(num)
#             # 把新加进primes的素数的倍数划掉，但是从num**2开始
#             # num**2的最小质因数才是num，更小的数字最小质因数一定比num小
#             # 所以num**2之前的应该被更小的质因数筛掉了
#             for b in range(num**2, limit+1, num):
#                 is_prime[b-2]=False
#     return primes
#
# primes = euler_sieve(10**6)
# primes_square = list(map(lambda x: x ** 2, primes))
# for i in range(n):
#     num = inp[i]
#     if num in primes_square:
#         print("YES")
#     else:
#         print("NO")
#     # for prime in [prime for prime in primes if prime <= math.floor(num)]:
#     #     if num == prime**2:
#     #         print("YES")
#     #         flag = 1
#     #         break
#     # if flag == 0:
#     #     print("NO")

# # taxi
# # 和装箱问题的思路比较像
# groups = int(input())
# members = list(map(int, input().split()))
#
# four = [x for x in members if x == 4]
# three = [x for x in members if x == 3]
# two = [x for x in members if x == 2]
# one = [x for x in members if x == 1]
#
# import math
# taxi = len(four) + len(three) + math.ceil(len(two) / 2)
# space = len(three) + 2 * (math.ceil(len(two)/2)-len(two)//2)
# if space < len(one):
#     rest = len(one) - space
#     taxi += math.ceil(rest/4)
#
# print(taxi)

# # 圣诞老人的礼物
# n , w = map(int, input().split())
# v_per_w = [0] * n
# weight=[0] * n
# value = [0] * n
# paired_v_w = [() for _ in range(n)]
# for i in range(n):
#     value[i],weight[i] = map(int, input().split())
#     v_per_w[i] = value[i]/weight[i]
#     paired_v_w[i] = (v_per_w[i],weight[i])
# paired_v_w = sorted(paired_v_w,key=lambda x:x[0],reverse=True)
# # print(paired_v_w)
# weight_now = 0
# value_now = 0
# for pair in paired_v_w:
#     if pair[1] + weight_now <= w:
#         weight_now += pair[1]
#         value_now += pair[1] * pair[0]
#     elif pair[1] + weight_now > w:
#         weight_left = w - weight_now
#         value_now += weight_left * pair[0]
#         break
# value_now = round(value_now,1)
# print(value_now)

# # 约瑟夫问题
#
# # pop函数可以按位置索引移除元素并返回移除的元素的值 list.pop(index)
# # remove函数移除列表中第一个和输入相同的元素 list.remove(value)
# # del 可以删除列表中的元素 del list[2]
#
# while True:
#     n,m = map(int, input().split())
#     if m + n > 0:
#         queue = list(range(1,n+1))
#         queue =list(map(lambda x: [x,1,x], queue))
#         #第一个是i（不断连续往下编号），第二个是标志是否被剔除的flag，第三个是原始数
#
#         i = 1
#         # 这个是连续编号的i，不断迭代
#
#         length = n
#
#         while length > 1:
#
#             for item in queue:
#
#                 if item[1] == 1:
#                     item[0] = i
#                     i = i + 1
#                 # 如果没有被剔除，往下编号
#                     if item[0] % m == 0:
#                         item[1] = 0
#                     # 如果发现i是m的倍数，那么把这个项目的flag设为0
#                 length = len([x for x in queue if x[1] == 1])
#
#                 if length == 1:
#                     break
#
#         # 这里出循环了
#         left = [x for x in queue if x[1] == 1]
#         print(left[0][2])
#
#     else:
#         break
# #   最后是为了break出while True循环

# # laptops
# n = int(input())
# price_quality_pair = [[] for _ in range(n)]
# for i in range(n):
#     price_quality_pair[i] = list(map(int, input().split()))
#
# price_quality_pair = sorted(price_quality_pair, key=lambda x: x[0])
# flag = 0
# for i in range(n-1):
#     if price_quality_pair[i][1] > price_quality_pair[i+1][1] and price_quality_pair[i][0] < price_quality_pair[i+1][0]:
#         flag = 1
#         break
# if flag == 1:
#     print("Happy Alex")
# else:
#     print("Poor Alex")

# # holiday hotel
# # 因为平台的输入是一股脑输入的，一定要设置一个停止运行的标志 n == 0
# # 如果不设置的话，会把0认为是下一个输入的 n，产生错误
# while True:
#     n = int(input())
#     d_c = [[] for _ in range(n)]
#     if n == 0:
#         break
#     for i in range(n):
#         d_c[i] = list(map(int, input().split()))
#     # 按照d从小到大排序，也就是说，从距离由近到远排序
#     # 如果有相同距离，那么是价格从低到高排序
#     d_c.sort(key = lambda x:(x[0],x[1]))
#     candidate = 0
#     c = list(map(lambda x:x[1],d_c))
#     if n >= 2:
#         for i in range(n):
#
#             item = d_c[i]
#             # 第一个，没有人比它更近，而且它是同距离里最便宜的一个（sort的性质），所以它一定是candidate
#             if i == 0:
#                 candidate += 1
#             # 最后一个，必须是所有的旅馆里最便宜的，而且不能有和它同距离的比它便宜
#             elif i == n-1:
#                 if item[1] < min(c[:-1]):
#                     candidate += 1
#             # 中间的，比它近的要比它贵，比它便宜的要比它远（不可以同一个距离的hotel比它便宜）
#             else:
#                 closer_c = c[:i]
#                 if min(closer_c) > item[1]:
#                     candidate += 1
#         print(candidate)
#     else:
#         print(1)

# # BerSU ball
# n = int(input())
# boys = list(map(int, input().split()))
# boys.sort()
#
# m = int(input())
# girls = list(map(int, input().split()))
# girls.sort()
#
# pairs = 0
# # 双指针
# i, j = 0, 0
#
# if n < m:
#     while i<=n-1 and j<=m-1:
#         if girls[j] < boys[i]-1:
#             j += 1
#         elif girls[j] > boys[i]+1:
#             i += 1
#         else:
#             pairs += 1
#             i += 1
#             j += 1
#
# else:
#     while i<=m-1 and j<=n-1:
#         if boys[j] < girls[i]-1:
#             j += 1
#         elif boys[j] > girls[i]+1:
#             i += 1
#         else:
#             pairs += 1
#             i += 1
#             j += 1
# print(pairs)

# # ants
# tests = int(input())
# for _ in range(tests):
#     l, ants = map(int, input().split())
#     positions = list(map(int, input().split()))
#     left = [x for x in positions if x < l/2]
#     right = [x for x in positions if x >= l/2]
#     if len(left) > 0 and len(right) > 0:
#         # 最早的：中点左边往左边走，中点右边往右边走，没有蚂蚁相遇
#         earliest = max(max(left),l-min(right))
#     elif len(left) == 0:
#         earliest = l - min(right)
#     else:
#         earliest = max(left)
#     # 最晚的：实际上两只蚂蚁相遇后，可以看作是擦肩而过，往原来的方向行进
#     # 因为每只蚂蚁的速度是一样的，等价
#     positions.sort()
#     if len(left) > 0 and len(right) > 0:
#         latest = max(l-min(left),max(right))
#     elif len(left) == 0:
#         latest = max(right)
#     else:
#         latest = l - min(left)

#     print(f"{earliest} {latest}")

# # Kuriyama Mirai's stones
# n = int(input())
# costs = list(map(int, input().split()))
# sorted_costs = sorted(costs)
#
# m = int(input())
# for _ in range(m):
#     question, l, r = map(int, input().split())
#     if question == 1:
#         print(sum(costs[l-1:r]))
#     else:
#         print(sum(sorted_costs[l-1:r]))

# 提高效率后的stones这道题
# 排序算法O(nlog2n)

# 切片算法遍历l～r的元素，所以最差情况O(n)
# 总共要经历m次切片，所以O(n*m)
# 前缀求和：O(n)
# 访问第r个和第l个元素：O(1)
# 所以O(n)

# n = int(input())
# costs = list(map(int, input().split()))
# sorted_costs = sorted(costs)
#
# prefix_sum = [0]
# prefix_sum_sorted = [0]
#
# for i in range(n):
#     # 每次新的prefix_sum都是上一个prefix_sum加当前的cost
#     prefix_sum.append(prefix_sum[-1] + costs[i])
#     prefix_sum_sorted.append(prefix_sum_sorted[-1] + sorted_costs[i])
#
# m = int(input())
#
# for _ in range(m):
#     question, l, r = map(int, input().split())
#     if question == 1:
#         print(prefix_sum[r]-prefix_sum[l-1])
#     else:
#         print(prefix_sum_sorted[r]-prefix_sum_sorted[l-1])

# # 斐波那契数列
# n = int(input())
# lineup = [0 for i in range(20)]
# lineup[0] = 1
# lineup[1] = 1
# for i in range(2,20):
#     lineup[i] = lineup[i-1] + lineup[i-2]
#
# for _ in range(n):
#     a = int(input())
#     print(lineup[a-1])

# # Vanya and lanterns
# n, l = map(int, input().split())
# a = list(map(int, input().split()))
# if n > 1:
#     d = [0] * (n-1)
#     a.sort()
#
#     for i in range(n-1):
#         d[i] = a[i+1]-a[i]
#
#
#     d_min = max(max(max(d)/2,a[0]),l-a[-1])
# else:
#     d_min = max(a[0],l-a[0])
#
# print(d_min)

# # Pell 数列
# n = int(input())
#
# k = [0] * n
#
# for i in range(n):
#     k[i] = int(input())
#
# pell = [0] * max(k)
# pell[0] = 1
# pell[1] = 2
#
# for i in range(2,max(k)):
#     pell[i] = 2 * pell[i-1] + pell[i-2]
#
# for i in range(n):
#     print(pell[k[i]-1] % 32767)

# 可以先取模再运算，让内存变小（数字变小了）
# n = int(input())
# pell = [0] * 10**6
# pell[0],pell[1] = 1, 2
# for i in range(2,10**6):
#     pell[i] = (2 * pell[i-1] + pell[i-2]) % 32767
#
# for _ in range(n):
#     k = int(input())
#     print(pell[k-1])

# # Pasha and Pixels
# n, m, k = map(int,input().split())
# pixels = [[0 for _ in range(m+2)] for _ in range(n+2)]
# # 相当于把n*m的方格外面又加了一圈方格
#
# move = 0
# flag = 0
#
# for i in range(k):
#     row, col = map(int,input().split())http://cs101.openjudge.cn/practice/18160
#     pixels[row][col] = 1
#     move += 1
#     if (pixels[row][col] + pixels[row-1][col-1] + pixels[row-1][col] + pixels[row][col-1] == 4
#             or pixels[row][col] + pixels[row+1][col+1] +  pixels[row+1][col] + pixels[row][col+1] == 4
#             or pixels[row][col] + pixels[row-1][col+1] + pixels[row][col+1] + pixels[row-1][col] == 4
#             or pixels[row][col] + pixels[row+1][col-1] + pixels[row][col-1] + pixels[row+1][col] == 4):
#         flag = 1
#         print(move)
#         break
# if flag == 0:
#     print(0)
#
# # 集合加法
# 这个做法的题意理解不太对，认为A中一个元素只能和B中一个元素配对
# 其实A中一个元素可以和B中所有元素配对
# n = int(input())
# for _ in range(n):
#     s = int(input())
#     a = int(input())
#     A = list(map(int, input().split()))
#     A.sort()
#     b = int(input())
#     B = list(map(int, input().split()))
#     B.sort()
#     pair = 0
#
#     # 双指针，但是A从小往大找，B从大往小找
#     i, j = 0, b-1
#
#     while i <= a-1 and j >= 0:
#         print(pair)
#         if A[i] + B[j] == s:
#             pair += 1
#             i += 1
#             j -= 1
#         elif A[i] + B[j] < s:
#             i += 1
#         else:
#             j -= 1
#     print(pair)

# # 集合加法
# n = int(input())
# for _ in range(n):
#     s = int(input())
#     a = int(input())
#     A = list(map(int, input().split()))
#     A.sort()
#     b = int(input())
#     B = list(map(int, input().split()))
#     B.sort()
#     pair = 0
#
#     for p in A:
#         for q in B:
#             if p+q == s:
#                 pair += 1
#             elif p + q > s:
#                 break
#
#     print(pair)
#
# # queue
# n = int(input())
# t = list(map(int, input().split()))
# t.sort()
# lineup = t[:2]
# for item in t[2:]:
#     prefix = sum(lineup)
#     if item >= prefix:
#         lineup.append(item)
# print(len(lineup))

# # 完美立方
# n = int(input())
# triple = []
# for a in range(2,n+1):
#     for d in range(a,1,-1):
#         for c in range(d,1,-1):
#             for b in range(2,c+1):
#                 if a**3 == b**3 + c**3 + d**3:
#                     triple.append([a,b,c,d])
#                     break
# triple.sort()
# for i in range(len(triple)):
#     print(f"Cube = {triple[i][0]}, Triple = ({triple[i][1]},{triple[i][2]},{triple[i][3]})")


# # boxes packing
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# # print(a)
# boxes = n
# simplified = []
# repetition = 1
# for i in range(1,n):
#     if a[i] == a[i-1]:
#         repetition += 1
#     else:
#         simplified.append([a[i-1],repetition])
#         repetition = 1
# simplified.append([a[-1],repetition])
# # print(simplified)
# print(max(list(map(lambda x: x[1], simplified))))

# # 大整数加法
# 意义何在啊？
# a = int(input())
# b = int(input())
# print(a+b)

# # 十进制转k进制
# n, k = map(int,input().split())
# string = ""
# while n >= k:
#     mod = n % k
#     n = n // k
#     if mod == 10:
#         mod = "A"
#     elif mod == 11:
#         mod = "B"
#     elif mod == 12:
#         mod = "C"
#     elif mod == 13:
#         mod = "D"
#     elif mod == 14:
#         mod = "E"
#     elif mod == 14:
#         mod = "F"
#     string += str(mod)
# string += str(n)
# print(string[::-1])
# 列表切片可以让字符串倒过来

# # 约瑟夫问题No.2
#
# # 约瑟夫问题
# # pop函数可以按位置索引移除元素并返回移除的元素的值 list.pop(index)
# # remove函数移除列表中第一个和输入相同的元素 list.remove(value)
# # del 可以删除列表中的元素 del list[2]
#
# while True:
#     n, p, m = map(int,input().split())
#     if m + n + p > 0:
#         queue = list(range(p,n+1))
#         for i in range(1,p):
#             queue.append(i)
#         queue =list(map(lambda x: [x,1,x], queue))
#         #第一个是i（不断连续往下编号），第二个是标志是否被剔除的flag，第三个是原始数
#
#         i = 1
#         # 这个是连续编号的i，不断迭代
#
#         removed = []
#         # 用来记录移除的数
#
#         length = n
#
#         while length > 1:
#
#             for item in queue:
#
#                 if item[1] == 1:
#                     item[0] = i
#                     i = i + 1
#                 # 如果没有被剔除，往下编号
#                     if item[0] % m == 0:
#                         item[1] = 0
#                         removed.append(item[2])
#                     # 如果发现i是m的倍数，那么把这个项目的flag设为0
#                 length = len([x for x in queue if x[1] == 1])
#
#                 if length == 1:
#                     break
#
#         # 这里出循环了
#
#         for i in range(len(removed)):
#             print(removed[i],end=",")
#         left = [x for x in queue if x[1] == 1]
#         print(left[0][2])
#     else:
#         break
#   最后是为了break出while True循环

# # 公共前缀
# n = int(input())
# string = ['' for _ in range(n)]
# length = [0] * n
# prefix = ''
# for i in range(n):
#     string[i] = input()
#     length[i] = len(string[i])
# min_len = min(length)
# min_string = string[length.index(min_len)]
# flag = 0
# for i in range(min_len):
#     letter = min_string[i]
#     for j in range(n):
#         current_string = string[j]
#         if current_string[i] != letter:
#             flag = 1
#             break
#     if flag == 0:
#         prefix += letter
#     else:
#         break
# print(prefix)

# # 质数的和与积
# s = int(input())
# import math
# half = math.ceil(s / 2)
#
# # 欧拉筛
# def euler_sieve(limit):
#     primes = []
#     # is_prime是标记每个2～limit的数字是不是素数的
#     # is_prime[num-2]代表的是num的属性
#     # 可以先把所有数标记成素数
#     # 后续把合数标记为False（筛掉）
#     is_prime = [True] * (limit-1)
#     # 在2～limit中从小到大找素数
#     for num in range(2,limit+1):
#         if is_prime[num-2]:
#             # 找到一个素数就加进primes
#             primes.append(num)
#             # 把新加进primes的素数的倍数划掉，但是从num**2开始
#             # num**2(num的平方)的最小质因数才是num，更小的数字最小质因数一定比num小
#             # 所以num**2之前的应该被更小的质因数筛掉了
#             for b in range(num**2, limit+1, num):
#                 is_prime[b-2]=False
#     return primes
# primes = euler_sieve(s)
# for x in range(half,s):
#     y = s - x
#     if x in primes and y in primes:
#         print(x*y)
#         break
