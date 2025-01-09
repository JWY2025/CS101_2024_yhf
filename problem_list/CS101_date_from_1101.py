# 1101
# # basketball exercise
# n = int(input())
# hs1 = list(map(int, input().split()))
# hs2 = list(map(int, input().split()))
# dp = [[0] * 2 for _ in range(n+1)]
# # dp[i][0]：以第一排编号为i的球员结尾的总身高最高的序列
# # dp[i][1]：以第二排编号为i的球员结尾的总身高最高的序列
# for i in range(1,n+1):
#     dp[i][0] = max(dp[i-1][1] + hs1[i-1],dp[i-1][0])
#     dp[i][1] = max(dp[i-1][0] + hs2[i-1], dp[i-1][1])
# print(max(dp[-1]))



# 1102
# Kousuke's Assignment
# 超时了，因为list查找是比较慢的
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     array = list(map(int, input().split()))
#     # 每段beautiful segment都要越早结束越好
#     # 所以维护前缀和序列，找到两个一样的就说明有一个beautiful segment
#     prefixes = [0]
#     count = 0
#     for a in array:
#         current_prefix = a + prefixes[-1]
#         if current_prefix in prefixes:
#             count += 1
#             prefixes.clear()
#             prefixes.append(current_prefix)
#         else:
#             prefixes.append(current_prefix)
#     # print(prefixes)
#     print(count)

#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     array = list(map(int, input().split()))
#     # 每段beautiful segment都要越早结束越好
#     # 所以维护前缀和序列，找到两个一样的就说明有一个beautiful segment
#     current_prefix = 0
#     prefixes = set()
#     prefixes.add(0)
#     count = 0
#     for a in array:
#         current_prefix += a
#         if current_prefix in prefixes:
#             count += 1
#             prefixes.clear()
#             prefixes.add(current_prefix)
#         else:
#             prefixes.add(current_prefix)
#     # print(prefixes)
#     print(count)

# 1103
# 全排列III
#  sequ("", 1 1 3, 3)
# ├── sequ("1", 1 3, 2)
# │   ├── sequ("11", 3, 1)
# │   │   └── sequ("113", , 0) -> 添加 "113" 到结果
# │   └── sequ("13", 1)
# │       └── sequ("131", , 0) -> 添加 "131" 到结果
# ├── sequ("1", 1 3, )
# │   ├── sequ("21", 3)
# │   │   └── sequ("213", 3) -> 添加 "213" 到结果
# │   └── sequ("23", 3)
# │       └── sequ("231", 3) -> 添加 "231" 到结果
# └── sequ("3", 3)
#     ├── sequ("31", 3)
#     │   └── sequ("312", 3) -> 添加 "312" 到结果
#     └── sequ("32", 3)
#         └── sequ("321", 3) -> 添加 "321" 到结果
# 思路参考排序
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

def next_permutation(n,nums):
    for i in reversed(range(n-1)):
        if nums[i]<nums[i+1]:
            i = i
            for j in reversed(range(n)):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i + 1:] = reversed(nums[i + 1:])
                    return nums
            break
        if i == 0 and nums[i] >= nums[i+1]:
            return

def is_non_increasing(n,nums):
    flag = True
    if n <= 1:
        return True
    for _ in range(n-1):
        if nums[_] < nums[_+1]:
            flag = False
            break
    return flag
#
#
n = int(input())
nums = list(map(int,input().split()))
print(*nums)
while not is_non_increasing(n,nums):
    nums = next_permutation(n,nums)
    print(*nums)
#
#
# # 题解的另一种做法
# # 开挂一般的做法 原来python里面有自带的permutations函数
# from itertools import permutations
#
# def generate_permutations(nums):
#     # 使用Python内置的permutations函数生成所有排列
#     all_permutations = set(permutations(nums))
#     # 将排列转换为列表并排序
#     sorted_permutations = sorted(all_permutations)
#     return sorted_permutations
#
#
#
# n = int(input())
# nums = list(map(int, input().split()))
#
# # 生成所有排列
# result = generate_permutations(nums)
#
# # 输出结果
# for perm in result:
#     print(" ".join(map(str, perm)))

# 1105
# 跳高
# Dilworth定理:
# Dilworth定理表明，任何一个有限偏序集的最长反链(即最长下降子序列)的长度，
# 等于将该偏序集划分为尽量少的链(即上升子序列)的最小数量。

# 这道题里可以看成是找最长的递减子序列
# 用dp可以做到
# 很可惜 dp超时了

# n = int(input())
# scores = list(map(int,input().split()))
# dp = [0] + [1]*n
# for i in range(1,n+1):
#     ind_i = i-1
#     for ind_j in range(ind_i):
#         if scores[ind_i] < scores[ind_j]:
#             j = ind_j + 1
#             dp[i] = max(dp[j] + 1, dp[i])
# print(max(dp))

# 解法2
# Dilworth定理:
# Dilworth定理表明，任何一个有限偏序集的最长反链（无法互相比较大小的一组元素）的长度，
# 等于将该偏序集划分为尽量少的链(即一组具有互相的大小关系的元素)的最小数量。
# 这道题目里，链就是一段段非递减的子序列，反链就是一段递减的子序列
# 最少能用多少个链覆盖list（最少需要几个tester） = 最长的反链的长度（最长的递减子序列）

