# # theatre square
# [n,m,a] = list(map(int,input().split()))
# import math
# stones = math.ceil(n/a) * math.ceil(m/a)
# print(stones)

# # chat room
# inp: str = input()
#
# # def find_char(s):
# #     chars = {'h', 'e', 'l', 'o'}
# #     return chars.issubset(s)
#
#
# h = inp.find('h')
# e = inp.find('e', h+1)
# l1 = inp.find( 'l',e+1)
# l2 = inp.find('l',l1+1)
# o = inp.find('o',l2+1)
#
#
# if -1 not in [h,e,l1,l2,o]:
#     print("YES")
# else:
#     print("NO")

# # 与7无关的数
# inp = int(input())
# numbers = [num for num in range(1,inp+1) if not (num % 7 == 0 or num//10 ==7 or (num-7) % 10 ==0)]
# print(sum(x**2 for x in numbers))

# # young physicist
# tests = int(input())
# x = [0] * tests
# y = [0] * tests
# z = [0] * tests
# for i in range(tests):
#     [x[i],y[i],z[i]] = list(map(int, input().split()))
# x = sum(x)
# y = sum(y)
# z = sum(z)
# if x == 0 and y == 0 and z == 0:
#     print("YES")
# else:
#     print("NO")

# # young physicist -- solution 2
# tests = int(input())
# vectors = [[]] * tests
# for i in range(tests):
#     vectors[i] = list(map(int,input().split()))
# x = sum(map(lambda vector:vector[0], vectors))
# y = sum(map(lambda vector:vector[1], vectors))
# z = sum(map(lambda vector:vector[2], vectors))
#
# if x == 0 and y == 0 and z == 0:
#     print("YES")
# else:
#     print("NO")

# # 最大公约数
# import math
# while True:
#     try:
#         [x,y] = list(map(int,input().split()))
#         print(math.gcd(x,y))
#     except EOFError:
#         break

# # string task
# inp = input()
# vowels = {'a', 'e', 'i', 'o', 'u','y','A','E','I','O','U','Y'}
# for letter in inp:
#     if letter in vowels:
#         inp = inp.replace(letter,'')
# letters = [letter for letter in inp]
# inp_final = ""
# for letter in letters:
#     inp_final += "."+letter
#     inp_final = inp_final.lower()
# print(inp_final)

# # 矩阵运算
# A_rows, A_cols = map(int, input().split())
# A = [[]] * A_rows
# for i in range(A_rows):
#     A[i]=list(map(int, input().split()))
# B_rows, B_cols = map(int, input().split())
# B = [[]] * B_rows
# for i in range(B_rows):
#     B[i]=list(map(int, input().split()))
# C_rows, C_cols = map(int, input().split())
# C = [[]] * C_rows
# for i in range(C_rows):
#     C[i]=list(map(int, input().split()))
# if A_cols == B_rows and A_rows == C_rows and B_cols == C_cols :
#     D_rows = A_rows
#     D_cols = B_cols
#     D = [[0 for _ in range(D_cols)] for _ in range(D_rows)]
#     # print(D)
#     for i in range(D_rows):
#         for j in range(D_cols):
#             for k in range(A_cols):
#                 D[i][j] += A[i][k] * B[k][j]
#     for i in range(D_rows):
#         for j in range(D_cols):
#             D[i][j] += C[i][j]
#             print(D[i][j],end = " ")
#         print()
# else:
#     print("Error!")

# # lucky division
# num = int(input())
# lucky = [x for x in range(1,1001) if set(list(str(x))).issubset({'4','7'})]
# flag = 0
# for lucky in lucky:
#     if num % lucky == 0:
#         flag = 1
#         print("YES")
#         break
# if flag == 0:
#     print("NO")

# # 求一元二次方程的根
# tests = int(input())
# import math
# for _ in range(tests):
#     a,b,c = map(float,input().split())
#     try:
#         x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
#         x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
#         if x1 == x2:
#             print(f"x1=x2={x1:.5f}")
#         else:
#             print(f'x1={x1:.5f};x2={x2:.5f}')
#     except ValueError:
#         r = (-b) / (2 * a)
#         i = (math.sqrt(4 * a * c - b * b)) / (2 * a)
#         if b != 0:
#             print(f"x1={r:.5f}+{i:.5f}i;x2={r:.5f}-{i:.5f}i")
#         else:
#             print(f"x1={-r:.5f}+{i:.5f}i;x2={-r:.5f}-{i:.5f}i")

# # 邮箱验证
# while True:
#     try:
#         inp = input()
#         position_at = [i for i in range(len(inp)) if inp[i]=="@"]
#         position_dot = [i for i in range(len(inp)) if inp[i]=="."]
#         if (
#                 len(position_at)==1
#                 and position_at[0] != 0
#                 and position_at[0] != len(inp)-1
#                 and len(position_dot)>0
#                 and not 0 in position_dot
#                 and not len(inp) - 1 in position_dot
#                 and "." != inp[inp.find('@') + 1]
#                 and "." != inp[inp.find("@") - 1]
#                 and max(position_dot) > position_at[0]
#
#         ):
#             print('YES')
#         else:
#             print("NO")
#     except EOFError:
#         break

# # 邮箱验证solution2
# while True:
#     try:
#         inp = input()
#         position_at = [i for i in range(len(inp)) if inp[i]=="@"]
#         position_dot = [i for i in range(len(inp)) if inp[i]=="."]
#         if (
#                 len(position_at)==1
#                 and not set(position_at) & {0,len(inp)-1}
#                 and len(position_dot)>0
#                 and not {0,len(inp)-1} & set(position_dot)
#                 and inp[inp.find('@')+1] != "."
#                 and inp[inp.find('@')-1] != "."
#                 and max(position_dot) > position_at[0]
#
#         ):
#             print('YES')
#         else:
#             print("NO")
#     except EOFError:
#         break

