# #鸡兔同笼02750
# legs = int(input())
# if legs % 4 ==0:
#     least=legs//4
#     most=legs//2
# elif legs % 2 ==0:
#     least=int((legs-2)/4)+1
#     most=legs//2
# else:
#     least=0
#     most=0
# print(least,end=" ")
# print(most)

# #判断闰年02733
# year=int(input())
# if year % 4 != 0:
#     print("N")
# elif year % 100 ==0 and year % 400 != 0:
#     print("N")
# elif year % 400 ==0:
#     print("Y")
# else:
#     print("Y")

# #drinks
# number = int(input())
# percent_string=input()
# # 把输入的字符串拆开来
# percent=percent_string.split(" ")
# # 把字符串列表变成浮点数列表
# for index in range(0,number):
#     percent[index]=float(percent[index])
# if len(percent)==number:
#     fraction=sum(percent)/number
#     print(fraction)

# # domino piling
# input_string = input()
# input_m_n=input_string.split()
# m = int(input_m_n[0])
# n = int(input_m_n[1])
# if (m*n) % 2 ==0:
#     domino=m*n//2
# else:
#     domino=(m-1)*n//2+n//2
# print(domino)

# # watermelon
# weight=int(input())
# if weight % 2 !=0 or weight==2:
#     print("NO")
# else:
#     print("YES")

# # next round
# n_k_string = input().split()
# n = int(n_k_string[0])
# k = int(n_k_string[1])
# score_string = input().split()
# score=[]
# number=0
# for index in range(0,n):
#     score.append(int(score_string[index]))
# for index in range(0,n):
#     if score[index]>0 and score[index]>=score[k-1]:
#         number += 1
# print(number)

# # petya and strings
# string1 = input().lower()
# string2 = input().lower()
# if string1 < string2:
#     print(-1)
# elif string1 == string2:
#     print(0)
# else:
#     print(1)

# #boyorgirl
# name = input()
# import string
# lowercase_letters = list(string.ascii_lowercase)
# number = 0
# for letter in lowercase_letters:
#     position = name.find(letter)
#     if position != -1:
#         number += 1
# if number % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

# # team
# question = int(input())
# solution = []
# answer = 0
# for i in range(0,question):
#     solution.append(input())
#     questioni=solution[i].split(' ')
#     for n in range(0,3):
#         questioni[n] = int(questioni[n])
#     solution[i] = sum(questioni)
#     if solution[i] >= 2:
#         answer += 1
# print(answer)

# # stones on the table
# number = int(input())
# colors = input()
# flag = 0
# for index in range(number-1):
#     if colors[index]==colors[index+1]:
#         flag +=1
# print(flag)
# 把字符串中的每个字母编码为index的方法，不简单
# for index in range(number):
#     if colors[index]=="R":
#         position_red.append(index)
#     elif colors[index]=="G":
#         position_green.append(index)
#     else:
#         position_blue.append(index)
# if len(position_red)>0 and len(position_red)>0 and len(position_green)>0 and len(position_green)>0:
#     for i in range(0,len(position_red)-1):
#         if position_red[i]==position_red[i+1]-1:
#             flag += 1
#     for i in range(0, len(position_blue)-1):
#         if position_blue[i] == position_blue[i+1]-1:
#             flag += 1
#     for i in range(0,len(position_green)-1):
#         if position_green[i]==position_green[i+1]-1:
#             flag += 1
# print(flag)

# # beautiful matrix
# row1 = input().split()
# row2 = input().split()
# row3 = input().split()
# row4 = input().split()
# row5 = input().split()
# row1 = [int(num) for num in row1]
# row2 = [int(num) for num in row2]
# row3 = [int(num) for num in row3]
# row4 = [int(num) for num in row4]
# row5 = [int(num) for num in row5]
# rows = [row1, row2, row3, row4, row5]
# flagrow = 0
# flagcol = 0
# for rownum in range(0,5):
#     if sum(rows[rownum]) != 0:
#         flagrow = rownum
# flagcol=rows[flagrow].index(1)
# moves = abs(flagcol-2) + abs(flagrow-2)
# print(moves)

# # hitthelottery
# total = int(input())
# number100 = total//100
# number20 = (total-100*number100)//20
# number10 = (total-100*number100-20*number20)//10
# number5 = (total-100*number100-20*number20-10*number10)//5
# number1 = (total-100*number100-20*number20-10*number10-5*number5)//1
# print(number1 + number5 + number10 + number20 + number100)

# # divisibilityproblem
# tests = int(input())
# inp = []
# moves = 0
# for times in range(tests):
#     inp.append(list(map(int,input().split())))
# for times in range(tests):
#     if inp[times][0] % inp[times][1] == 0:
#         moves = 0
#     else:
#         moves = inp[times][1]-inp[times][0] % inp[times][1]
#     print(moves)

# # a sum of round numbers
# rows = int(input())
# number = [0 for i in range(rows)]
# digit = [0 for i in range(rows)]
# round_numbers = [[] for i in range(rows)]
# non_zeros = [0 for i in range(rows)]
# non_zeros_length = [0 for i in range(rows)]
# for row in range(rows):
#     number[row] = input()
#     # list(map(int, )))是将一个输入的str类型的数字转化为一个个digit分开的int型元素组成的lsit
#     digit[row]=list(map(int, number[row]))
#     length = len(digit[row])
#     for i in range(length):
#         round_numbers[row].append(digit[row][i] * 10 ** (length - i - 1))
#     non_zeros[row]=[x for x in round_numbers[row] if x != 0]
#     non_zeros_length[row] = len(non_zeros[row])
# for row in range(rows):
#     print(non_zeros_length[row])
#     length = len(non_zeros[row])
#     for i in range(length):
#         print(non_zeros[row][i],end=" ")
#     print()