# from bisect import bisect_left
# def min_testers_needed(scores):
#     scores.reverse()  # 反转序列，原来要找的是最长的递减子序列，reverse后=最长的递增的子序列
#     为什么一定要找递增的子序列呢？因为用bisect_left不会有越界的问题，找出的是有没有比当前的这个score更大的尾巴
#     lis = []
#     # 用于存储最长递增子序列
#     # lis里储存的其实是每一个小递减序列的尾巴
#     # 如果出现一个数比原来的某个尾巴小，那么就替换掉比它大一点的那个尾巴，成为新的尾巴（即接到这个尾巴所在的递减序列之后）
#     # 如果出现的这个数比原来的所有尾巴都大，那么成为一个新的递减序列的开始
#
#     for score in scores:
#         pos = bisect_left(lis, score)
#         if pos < len(lis):
#             lis[pos] = score
#         else:
#             lis.append(score)
#
#     return len(lis)
#
#
# N = int(input())
# scores = list(map(int, input().split()))
#
# result = min_testers_needed(scores)
# print(result)


# 1105
# wooden sticks
# Dilworth定理:
# Dilworth定理表明，任何一个有限偏序集的最长反链（无法互相比较大小的一组元素）的长度，
# 等于将该偏序集划分为尽量少的链(即一组具有互相的大小关系的元素)的最小数量。

# 找最少能用多少个非递减的链覆盖这个序列
# 也就是找最长的反链（递减的序列）
# 把输入反过来，找有多少个非递增的链覆盖这个序列
# 也就是找最长的反链（递增的序列）

# from bisect import bisect_left
# def min_minutes_needed(woods):
#     lis = []
#     for wood in woods:
#         pos = bisect_left(lis,wood[1])
#         if pos < len(lis):
#             lis[pos] = wood[1]
#             # print(lis)
#         else:
#             lis.append(wood[1])
#             # print(lis)
#     return len(lis)
#
#
# t= int(input())
#
# for _ in range(t):
#     n = int(input())
#     data = list(map(int,input().split()))
#     woods = []
#     for i in range(0,2*n,2):
#         woods.append([data[i],data[i+1]])
#         woods.sort(key = lambda x:(x[0],x[1]),reverse= True)
#     # print(woods)
#     print(min_minutes_needed(woods))

# 1106
# # 最大子矩阵
# '''
# 为了找到最大的非空子矩阵，可以使用动态规划中的Kadane算法进行扩展来处理二维矩阵。
# 基本思路是将二维问题转化为一维问题：可以计算出从第i行到第j行的列的累计和，
# 这样就得到了一个一维数组。然后对这个一维数组应用Kadane算法，找到最大的子数组和。
# 通过遍历所有可能的行组合，我们可以找到最大的子矩阵。
# '''
# '''
# Kadane算法善于解决“最大子数组问题”：
# 即在一个一维数组中找到一个**连续子数组**，使得这个子数组的元素之和最大。
#
# 如果 current_max + num 大于 num，
# 这意味着将当前元素 num 添加到现有的子数组（由 current_max 表示）中会得到一个更大的和。
# 因此，我们选择继续扩展现有的子数组。
# 如果 current_max + num 小于或等于 num，
# 这表示如果我们将当前元素 num 加入到现有的子数组中，新的和不会比单独的 num 更大。
# 换句话说，现有子数组的和已经变得“负累”，它不会对后续的和产生积极影响。
# 在这种情况下，更好的选择是从当前元素 num 开始一个新的子数组，因为这样有可能找到一个更大的和。
# 通过这种方式，Kadane算法确保了在每一步都做出最优的选择：
# 要么扩展当前的最佳子数组，要么从当前元素重新开始，从而最终能够找到整个数组中的最大子数组和。
# '''
# def kadane(arr):
#     # max_end_here 用于追踪到当前元素为止包含当前元素的最大子数组和
#     # max_so_far 用于储存迄今为止遇到的最大子数组和
#     max_end_here = max_so_far = arr[0]
#     for x in arr[1:]:
#         # 对于每个新元素，我们决定是开始一个新的子数组（仅包含当前元素x）
#         # 还是将当前元素添加到现有的子数组中
#         max_end_here = max(x, max_end_here + x)
#         max_so_far = max(max_so_far, max_end_here)
#     return max_so_far
#
# def max_submatrix(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     max_sum = float('-inf')
#
#     for left in range(cols):
#         temp = [0] * rows
#         for right in range(left,cols):
#             # temp 数组实际上代表了当前选择的列范围内的每一行的总和，因此可以被视为一维数组。
#             for row in range(rows):
#                 temp[row] += matrix[row][right]
#                 # print(temp)
#             max_sum = max(max_sum, kadane(temp))
#     return max_sum
#
# n = int(input())
# nums = []
# matrix = []
# while len(nums) < n**2:
#     nums.extend(input().split())
#     nums = list(map(int, nums))
# for i in range(n):
#     matrix.append(nums[i*n : (i+1)*n])
# # matrix=[list(map(int, nums[i * n:(i+1) * n])) for i in range(n)]
# print(max_submatrix(matrix))

# 1107
# boredom
# 转化为“不相邻数的最大和问题”：因为得到ak分就会删除所有的ak+1和ak-1，所以所有的ak+1和ak-1都不体现在最后的分数里

