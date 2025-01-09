# # sale
# [n,m]=list(map(int,input().split()))
# prices = list(map(int,input().split()))
# prices_negative = [price for price in prices if price <0]
# prices_negative_sorted = sorted(prices_negative)
# earn = 0
# if len(prices_negative_sorted) >= m:
#     earn = -sum(prices_negative_sorted[0:m])
# else:
#     earn = -sum(prices_negative_sorted)
# print(earn)

# # odd divisor
# tests = int(input())
# flags = [0 for i in range(tests)]

# for i in range(tests):
#     number = int(input())
#     # 如果数字是奇数，则一定有odd divisor
#     if number % 2 != 0:
#         flags[i]=1
#     else:
#         # 如果一个偶数是2的次方，则没有odd divisor
#         while number % 2 == 0:
#             number = number//2
#         if number > 1:
#             flags[i] = 1

# # 输出结果
# for i in range(tests):
#     if flags[i] == 1:
#         print("YES")
#     else:
#         print("NO")

# # odd divisor -- solution 2
# tests = int(input())
# for _ in range(tests):
#     number = int(input())
# # 不断处以2直到为奇数
#     while number % 2 == 0:
#         number = number//2
#
#     if number > 1:
#         print("YES")
#     else:
#         print("NO")

# # twins
# coins = int(input())
# values = list(map(int, input().split()))
# values = sorted(values,reverse=True)
# taken = 0
# iteration = 0
# total = sum(values)
# for i in range(coins):
#     if taken <= total/2:
#         taken += values[i]
#         iteration = iteration + 1
#     else:
#         break
# print(iteration)

# # football
# inp = input()
# total = len(inp)
# flag = 0
# for i in range(total-1):
#     if inp[i] == inp[i+1]:
#         flag += 1
#         if flag >= 6:
#             break
#     else:
#         flag = 0
# if flag >= 6:
#     print("YES")
# else:
#     print("NO")

# # chips on the board
# tests = int(input())
# for _ in range(tests):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int,input().split()))
#     matrix = [a,b]
#     smallest = min(sum(b)+n*min(a),sum(a)+n*min(b))
#     print(smallest)

# # restore the weather
# tests = int(input())
# for _ in range(tests):
#     [n,k]=list(map(int,input().split()))
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#
#     # 把b从小到大排序
#     b = sorted(b)
#
#     # 这行以后b都是从小到大的
#
#     # 把a每个温度和自己的天数绑定
#     for day in range(n):
#         a[day] = [a[day],day]
#     # 把标记好天数的a按照 温度 从小到大排列
#     a_sorted = sorted(a,key=lambda x:x[0])
#
#     for i in range(n):
#         # 把b和a的温度对应上
#         a_sorted[i].append(b[i])
#     # paired按照天数从小到大排好
#     paired_sorted = sorted(a_sorted,key=lambda x:x[1])
#     # 打印每个子list的最后一个数，也就是b的温度
#     for day in range(n):
#         print(paired_sorted[day][2],end = " ")
#     print()

# # restore the weather --- solution 2
# t = int(input())
# for _ in range(t):
#     j, k = map(int, input().split())
#
#     l1 = list(map(int, input().split()))
#     v = [(l1[i], i) for i in range(j)] # 默认按照第一个元素进行排列
#     v.sort()
#     print(v)
#     l2 = list(map(int, input().split()))
#     l2.sort()
#
#     z = [0] * j
#     for i in range(j):
#         z[v[i][1]] = l2[i]
#     # 这时候的v已经将a中的温度从小到大排好（tuple里带着温度对应的天数），b也从小到大排好了
#     for data in z:
#         print(data, end=" ")
#     print()

# # 文字排版
# words = int(input())
# content = input().split()
# digit_count = 0
# total_words = 0
# l = ""
# for word in content:
#     digit_count += len(word) + 1
#     total_words += 1
#     l = l + word + " "
#     if digit_count - 1 > 80:
#         l_current = l[:-(len(word)+1)]
#         l_without_space = l_current.rstrip()
#         print(l_without_space)
#         print(word,end = " ")
#         digit_count = len(word) + 1
#         l = ""
#     elif total_words == words:
#         l_without_space = l.rstrip()
#         print(l_without_space)

