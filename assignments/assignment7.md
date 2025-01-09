# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by 姜文宜 元培学院



**说明：**

1）⽉考： AC3 <mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

给每个病人一个order，先选出老年人和非老年人，老年人按照年龄倒序排，order按正序排（为了实现这个目标，转化为 n-order），非老年人直接按照order排

代码：

```python
# 病人排队
n= int(input())
patients = [[] for _ in range(n)]
for order in range(n):
    id, age = list(input().split())
    age = int(age)
    reverse_order = n - order
    patients[order] = [reverse_order,id,age]

elder = [patient for patient in patients if patient[2] >= 60]
young = [patient for patient in patients if patient[2] < 60]
elder.sort(key = lambda x: (x[2],x[0]), reverse=True)

output = list(map(lambda x: x[1], elder)) + list(map(lambda x: x[1], young))
for out in output:
    print(out)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-09 13.00.52](/Users/jiangwenyi/Desktop/截屏2024-11-09 13.00.52.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

先还原回正常的矩阵，做运算，再转换回节省存储的矩阵

代码：

```python
# 节省储存的矩阵乘法

n, m1, m2 = map(int, input().split())
# n: n*n的矩阵
# m1：m1行，X矩阵的元素
# m2：m2行，Y矩阵的元素
# 每一行都是三元组：行、列、元素值
# 输出是m3行，代表X和Y两个矩阵乘积中的非0元素的数目，按照先行号后列号的方式递增排序。
# 每行仍然是前述的三元组形式。

# 读取X矩阵的元素值
X = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m1):
    row_X,col_X,item_X = map(int,input().split())
    X[row_X][col_X] = item_X
# 读取Y矩阵的元素值
Y = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m2):
    row_Y,col_Y,item_Y = map(int,input().split())
    Y[row_Y][col_Y] = item_Y

