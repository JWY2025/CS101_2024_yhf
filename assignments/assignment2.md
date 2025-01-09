# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==姜文宜 元培学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：

需要一个变量来记录现在“1”在哪里（行、列）

然后直接行和列分别和3作差就可以了

##### 代码

```python
# beautiful matrix
row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()
row5 = input().split()
row1 = [int(num) for num in row1]
row2 = [int(num) for num in row2]
row3 = [int(num) for num in row3]
row4 = [int(num) for num in row4]
row5 = [int(num) for num in row5]
rows = [row1, row2, row3, row4, row5]
flagrow = 0
flagcol = 0
for rownum in range(0,5):
    if sum(rows[rownum]) != 0:
        flagrow = rownum
flagcol=rows[flagrow].index(1)
moves = abs(flagcol-2) + abs(flagrow-2)
print(moves)

```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-29 23.27.06](/Users/jiangwenyi/Desktop/截屏2024-09-29 23.27.06.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：

如果a本来就可以被b整除那就是0步

如果a不能被b整除，那么就要加上（b-余数）

##### 代码

```python
# divisibilityproblem
tests = int(input())
inp = []
moves = 0
for times in range(tests):
    inp.append(list(map(int,input().split())))
for times in range(tests):
    if inp[times][0] % inp[times][1] == 0:
        moves = 0
    else:
        moves = inp[times][1]-inp[times][0] % inp[times][1]
    print(moves)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-29 23.33.48](/Users/jiangwenyi/Desktop/截屏2024-09-29 23.33.48.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：

recruits这个变量用于储存现在有的人手

每次发生一个案件就会-1；每次招人就会增加相应的量

如果发现recruits这个变量小于0，那么说明出现了untreated crime

但是人手最小也就是0，所以在每次发现recruits变量小于0（也即出现了untreated crime的时候）都要把变量recruits重制为0

##### 代码

```python
# police recruits
event_number = int(input())
events = list(map(int, input().split()))
recruits = 0
untreated = 0
for event in events:
    recruits = recruits + event
    if recruits < 0:
        recruits = 0
        untreated += 1
print(untreated)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-29 23.40.07](/Users/jiangwenyi/Desktop/截屏2024-09-29 23.40.07.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

其实就是取那些地铁区间的并集，从整个区间中减去这个并集中包含的每个点

##### 代码

```python
# 校门外的树
[l,m]=list(map(int,input().split()))
start = [0] * m
end = [0] * m
interval = [0] * m
for i in range(m):
    start[i], end[i] = map(int,input().split())
    interval[i] = set(range(start[i],end[i]+1))
def union_set(*sets):
    return set.union(*sets)
union_intervals = union_set(*interval)
print(l+1-len(union_intervals))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-29 23.51.05](/Users/jiangwenyi/Desktop/截屏2024-09-29 23.51.05.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

现在把800和900的题目做完了，准备开始做1000的题目。

发现自己的一个问题：容易看不清楚嵌套循环什么时候出循环、出循环后读哪一行，于是尝试用笔一行行点着读，好像有点用。

之前题目还比较简单，所以还不怎么需要看书/看网课，可以用ai解决。ai的思路可以借鉴，但是经常会出现一些小问题，自己改正过来就好。之后打算如果碰到难题写不出，可以通过tag里的算法提示来查书/网课/问ai。