# 这个代码超时！主要是因为遍历了很多次nums进行每个数字的计数，而另一个代码只遍历了一次nums就完成了计数
# n = int(input())
# nums = list(map(int, input().split()))
#
# # dp[i][0]是不选择当前这个数的最大分数和
# # dp[i][1]是选择当前这个数的最大分数和
# distinct_nums = set(nums)
# max_num = max(distinct_nums)
# num_counts = [[i,0] for i in range(max_num+1)]
#
# for num in distinct_nums:
#     count = 0
#     for i in range(n):
#         if nums[i] == num:
#             count += 1
#     num_counts[num][1] = count
#     # print(num_counts)
# dp = [[0] * 2 for _ in range(len(num_counts)+1)]
# for i in range(1,len(num_counts)+1):
#     ind_i = i-1
#     dp[i][0] = max(dp[i-1][0], dp[i-1][1])
#     dp[i][1] = dp[i-1][0]+ num_counts[ind_i][0] * num_counts[ind_i][1]
#     # print(dp)
# print(max(dp[-1]))

#
# M = int(1e5)
# a = [0] * (M + 1)
# n = int(input())
# for x in map(int, input().split()): a[x] += 1
# dp = [[0, 0] for _ in range(M + 1)]
# # dp[i][0] 不选i, dp[i][1] 选i
# for i in range(1, M + 1):
#     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
#     dp[i][1] = dp[i - 1][0] + a[i] * i
# # print(dp)
# print(max(dp[M][0], dp[M][1]))

# 1108
# piggy-bank
# 是一个dp，有点像cut ribbon，必须完全放满背包
# INF = float("inf")
# t = int(input())
# for _ in range(t):
#     e, f = map(int, input().split())
#     n = int(input())
#     coins = []
#     for i in range(n):
#         p, w = map(int, input().split())
#         coins.append((p,w))
#
#     weight = f - e
#     # 初始化DP数组，dp[j]表示达到重量j所需的最小价值。
#     # 初始时除了dp[0]=0（重量为0可以用价值为0的硬币达到）外，其他都设为无穷大（尚未有解的状态）。
#     dp = [0] + [INF] * weight
#
#     # 动态规划过程：对于每一种硬币，更新所有可用这种硬币达到的重量的价值
#     # 也就是说，每个可以用这种硬币达到的重量，价值都被计算一遍，
#     # 是不是要改变dp[i]的值，要看新的这种硬币更新出来的价值是不是比原来的解法小
#     # dp[i]储存的是重量为i的硬币，最小价值是多少
#     for i in range(n):
#         p, w = coins[i]
#         for j in range(w, weight + 1):
#             # 如果前一个状态是可达的
#             # 更新当前状态为更小的价值
#             if dp[j-w] != INF:
#                 dp[j] = min(dp[j], dp[j-w]+p)
#     if dp[-1] != INF:
#         print(f"The minimum amount of money in the piggy-bank is {dp[-1]}.")
#     else:
#         print("This is impossible.")
#
# INF = float("inf")
# t = int(input())
# for _ in range(t):
#     e, f = map(int, input().split())
#     n = int(input())
#     coins = []
#
#     weight = f - e
#     dp = [0] + [INF] * weight
#
#     for i in range(n):
#         p, w = map(int, input().split())
#         for j in range(w, weight + 1):
#             # 如果前一个状态是可达的
#             # 更新当前状态为更小的价值
#             if dp[j-w] != float(INF):
#                 dp[j] = min(dp[j], dp[j-w]+p)
#     if dp[-1] != INF:
#         print(f"The minimum amount of money in the piggy-bank is {dp[-1]}.")
#     else:
#         print("This is impossible.")

# 1109
# 健身房
# T,n = map(int,input().split())
# exercise = []
# for _ in range(n):
#     t,w = map(int,input().split())
#     exercise.append((t,w))
# dp = [0] + [float("-inf")] * T
# for item in exercise:
#     t = item[0]
#     w = item[1]
#     # 倒过来遍历，可以保证不会连续做两组相同的练习
#     # 也就是说，这样遍历出来最多只加上了一个ti，不会出现后面的被前面已经加上的ti影响的情况
#     for j in range(T,t-1,-1):
#         if dp[j-t] != float("-inf"):
#             dp[j] = max(dp[j], dp[j-t] + w)
#
#
# if dp[-1] != float("-inf"):
#     print(dp[-1])
# else:
#     print(-1)

# 1110
# 波兰表达式
# s = input().split()
# # 当代码执行到 return str(eval(poland() + cur + poland())) 这一行时，
# # 实际上是在说：“我遇到了一个操作符（比如 + 或 *），我现在需要找出它的两个操作数是什么。”
# # 首先，它调用 poland() 来获取第一个操作数。
# # 然后，它使用当前的操作符 cur。
# # 最后，它再次调用 poland() 来获取第二个操作数。
# # 这两次对 poland() 的调用可能会触发更多的递归调用，直到找到实际的数字为止。
# # 一旦所有的递归调用都返回了它们的结果，这些结果就会被传递给 eval 函数进行计算。
# def poland(s):
#     cur = s.pop(0)
#     if cur in "+-*/":
#         return str(eval(poland(s) + cur + poland(s)))
#     else:
#         return cur

# print("%.6f" % float(poland(s)))

