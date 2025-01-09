# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：

逢4闰年，逢10不闰年，逢40又闰年

所以应该使用if循环进行条件分析

##### 代码

```python
#判断闰年02733
year=int(input())
if year % 4 != 0:
    print("N")
elif year % 100 ==0 and year % 400 != 0:
    print("N")
elif year % 400 ==0:
    print("Y")
else:
    print("Y")
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-23 00.12.27](/Users/jiangwenyi/Desktop/截屏2024-09-23 00.12.27.png)

大约花费时间：10min

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：

首先，脚必须是偶数才有解

其次，兔子要最多

##### 代码

```python
# 鸡兔同笼02750
legs = int(input())
if legs % 4 ==0:
    least=legs//4
    most=legs//2
elif legs % 2 ==0:
    least=int((legs-2)/4)+1
    most=legs//2
else:
    least=0
    most=0
print(least,end=" ")
print(most)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-09-23 00.14.57](/Users/jiangwenyi/Desktop/截屏2024-09-23 00.14.57.png)

大约花费时间：30min，因为一开始不熟悉语法

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：

如果行列都是偶数，那么就直接铺满

如果其中有一个奇数，那么可以看作把这一行（列）拿走，把剩下的铺满，再把这一行（列）尽量多地铺上，也就是空1格

##### 代码

```python
# domino piling
input_string = input()
input_m_n=input_string.split()
m = int(input_m_n[0])
n = int(input_m_n[1])
if (m*n) % 2 ==0:
    domino=m*n//2
else:
    domino=(m-1)*n//2+n//2
print(domino)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-23 00.17.44](/Users/jiangwenyi/Desktop/截屏2024-09-23 00.17.44.png)

大约花费时间：20min

### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：

python里strings可以直接比大小

##### 代码

```python
# petya and strings
string1 = input().lower()
string2 = input().lower()
if string1 < string2:
    print(-1)
elif string1 == string2:
    print(0)
else:
    print(1)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-23 00.23.37](/Users/jiangwenyi/Desktop/截屏2024-09-23 00.23.37.png)

大约花费时间：10min，主要是学习一下string可以直接比较大小

### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：

每一行求和，大于等于2就是可作答

需要一个参数来计数，所以要迭代这个参数



##### 代码

```python
# team
question = int(input())
solution = []
answer = 0
for i in range(0,question):
    solution.append(input())
    questioni=solution[i].split(' ')
    for n in range(0,3):
        questioni[n] = int(questioni[n])
    solution[i] = sum(questioni)
    if solution[i] >= 2:
        answer += 1
print(answer)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-09-23 00.25.05](/Users/jiangwenyi/Desktop/截屏2024-09-23 00.25.05.png)

大约花费时间：20min，主要是不熟悉append的用法，for循环开始嵌套读起来不那么容易（做的时候没学会debugger的使用方法）

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

本来一直在看一门python入门网课，想要看完网课再开始自己动手写（感觉得把“武器装备”全都准备好了才能上战场），但是感觉再不开始进度落下太多了，于是网课看了一半就开始通过题目学语法和函数，想要实现什么功能就问ai或者问同学。网课看着看着就忘记了，因为很多功能不是立马用得到，但是还是有用的，因为可以理解代码的逻辑和了解python中的一些功能和函数，搜索的时候可以更有目标，看ai的答案也更加有熟悉感，更好接受。

每日选做现在是在做800难度的题，还剩3道800的题就都做完了。下面准备有机会的话把网课倍速看完，然后接着做900的题目。

昨天做了一道题目，发现方法不同难度显著不同。特别是我的方法涉及到很多break的运用，很容易看不清楚跳出循环后应该运行哪一段代码。发现了（在没有更好的思路的情况下）会用debugger很重要。