# # 编码字符串
# inp = input()
# inp = inp.lower()
# letters = list(set(inp))
# count = 0
# for i in range(len(inp)-1):
#     if inp[i] == inp[i+1]:
#         count += 1
#     else:
#         count_total = count + 1
#         letter = letters[letters.index(inp[i])]
#         count = 0
#         print(f"({letter},{count_total})", end = "")
# count_total = count + 1
# letter = letters[letters.index(inp[-1])]
# print(f"({letter},{count_total})", end = "")

# 编码字符串---solution2

# # 校门外的树
# [l,m]=list(map(int,input().split()))
# start = [0] * m
# end = [0] * m
# interval = [0] * m
# for i in range(m):
#     start[i], end[i] = map(int,input().split())
# # start_all = start[0]
# # end_all = end[0]
# # for i in range(m-1):
# #     if end_all > start[i + 1] > start_all:
# #         end_all = max(end_all,end[i+1])
# #     if end_all > end[i+1] > start_all:
# #         start_all = min(start_all,start[i+1])
#     interval[i] = set(range(start[i],end[i]+1))
# def union_set(*sets):
#     return set.union(*sets)
# union_intervals = union_set(*interval)
# print(l+1-len(union_intervals))

# # 提取实体
# sentences = int(input())
# number_total = 0
# for _ in range(sentences):
#     sentence = input()
#     position = [j for j in range(2,len(sentence)) if sentence[j-2:j+1]=="###"]
#     number = len(position)//2
#     # print(position)
#     for i in range(len(position)-1):
#         if sentence[position[i]+2]=="#" and sentence[position[i]+1]==" ":
#             number = number-1
#     number_total += number
# print(number_total)

# # 数学密码 --- 超时
# sum_all = int(input())
# import math
# GCD = 1
# for x1 in range(1,sum_all//3):
#     for x3 in range(sum_all//3+1,sum_all-1):
#             x2 = sum_all - x1 - x3
#             if x1 < x2 < x3:
#                 GCD = max(math.gcd(math.gcd(x1,x2),x3),GCD)
# print(GCD)

# # 数学密码
# # 如果d是最大公因数，那么三个数的和一定是d的倍数，至少6倍
# sum_all = int(input())
# for d in range(sum_all // 6, 0, -1):
#     if sum_all % d == 0:
#         GCD = d
#         break
# # GCD = max([d for d in range(sum_all//6,1,-1) if sum_all % d == 0])
# print(GCD)

# # 24点
# tests = int(input())
# for _ in range(tests):
#     flag = 0
#     [x1, x2, x3, x4] = list(map(int,input().split()))
#     # 测试所有的运算符组合（4个运算符）
#     # 一个循环如果内部的东西没有读完是不会开始一个新的迭代的
#     # 如果一个循环的内部读完了，那么就会开始一个新的迭代
#     # 如果迭代结束了，就会开始读这个循环外部下面的行
#
#     for op1 in ["-","+"]:
#         for op2 in ["-","+"]:
#             for op3 in ["-","+"]:
#                 for op4 in ["-","+"]:
#                     equation = f"{op1}{x1}{op2}{x2}{op3}{x3}{op4}{x4}"
#                     if eval(equation) == 24:
#                         flag = 1
#                         print("YES")
#                         break
#                 if flag == 1:
#                     break
#             if flag == 1:
#                 break
#         if flag ==1:
#             break
#
#     if flag == 0:
#         print("NO")

# # hangover
# while True:
#     goal = float(input())
#     cards = 0
#     if goal != 0.00:
#         overhang = 0.00
#         while overhang < goal:
#             overhang += 1/eval(f"2+{cards}")
#             cards += 1
#         print(f"{cards} card(s)")
#     else:
#         break

# # multiply by 2, divide by 6
# tests = int(input())
# for _ in range(tests):
#     x = int(input())
#     n = 0
#     m = 0
#     while x % 2 == 0:
#         x = x//2
#         n += 1
#     while x % 3 == 0:
#         x = x//3
#         m += 1
#     if x > 1 or n > m:
#         print(-1)
#     else:
#         moves = (m-n) + m
#         print(moves)