# 1111
# 简单的整数划分
# 递归方法
# from functools import lru_cache
# @lru_cache(maxsize=None)
# # integer_sep(n,m) 是 把n划分为最大不超过m的整数的 划分数
# # 其实题目就是要求integer_sep(n,n)
#
# # integer_sep(n,m)的定义域为n.m 均大于0
# def integer_sep(n, m):
#     # 如果划分中的最大不超过1(m=1），那么只有一种划分方式，即n个1
#     # 如果n=1，那么只有一种划分方式，就是1
#     # 目标就是把所有其他的情况都递归到n=1 或m=1的情况上（初始值）
#     # 通过递归的式子不断地去缩小n和m
#     if n == 1 or m == 1:
#         return 1
#     # 如果n<m，因为划分中没有负数，所以最大数肯定不超过n
#     # 所以integer_sep(n,m) = integer_sep(n,n)
#     elif n < m:
#         return integer_sep(n, n)
#     # 如果n=m，那么根据最大数是否达到n分类
#     # 最大数达到n：只有一种划分方式，即{n}
#     # 最大数小于n：最大数不超过n-1，有integer_sep(n,n-1)种划分方式
#     elif n == m:
#         return integer_sep(n, n - 1) + 1
#     # 如果n>m，那么根据最大数是否达到m分类
#     # 最大数达到m: 把m拿走一个，等于把n-m划分为最大数不超过m的划分次数integer_sep(n-m, m)
#     # 最大数没有达到m：那么最大数就不超过m-1 integer_sep(n,m-1)
#     elif n > m:
#         return integer_sep(n,m-1) + integer_sep(n-m, m)
#
# while True:
#     try:
#         n = int(input())
#         print(integer_sep(n, n))
#     except EOFError:
#         break
#
# dp方法
# 完全背包（必须全放满）
# 完全背包问题求的是最大价值，这里是选取物品恰好为n的方法数
# 是一个二维dp，因为同时需要确定被分解的数和分解中的最大数，像小偷背包里的逻辑
# while True:
#     try:
#         n = int(input())
#     except EOFError:
#         break
#
#     dp = [[0] * (n + 1) for _ in range(n+1)]
#
#     # dp[n][m]：被分解的数为n（背包容量为n），分解的最大数不超过m的最多的划分方法
#     # n=0，全设为1，其实是为了让i=j的时候dp[i-j][j] = 1
#     for i in range(1, n+1):
#         dp[i][1] = 1
#         dp[0][i] = 1
#
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i >= j:
#                 dp[i][j] = dp[i-j][j]+dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i][i]
#     print(dp[n][n])

# 1112
# lake counting
# 为了防止栈溢出 sys.setrecursionlimit(20000)
# import sys
# sys.setrecursionlimit(20000)
# n,m = map(int,input().split())
# matrix = [list(input()) for _ in range(n)]
# # 八个方向（adjacent）
# directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
# # 初始化count
# count = 0
# # 这个dfs函数的逻辑是，只要找到一个W，就把它附近的W全部设置为.
# # 因为这样可以标记哪些W已经被计算进同一个湖里了，可以提高效率
# def dfs(x,y):
#     matrix[x][y] = '.'
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx <n and 0 <= ny <m and matrix[nx][ny] != ".":
#             dfs(nx,ny)
#
# # 遍历地图
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == 'W':
#             dfs(i,j)
#             count += 1
# print(count)

# 1113
# strange tower of hanoi
# 没有输入，直接输出n=1-12所有的答案

# 已知：n个盘子，三塔问题，需要 2**n - 1步

# 建立一个dp数组，dp[n]=n个盘子的四塔问题最小移动次数

# 对每个n，解决方法如下：
# 先把上面k个盘子先用四塔问题从A移动到B上，
# 把剩下n-k个盘子当作三塔问题从A移动到D上
# 再把k个盘子当作四塔问题从B移动到D上
# 把k从1-n-1遍历一遍，其中最小的移动次数就是n个盘子的四塔问题最小的移动次数

# 大的n的四塔问题依赖于小的n的四塔问题的最小移动次数，

# INF = float("inf")
# def four_hanoi(n):
#     dp = [INF] + [INF] * n
#
#     dp[1] = 1
#     for i in range(2,n+1):
#         for j in range(1,i):
# # 动态规划在这里
# # 把j个盘子用四塔问题挪到B上 + 把i-j个盘子用三塔问题挪到D上 + 把j个盘子用四塔问题挪到D上 的步数比之前的每一个j的情况都小，那么更新dp[i]
#             dp[i] = min(dp[j] + 2**(i-j) -1 + dp[j], dp[i])
#         # print(dp)
#     return dp
# print(*four_hanoi(12)[1:], sep='\n')


# INF = float("inf")
# def four_hanoi(n):
#     dp = [INF] + [INF] * n
#
#     dp[1] = 1
#     for i in range(2,n+1):
#         for j in range(1,i):
#             dp[i] = min(dp[j] + 2**(i-j) -1 + dp[j], dp[i])
#         # print(dp)
#     return dp[-1]
#
# # print(four_hanoi(3))
# for i in range(1,13):
#     print(four_hanoi(i))