Z = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for a in range(n):
            Z[i][j] += X[i][a] * Y[a][j]
        if Z[i][j] != 0:
            print(i,j,Z[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-11-09 13.03.07](/Users/jiangwenyi/Desktop/截屏2024-11-09 13.03.07.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

首先把所有技能按照t排序，然后每个t之内按照技能掉血量从高到低排序

可以使用字典

然后每个t从头读取，如果技能数超过m，就跳出这个循环进入下一个t，如果b<=0就打印这个t

如果读完了所有t后b还是大于0，打印alive

代码：

```python
# 打怪兽
cases = int(input())
for case in range(cases):

    n, m, b = map(int,input().split())

    skills = []

    for i in range(n):
        t, x = map(int, input().split())
        skills.append((t,x))

    skills.sort()

    count = 0
    skills_simp = {}
    blood = []

    if n > 1:
        for i in range(1,n):
            if skills[i][0] == skills[i-1][0]:
                blood.append(skills[i-1][1])

            else:
                blood.append(skills[i-1][1])
                skills_simp[skills[i-1][0]]= blood
                blood = []

        blood.append(skills[n-1][1])
        skills_simp[skills[n-1][0]] = blood

    else:
        skills_simp[skills[0][0]] = [skills[0][1]]

    flag = 0

    for key in skills_simp:
        skills_simp[key].sort(reverse=True)
        count = 0
        for i in range(len(skills_simp[key])):
            if count < m:
                if b > skills_simp[key][i]:
                    b -= skills_simp[key][i]
                    count += 1
                else:
                    print(key)
                    flag = 1
                    break
            else:
                break

        if flag == 0:
            continue
        if flag == 1:
            break

    if flag == 0:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-09 12.52.09](/Users/jiangwenyi/Desktop/截屏2024-11-09 12.52.09.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

动态规划（一元动态规划）

首先把每个钱数可能换成的硬币个数都写出来，然后从中挑出最小的一个

如果不能换开，那就保持-1

最后看dp[n]

代码：

```python
n, m = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort(reverse = True)
dp = [-1 for _ in range(m+1)]
# 0元不用换
dp[0] = 0

for amount in range(1,m+1):
    possibility = []
    for coin in coins:
        if m >= coin and dp[amount-coin] != -1:
             possibility.append(dp[amount-coin] + 1)

    if possibility == []:
        dp[amount] = -1
    else:
        dp[amount] = min(possibility)

print(dp[m])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-09 12.46.17](/Users/jiangwenyi/Desktop/截屏2024-11-09 12.46.17.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

和罗马数字转换那道题一样，是暴力的一一对应关系

不知道还有没有更好的思路，但是这个思路最好实现

代码：

```python
# 阿尔法星人翻译官
inp = input().split()
alpha = ['zero', 'one', 'two',
         'three', 'four', 'five',
         'six', 'seven', 'eight',
         'nine', 'ten', 'eleven',
         'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen',
         'eighteen', 'nineteen', 'twenty',
         'thirty', 'forty', 'fifty',
         'sixty', 'seventy', 'eighty',
         'ninety', 'hundred', 'thousand', 'million']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100,
          1000, 1000000]
num = 0

if inp[0] == "negative":
    inp = inp[1:]
    if "million" in inp:
        million = inp[:inp.index('million')]
        inp = inp[inp.index('million') + 1:]

        if 'hundred' in million:
            hundred_million = million[:million.index('hundred')]
            million = million[million.index('hundred') + 1:]
            for item in hundred_million:
                id = alpha.index(item)
                num += number[id] * 100000000
        for item in million:
            id = alpha.index(item)
            num += number[id] * 1000000


    if 'thousand' in inp:
        thousand = inp[:inp.index('thousand')]
        inp = inp[inp.index('thousand') + 1:]

        if 'hundred' in thousand:
            hundred_thousand = thousand[:thousand.index('hundred')]
            thousand = thousand[thousand.index('hundred') + 1:]
            for item in hundred_thousand:
                id = alpha.index(item)
                num += number[id] * 100000
        for item in thousand:
            id = alpha.index(item)
            num += number[id] * 1000


    if 'hundred' in inp:
        hundred = inp[:inp.index('hundred')]
        inp = inp[inp.index('hundred') + 1:]

        for item in hundred:
            id = alpha.index(item)
            num += number[id] * 100

    one = inp
    for item in one:
        id = alpha.index(item)
        num += number[id]
    print(-num)


else:
    if "million" in inp:
        million = inp[:inp.index('million')]
        inp = inp[inp.index('million') + 1:]

        if 'hundred' in million:
            hundred_million = million[:million.index('hundred')]
            million = million[million.index('hundred') + 1:]
            for item in hundred_million:
                id = alpha.index(item)
                num += number[id] * 100000000
        for item in million:
            id = alpha.index(item)
            num += number[id] * 1000000

    if 'thousand' in inp:
        thousand = inp[:inp.index('thousand')]
        inp = inp[inp.index('thousand') + 1:]

        if 'hundred' in thousand:
            hundred_thousand = thousand[:thousand.index('hundred')]
            thousand = thousand[thousand.index('hundred') + 1:]
            for item in hundred_thousand:
                id = alpha.index(item)
                num += number[id] * 100000
        for item in thousand:
            id = alpha.index(item)
            num += number[id] * 1000

    if 'hundred' in inp:
        hundred = inp[:inp.index('hundred')]
        inp = inp[inp.index('hundred') + 1:]

        for item in hundred:
            id = alpha.index(item)
            num += number[id] * 100

    one = inp
    for item in one:
        id = alpha.index(item)
        num += number[id]
    print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-09 12.45.02](/Users/jiangwenyi/Desktop/截屏2024-11-09 12.45.02.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

见代码注释

代码：

```python
# 充实的寒假生活
# n个activities
n = int(input())
activities = []
for i in range(n):
    start, end = map(int, input().split())
    activities.append((start, end))

# 按照结束天数从早到晚排列
activities.sort(key = lambda x: x[1])

# 第一个活动总能参加
max_activities = 1
last_end = activities[0][1]
# greedy 方法
# 选结束早的活动
# 比较的结束时间是被选中的活动才需要考虑
for start,end in activities[1:]:
    if start > last_end:
        max_activities += 1
        last_end = end

print(max_activities)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2024-11-09 12.44.18](/Users/jiangwenyi/Desktop/截屏2024-11-09 12.44.18.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

其实“充实的寒假生活”想明白了很简单，就是要尽量选早结束的活动（因为同一段时间里能排多少活动是由每个活动的结束时间决定的，而不是duration，即使duration短，结束时间晚，也会导致结束时间后面的时间被浪费）。开始时间只要晚于前一个活动结束的时间就可以了。不过还没有明白这道题目dp怎么做，ai给了我一个dp的代码，ac了，但是我还没有仔细研究。

现在每日选做在1019。感觉进度越来越慢。可能是因为后面的题目越来越难了。反思一下，可以多看看ai给的代码想明白思路和实现，不一定要每道题目都自己想出来ac，或者看题解里的思路，看别人的代码。学别人的思路也是学习。

换硬币的题是我第一次独立写出了dp代码，感觉蛮有成就感的。