# # candies and two sisters
# tests = int(input())
# candies = [0 for i in range(tests)]
# ways = [0 for i in range(tests)]
# for test in range(tests):
#     candies[test] = int(input())
#     a_min = candies[test] // 2 + 1
#     a_max = candies[test] - 1
#     ways[test] = a_max - a_min + 1
# for test in range(tests):
#     print(ways[test])

# # soft drinking
# inpstr = input().split()
# [n, k, l, c, d, p, nl, np] = list(map(int, inpstr))
#
# volume = k * l
# slices = c * d
#
# glasses = volume // nl
# salt = p // np
#
# toasts_max = min(glasses, salt, slices)
# toasts = toasts_max - toasts_max % n
# toasts_per_friend = toasts // n
# print(toasts_per_friend)

# # police recruits---solution1
# event_number = int(input())
# events = list(map(int, input().split()))
# # first_positive = next((i for i, x in enumerate(events) if x > 0), None)
# recruits = 0
# untreated = 0
# stage = 1
# position = 0
# flag = 0
# while flag < event_number:
#     while stage == 1:
#         if flag < event_number:
#             for index, event in enumerate(events[position:],start=position):
#                 if event < 0:
#                     untreated += 1
#                     flag += 1
#                     if flag == event_number:
#                         break
#                 else:
#                     position = index
#                     stage = 2
#                     break
#             break
#     while stage == 2:
#         for index, event in enumerate(events[position:],start=position):
#             recruits += event
#             flag += 1
#             position = index + 1
#             if recruits == 0:
#                 stage = 1
#                 break
#         if position == event_number:
#             break
# print(untreated)
# # police recruits--solution2
# event_number = int(input())
# events = list(map(int, input().split()))
# recruits = 0
# untreated = 0
# for event in events:
#     recruits = recruits + event
#     if recruits < 0:
#         recruits = 0
#         untreated += 1
# print(untreated)

# # restoring three numbers
# inp = list(map(int,input().split()))
# sum_all = max(inp)
# sum_a_b = min(inp)
# inp.remove(sum_all)
# inp.remove(sum_a_b)
# c = sum_all - sum_a_b
# a = inp[0] - c
# b = inp[1] - c
# print(a,end =" ")
# print(b,end =" ")
# print(c)

# # sum
# tests = int(input())
# inp = [0 for i in range(tests)]
# maximum = [0 for i in range(tests)]
# for test in range(tests):
#     inp[test] = list(map(int, input().split()))
#     maximum[test] = max(inp[test])
#     inp[test].remove(maximum[test])
# for test in range(tests):
#     if maximum[test] == sum(inp[test]):
#         print("Yes")
#     else:
#         print("No")

# # word capitalization
# inp = input()
# capitalized_word = inp[0].upper() + inp[1:]
# print(capitalized_word)

# # helpful maths
# original = input()
# summand = original.split("+")
# summand = list(map(int, summand))
# summand = sorted(summand)
# s = "+".join(map(str, summand))
# print(s)

# # bit++
# statements = int(input())
# x = 0
# statement = ['' for i in range(statements)]
# for index in range(statements):
#     statement[index] = input()
# for index in range(statements):
#     if statement[index] in ["X++" , "++X"]:
#         x = x + 1
#     elif statement[index] in ["X--" , "--X"]:
#         x = x - 1
# result = x
# print(result)

# # hulk
# n = int(input())
# hate = "I hate"
# love = "I love"
# that = "that"
# it = "it"
# string = "I hate"
# for i in range(0,n-1):
#     if i % 2 == 0:
#         string = string+" "+that+" "+love
#     else:
#         string = string+" "+that+" "+hate
# feeling = string + " "+it
# print(feeling)

# # bulbs
# inp = list(map(int,input().split()))
# [buttons, bulbs]=inp
# # 变量预设好
# button = [0 for i in range(buttons)]
# numbers = [0 for k in range(buttons)]
# combined_list= []
# flag = 1
# # 把所有
# for index in range(buttons):
#     button[index]=list(map(int,input().split()))
#     numbers[index]=button[index][1:]
#     combined_list.extend(numbers[index])
# for j in range(bulbs):
#     if (j+1) not in combined_list:
#         flag = 0
# if flag == 0:
#     print("NO")
# else:
#     print("YES")

# # bulbs--solution2
# inp = list(map(int,input().split()))
# [buttons, bulbs]=inp
# lit_bulbs=set()
# for _ in range(buttons):
#     button_info=list(map(int,input().split()))
#     bulb_number = button_info[1:]
#     lit_bulbs.update(bulb_number)
# if len(lit_bulbs)<bulbs:
#     print('NO')
# else:
#     print('YES')

# # the new year: meeting friends
# inp = sorted(list(map(int,input().split())))
# mid= inp[1]
# dist = max(inp)- mid + mid - min(inp)
# print(dist)

# # the new year: meeting friend--solution2
# inp = list(map(int, input().split()))
# dist = max(inp)-min(inp)
# print(dist)

# # 大小写替换02689
# inp = input()
# new_string = ""
# for letter in inp:
#     if letter.islower():
#         new_string += letter.upper()
#     elif letter.isupper():
#         new_string += letter.lower()
#     else:
#         new_string += letter
# print(new_string)
# 这里注意 replace是会把字符串里每个都换掉的

# # way too long words
# tests = int(input())
# for _ in range(tests):
#     inp = input()
#     if len(inp)<=10:
#         print(inp)
#     else:
#         initial = inp[0]
#         last = inp[len(inp)-1]
#         count = len(inp)-2
#         print(initial + f"{count}" + last)