# 1114
# 开餐馆
# import copy
# copy.copy()浅拷贝 copy.deepcopy()深拷贝
# def max_profit(n,k,locations,profits):
#     # 这是创建了一个ps的浅拷贝，对于不可变类型的元素来说没问题（这里是整数，没问题）
#     # dp[i]：到第i个位置为止(只能在前i个位置上开餐厅)，在i位置上开餐厅能获得的最大利润
#     # 为每个地点计算出在其上开餐馆所能获得的最大利润
#     # 在第i个位置上开了餐馆
#     # 之所以可以这么做，是因为动态规划通过隐含的方式处理了某个地方不开店的情况：
#     # 默认不选择：当我们在更新 dp[i] 时，dp[i] 的初始值是 profits[i]，这意味着我们默认选择了在 i 处开店。
#     # 如果我们发现对于某个 j，dp[j] + profits[i] 并不能提供更大的利润，那么 dp[i] 就不会被更新，保持为 profits[i]。
#     # 这相当于在 j 处不开店（或者更准确地说，不在 i 处增加在j处开店的情况下带来的最大额外利润）。
#     # 动态更新：
#     # 如果存在一个 j 使得 dp[j] + profits[i] 比 profits[i] 大，则我们会更新 dp[i]。否则，dp[i] 保持不变。
#     # 这种机制确保了我们总是选择最优解——无论是开店还是不开店。
#     dp = profits[:]
#     for i in range(n):
#         for j in range(i):
#             # 不用sort是因为已经升序排列了
#             if locations[i] - locations[j] > k:
#                 dp[i] = max(dp[i], dp[j] + profits[i])
#     return max(dp)
#
#
# t = int(input())
#
# for _ in range(t):
#     n, k = map(int, input().split())
#     locations = list(map(int, input().split()))
#     # print(ms)
#     profits = list(map(int, input().split()))
#     print(max_profit(n,k,locations,profits))



# def max_profit(n,k,locations,profits):
    # 这是创建了一个ps的浅拷贝，对于不可变类型的元素来说没问题（这里是整数，没问题）
    # dp[i]：可以在前i个位置上开餐馆的（到第i个位置为止）的最大利润，
    # dp[i][0] 遍历到第i个位置，且在第i个位置没开餐馆的最大利润
    # dp[i][1] 遍历到第i个位置，且在第i个位置开了餐馆的最大利润
#     dp = [[0,0] for _ in range(n)]
#     dp[0] = [0,profits[0]]
#     for i in range(1,n):
#         dp[i][0] = max(dp[i-1][1], dp[i-1][0])
#         dp[i][1] = profits[i]
#         for j in range(i):
#             if locations[i] - locations[j] > k:
#                 dp[i][1] = max(dp[j][1] + profits[i], dp[i][1])
#     # print(dp)
#     return max(dp[-1])
#
#
# t = int(input())
#
# for _ in range(t):
#     n, k = map(int, input().split())
#     locations = list(map(int, input().split()))
#     # print(ms)
#     profits = list(map(int, input().split()))
#     print(max_profit(n,k,locations,profits))


# 1115
# 求排列的逆序数
# mergesort算法是一个通过将数组分割成更小的部分（直到每个部分只剩下一个元素）然后对每个部分进行排序
# 然后再将排序后的部分再一遍排序一遍合并为有序的数组

# 分割数列：我们将数列分成两半，直到每个子数列只包含一个元素。
# 递归处理：对于每一个子数列，我们递归地应用这个过程，直到所有的子数列都被单独处理过。
# 合并并计数：当我们开始合并这些有序的子数列时，我们可以同时计算逆序对的数量。
# 在合并过程中，如果我们从右边的子数列中取出一个数（因为右边的数更小），那么意味着左边子数列中剩下的所有数都与这个数构成逆序对。因此，可以立即增加逆序对的计数。
# 如果从左边的子数列中取出一个数，则不会产生新的逆序对，因为我们保持了原来的顺序。
# 重复以上步骤，直到整个数列被合并和排序完成，同时也完成了所有逆序对的计数。
# minimum = 0
# def mergesort(arr):
#     global minimum
#     # 不管对于多小的列表，mergesort的逻辑都是一样的，所以递归调用
#     # 不断分割，直到每个列表只有一个元素
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         mergesort(left)
#         mergesort(right)
#
#         Lptr = Rptr = ptr = 0
#
#         # 请记住，left和right都是排序好的列表！
#         # 合并left和right的同时也在排序和计数逆序对
#         # 如果合并的时候从左边取出一个元素，说明左边的数小于等于右边的，没有形成逆序对
#         # 如果合并的时候从右边取出一个元素，说明右边的数小于左边的，形成了逆序对
#         # 而且在left中之后的元素都会和这个元素形成逆序对
#         while len(left) > Lptr and len(right) > Rptr:
#             if left[Lptr] <= right[Rptr]:
#                 arr[ptr] = left[Lptr]
#                 Lptr += 1
#             else:
#                 arr[ptr] = right[Rptr]
#                 Rptr += 1
#                 minimum += len(left) - Lptr
#             ptr += 1
#         # 处理left和right里可能有的剩下的元素（一个列表已经处理完了但是另一个还有剩下的）
#         # 把它们往排序后的列表的最后放
#         while len(left) > Lptr:
#             arr[ptr] = left[Lptr]
#             ptr += 1
#             Lptr += 1
#         while len(right) > Rptr:
#             arr[ptr] = right[Rptr]
#             ptr += 1
#             Rptr += 1
#
# n = int(input())
# arr = list(map(int, input().split()))
# mergesort(arr)
# print(minimum)