# # vasya and socks
# [n, m] = list(map(int, input().split()))
# socks = n
# days = 0
# while socks > 0:
#     socks -= 1
#     days += 1
#     if days % m == 0:
#         socks += 1
# print(days)

# # 数论
# n = int(input())
# import math
# def prime_factors(n):
#     lim = math.ceil(math.sqrt(n))
#     factors = []
#     div = 2
#         # 从2开始，有多少个2就除多少个2，然后往上找除数
#         # 因为更大的合数都可以被分解为比自己小的质数，所以只要从小往大找找到的一定是质因数
#         # 每一个质因数都是有多少除多少
#         # 如果除出来还是大于1，说明没分解完，接着分解
#     while n > 1:
#         while n % div == 0 and div <= lim:
#             factors.append(div)
#             n //= div
#         div += 1
#         # 如果发现所有比sqrt（n）小的质数都不是n的因数，那么它自己就是质数
#         if div > lim:
#             factors.append(n)
#             break
#     return factors
# if len(prime_factors(n))>len(set(prime_factors(n))):
#     print(0)
# elif len(prime_factors(n)) % 2 ==0:
#     print(1)
# else:
#     print(-1)

# # keyboard
# shift = input()
# inp = input()
# keys = "qwertyuiopasdfghjkl;zxcvbnm,./"
# positions = []
# l = ""
# for i in range(len(inp)):
#     if shift == "R":
#         positions.append(keys.find(inp[i])-1)
#         l += keys[positions[i]]
#     else:
#         positions.append(keys.find(inp[i]) + 1)
#         l += keys[positions[i]]
# print(l)

# # 验证哥德巴赫猜想
# # 先定义一个函数用于验证某个数字是否是prime质数
# import math
# def isprime(n):
#     div = 2
#     limit = math.ceil(math.sqrt(n))
#     while n > 1:
#         while div <= limit:
#             flag = n % div
#             if flag == 0:
#                 break
#             div += 1
#         if flag == 0:
#             break
#         else:
#             return True
#     return False
# # 把3—2000之间的奇数筛选出来
# odds = range(3,2000,2)
# # 在奇数中筛选出3-2000的质数
# primes = [odd for odd in odds if isprime(odd)]
# # 下面开始枚举法进行分解
# x = int(input())
# if not(x >= 6 and x % 2==0) :
#     print("Error!")
# else:
#     lim = x // 2
#     for y in primes:
#         if y <= lim:
#             z = x - y
#             if z in primes:
#                 print(f"{x}={y}+{z}")

# # kefa and first step
# n = int(input())
# money = list(map(int,input().split()))
# length = 0
# max_length = 0
# if n>1:
#     for day in range(n-1):
#         if money[day] <= money[day+1]:
#             length += 1
#             if day == n-1:
#                 flag = 1
#         else:
#             max_length = max(max_length, length + 1)
#             length = 0
#         if day == n-2:
#             max_length_final = max(length + 1, max_length)
#             print(max_length_final)
# else:
#     print(1)

# # 这一天星期几
# tests = int(input())
# import math
# for _ in range(tests):
#     date = input()
#     c = int(date[0:2])
#
#     y = int(date[2:4])
#
#     m = int(date[4:6])
#     if m == 1:
#         m = 13
#         if y != 0:
#             y = y-1
#         else:
#             y = 0
#             c = c+1
#     elif m == 2:
#         m = 14
#         if y != 0:
#             y = y-1
#         else:
#             y = 0
#             c = c+1
#     d = int(date[6:8])
#     w = (y + math.floor(y/4) + math.floor(c/4) - 2*c + math.floor(26*(m+1)/10) + d -1) % 7
#     if w == 0:
#         print("Sunday")
#     elif w == 1:
#         print("Monday")
#     elif w == 2:
#         print("Tuesday")
#     elif w == 3:
#         print("Wednesday")
#     elif w == 4:
#         print("Thursday")
#     elif w ==5:
#         print("Friday")
#     else:
#         print("Saturday")