# 1116
# aggressive cows
# 检查在给定最小距离 min_distance 下是否可以放置 C 头奶牛
# def can_place_cows(stalls, C, min_distance):
#     # 假设第一头奶牛放在第一个牛棚中
#     last_position = stalls[0]
#     count = 1  # 已经放置了一头奶牛
#
#     # 尝试根据 min_distance 放置剩余的奶牛
#     for i in range(1, len(stalls)):
#         # 如果当前牛棚和上一个放置奶牛的牛棚之间的距离 >= min_distance
#         if stalls[i] - last_position >= min_distance:
#             count += 1  # 放置一头新的奶牛
#             last_position = stalls[i]  # 更新最后放置奶牛的位置
#
#             # 如果已经成功放置了 C 头奶牛，返回 True 表示可以
#             if count == C:
#                 return True
#     # 如果循环结束后未能放置 C 头奶牛，返回 False
#     return False
#
#
# # 主函数：用二分查找计算最大可能的最小距离
# def max_minimum_distance(stalls, C):
#     # 对所有牛棚位置进行排序，确保我们可以按顺序考虑它们
#     stalls.sort()
#
#     # 初始化二分查找的边界
#     low, high = 1, stalls[-1] - stalls[0]  # 最小和最大可能的距离
#     result = 0  # 记录找到的 最大的【最小距离】
#
#     # 开始二分查找
#     while low <= high:
#         mid = (low + high) // 2  # 计算中间值作为当前尝试的最小距离
#
#         # 如果可以在 mid 距离下放置所有的奶牛
#         if can_place_cows(stalls, C, mid):
#             result = mid  # 更新结果为这个有效的距离
#             low = mid + 1  # 尝试更大的最小距离
#         else:
#             high = mid - 1  # 否则，尝试更小的最小距离
#
#     # 返回最终找到的最大最小距离
#     return result
#
#
# # 读取输入数据
# import sys
#
# input = sys.stdin.read
# data = input().split()
#
# # 解析输入的数据
# N = int(data[0])  # 牛棚的数量
# C = int(data[1])  # 奶牛的数量
# stalls = [int(data[i]) for i in range(2, N + 2)]  # 牛棚的位置列表
#
# # 调用主函数解决问题并打印答案
# print(max_minimum_distance(stalls, C))

# 1117
# 不同路径
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         # 创建一个二维数组 dp 来存储到达每个位置的路径数
#         # 初始化为1，是因为边缘上（编号为0的行和列都只能是左边或者上面走来的，只有1条路）
#         dp = [[0] * n for _ in range(m)]
#         dp[0] = [1] * n
#         for i in range(1,m):
#             dp[i][0] = 1
#         # 动态规划填表
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#
#         # 返回右下角的值，即从左上角到右下角的不同路径数
#         return dp[-1][-1]
#
# m, n = map(int, input().split())
#
# # 创建解决方案实例并调用方法
# solution = Solution()
# ans = solution.uniquePaths(m, n)
#
# print(ans)

# 1118
# 螺旋矩阵
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         # 这句话是为了保证[]和[[]]的情况会直接输出空列表
#         if not matrix or not matrix[0]:
#             return list()
#
#         rows, columns = len(matrix), len(matrix[0])
#         visited = [[False] * columns for _ in range(rows)]
#         total = rows * columns
#         order = [0] * total
#         # 右->下->左->上 四个方向循环
#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         row, column = 0, 0
#         # 转向的指示
#         directionIndex = 0
#         for i in range(total):
#             order[i] = matrix[row][column]
#             visited[row][column] = True
#             nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
#             if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
#                 directionIndex = (directionIndex + 1) % 4
#             row += directions[directionIndex][0]
#             column += directions[directionIndex][1]
#         return order

# 1119
# 无重复字符的最长子串
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 初始化变量
#         start = -1  # 当前无重复子串的起始位置的前一个位置
#         max_length = 0  # 最长无重复子串的长度
#         char_index = {}  # 字典，记录每个字符最近一次出现的位置
#
#         # 遍历字符串
#         for i, char in enumerate(s):
#             # 如果字符之前出现过（在char_index里）
#             # 且上次出现是在这个子串中（位置大于当前无重复子串的起始位置的前一个位置）
#             # 那么当前子串里有重复的字符了
#             # 应该从当前这个字符开始寻找新的子串
#             if char in char_index and char_index[char] > start:
#                 # 更新起始位置为该字符上次出现的位置
#                 start = char_index[char]
#
#             # 更新字典中这个字符最后一次出现的位置
#             char_index[char] = i
#
#             # 计算当前无重复子串的长度，并更新最大长度
#             current_length = i - start
#             max_length = max(max_length, current_length)
#
#         return max_length

# 1120
# 摆动子序列
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         up = down = 1
#
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 up = down + 1
#             elif nums[i] < nums[i - 1]:
#                 down = up + 1
#
#         return max(up, down)

# 1121
# 接雨水
# dp
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
#         # 首先从左往右遍历，可以得到第i个柱子左边（包括自身）最高的柱子高度
#         # 然后从右往左遍历，可以得到第i个柱子右边（包括自身）最高的柱子高度
#         # 这里的dp体现在如果碰到了更高的柱子，就更新左边（or右边）最高的柱子高度
#         n = len(height)
#         leftMax = [height[0]] + [0] * (n - 1)
#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i - 1], height[i])
#
#         rightMax = [0] * (n - 1) + [height[n - 1]]
#         for i in range(n - 2, -1, -1):
#             rightMax[i] = max(rightMax[i + 1], height[i])
#         # 每个位置i上能储存的雨水就是它左边和它右边（包括自己）最高的柱子中更小的那个的高度 - 自己的高度（底为1）
#         # 如果自己是最高的，那么就存不住雨水
#         ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
#         return ans

# 1122
# 对于每个位置i的孩子来说：
# 左规则：如果第i-1个孩子<第i个孩子，sweet[i] >= sweet[i-1]+1
# 右规则：如果第i个孩子>第i+1个孩子，sweet[i] >= sweet[i+1]+1
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         # 从左遍历，每一个学生分别满足左规则时，最少需要被分得的糖果数量
#         left = [0] * n
#         for i in range(n):
#             if i > 0 and ratings[i] > ratings[i - 1]:
#                 left[i] = left[i - 1] + 1
#             # 如果第i个没有比左边的大，那么赋值1
#             else:
#                 left[i] = 1
#         # 从右向左，每一个学生分别满足右规则时，最少需要被分得的糖果数量
#         ret = 0
#         right = [0] * n
#         for i in range(n - 1, -1, -1):
#             if i < n - 1 and ratings[i] > ratings[i + 1]:
#                 right[i] = right[i + 1] + 1
#             # 如果
#             else:
#                 right[i] = 1
#             # 左规则和右规则同时满足：取left和right里更大的那个
#             ret += max(left[i], right[i])
#
#         return ret

# 1123
# 搜索二维矩阵
# 其实应该把二维矩阵拉直成为一维的数组，然后二分查找
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
#
#         m, n = len(matrix), len(matrix[0])
#         left, right = 0, m*n-1
#         while left <= right:
#             mid = (left + right) // 2
#             mid_value = matrix[mid//n][mid%n]
#             if mid_value == target:
#                 return True
#             if mid_value > target:
#                 right = mid-1
#             elif mid_value < target:
#                 left = mid+1
#         return False

# 1124
# 在排序数组中查找元素的第一个和最后一个位置
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         import bisect
#         left = bisect.bisect_left(nums,target)
#         right = bisect.bisect_right(nums,target)
#         if left == right:
#             return [-1,-1]
#         return [left,right-1]

# 1125
# # k-tree
# # dp
# n,k,d=map(int,input().split())
# mod = 10**9 + 7
# # 正难则反：至少有一条边>=d --> 每条边都<d
# # A[i]：总权重为i的路径数 ； B[i]：总权重为i且所有边权重小于d的路径数
# # 当i=0时，只有一条路（什么边都不选）
# A = [1] + [0] * n
# B = [1] + [0] * n
# # 路径数本质上就是整数划分问题
# # 本题:用不大于k的正整数划分i（总权重为i的路径）数-用小于d的正整数划分i（总权重为i且每条边权重都小于0的路径）数
# # 选A[i]的边的时候，可以看作是先选了A[i-j]的路径，然后加上了一条权重为j的路
# # （对于每条路径来说，都是从结束的节点往下走一条权重为j的路，所以A[i]就是从0开始一个个加上A[i-j]的数量）
# for i in range(1, n + 1):
#     for j in range(1, min(i,k)+1):
#         A[i] = (A[i] + A[i - j]) % mod
#     for j in range(1, min(d, i + 1)):
#         B[i] = (B[i] + B[i - j]) % mod
# print((A[n] - B[n]) % mod)

# dfs递归做法
# MOD = 1000000007
# from functools import lru_cache
# @lru_cache(maxsize=None)
# # n：剩余的总权重，每次执行会递减
# # b：当前递归分支路径中最大的边权重，应该随着路径的深入更新
# def dfs(n, b):
#     # 如果剩余权重n为0（正好分配完），最大边权重b>=d，说明找到了
#     if n == 0 and b >= d:
#         return 1
#     # 如果剩余的总权重小于0，则没有找到符合条件的路径。
#     if n < 0:
#         return 0
#
#     ans = 0
#     # 尝试添加权重从1到k的边(当前路径结束在的这个节点往下只有一条权重为i的边）
#     # 然后从新的节点开始递归地继续搜索剩余的总权重
#     # i是当前考虑添加到路径中的边的权重。b是到目前为止，在当前递归分支中已经遇到的最大边权重
#     for i in range(1, k + 1):
#         max_weight = max(b,i)
#         ans = (ans + dfs(n - i, max_weight)) % MOD
#
#     return ans
#
# # k-tree，权重为n的路径，至少有一条边>=d
# n, k, d = map(int, input().split())
# print(dfs(n, 1))

# 1126
# 核电站
# dp
# n,m = map(int,input().split())
# dp = [0] * (n+1)
# dp[0] = 1
# # dp[i]：到第i个坑为止的放置不会爆炸的方法数
# for i in range(1,n+1):
#     if i < m:
#         # 第i个坑里可以放/不放，乘2
#         dp[i] = 2 * dp[i-1]
#     elif i == m:
#         # 减去一个m个坑全放上的情况
#         dp[i] = 2 * dp[i-1] - 1
#     else:
#         # 2 * dp[i-1] 是不考虑炸的情况
#         # 减去在i处放就炸了的情况
#         # 如果在i处放上就炸了，那么就是i前面m-1个坑都放上了，且i-m处没有放（要不然在之前就已经炸了）
#         # 所以只要前i-m-1个坑的放置情况数 = 在i处放上就炸了的情况数
#         dp[i] = 2 * dp[i-1] - dp[i-m-1]
# print(dp[-1])

# 递归
# from functools import lru_cache
# @lru_cache(maxsize=None)
# # i：第i个坑
# # j：连续j个坑放了物质
# # n：总共n个坑
# # m：最多连续放m个坑
# def dfs(i, j, n, m):
#     # 这两步if不能换！必须先判断不会炸，才能放第n个坑
#     if j == m:
#         return 0  # 如果有连续的m个坑都有物质，此方案不可行
#     if i == n:
#         return 1  # 如果能到n，说明之前没有连续的m个坑都有物质，此方案可行
#
#     # 不在第i个坑放置物质
#     no_place = dfs(i + 1, 0, n, m)
#     # 在第i个坑放置物质
#     place = dfs(i + 1, j + 1, n, m)
#
#     # 计算总数
#     return no_place + place
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     result = dfs(0, 0, n, m)
#     print(result)

# 1127
# # 数楼梯
# n = int(input())
# if n > 1:
#     dp = [0] * n
#     dp[0] = 1
#     dp[1] = 2
#     for i in range(2,n):
#         dp[i] = dp[i-1] + dp[i-2]
#     print(dp[-1])
# else:
#     print(1)

# 1128
# flowers
# MOD = 1000000007  # 定义模数，用于防止整数溢出。
#
# # 读取测试用例数量t和白花的最小分组大小k。
# t, k = map(int, input().split())
#
# # 初始化dp数组，dp[i]表示吃恰好i朵花的方法总数。
# MAXN = 100001  # 预定义最大值以优化查询速度。
# dp = [0] * MAXN
# dp[0] = 1  # 基础情况：有一种方式让Marmot不吃任何花。
#
# # 初始化s数组，用于快速计算区间内的总和。
# s = [0] * MAXN
#
# # 动态规划填充dp数组。
# for i in range(1, MAXN):
#     if i >= 1:
#         dp[i] = dp[i - 1]  # 可以选择在i-1朵花的基础上加一朵红花。这种选择的情况就是i-1朵花的情况方法数。
#     if i >= k:
#         dp[i] = (dp[i] + dp[i - k]) % MOD  # 也可以选择在i-k朵花的基础上加一组白花。这种选择的情况就是i-k朵花的方法数。
#
#     # 更新累积和数组。
#     s[i] = (s[i - 1] + dp[i]) % MOD
#
# # 处理t次查询。
# results = []
# for _ in range(t):
#     a, b = map(int, input().split())
#     # 对于每次查询，快速计算区间[a, b]内吃花的方法总数。
#     result = (s[b] - s[a - 1] + MOD) % MOD
#     results.append(result)
#
# # 输出所有查询的结果。
# for result in results:
#     print(result)


# 1129
# 最佳凑单
# n, v = map(int, input().split()) # 商品数，凑单价
# a = list(map(int, input().split())) # 商品价格
# sum_a = sum(a)
#
# dp = [[-1] * (sum_a + 1) for _ in range(n + 1)]
# dp[0][0] = 0
# # dp[i][j]：到第i个商品为止，凑出价格为j的方法数
# # -1代表抽不出这样的方法
# if n > 1:
#     for i in range(1, n + 1):  # 商品数
#         for j in range(sum_a + 1):  # 价格
#             # 第i个商品的价格为a[i-1]
#             if a[i - 1] <= j and dp[i-1][j-a[i-1]] >= 0:
#                 # 第i个商品的价格 a[i] <= j，那么可以拿上这个商品也可以不拿上这个商品
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][ j - a[i - 1] ] + 1)
#             else:
#                 # 第i个商品的价格a[i] > j 或者 dp[i-1][j-a[i-1]] < 0（即 j-a[i-1] 的价格在之前i-1中取不到）
#                 dp[i][j] = dp[i - 1][j]
#     # print(dp)
#     if sum_a < v:
#         print("0")
#     else:
#         for k in range(v,sum_a+1):
#             if dp[n][k] > 0:
#                 print(k)
#                 break
# else:
#     if a[0] < v:
#         print(0)
#         exit()
#     if a[0] >= v:
#         print(a[0])
#         exit()

# 超强短代码版
# 稀疏桶
# a, b = map(int, input().split())
# c = {0}
# for i in map(int, input().split()):
#     for j in c.copy():
#         if j < b: c.add(i + j)
# for i in sorted(c):
#     if i >= b: print(i);exit()
# print(0)


# 1130
# 宠物小精灵之收服
# N: 精灵球数量
# M：皮卡丘的初始体力
# K：野生小精灵的数量
N, M, K = map(int, input().split())

# 初始化DP数组
# dp[i][j]为有i个精灵球、捕捉了j个小精灵后，皮卡丘最小的消耗体力
# inf代表不可达状态（即剩余i个精灵球不能收服j个小精灵）
dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0  # 当不收服任何小精灵时，皮卡丘的体力消耗为0

'''
这里需要说明一下，这其实是个三维背包问题，但是用滚动数组压缩了一维之后，dp变成了二维数组
这里滚动i，其实就是每次处理第i个物品要不要选择的问题
每次面对第i个物品，我们都面临是不是要选择它
如果选择了就要更新dp
如果没选择就保持原样
如果从小到大遍历r和j，因为r、j大的依赖于r、j小的，
如果r、j小的被更新过，相当于已经在那个情况下选择过第i个小精灵了
如果再更新r、j大的，那么相当于重复选择了第i个小精灵
'''

# 读取每个小精灵的信息
# 当前是第i个小精灵
for i in range(1, K + 1):
    # u: 收服这个小精灵需要u个精灵球
    # v：收服这个小精灵消耗v个体力值
    u, v = map(int, input().split())

    # 有j = u～N个精灵球都可以考虑捕捉当前小精灵
    for j in range(N, u-1, -1):
        # 可以捕获r = 0～i 个小精灵
        # r = 0 的情况在初始化dp的时候已经赋值过0了
        for r in range(i, 0, -1):
            if dp[j - u][r - 1] != float('inf'):
                dp[j][r] = min(dp[j][r], dp[j - u][r - 1] + v)

# 找到最大收服数量
max_captured = 0
max_reserved_energy = M
for i in range(K, -1, -1):
    if dp[N][i] < M:
        max_captured = i
        max_reserved_energy = M - dp[N][i]
        break

# 输出结果
print(max_captured, max_reserved_energy)
