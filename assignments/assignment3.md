# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：

把每个字母都变成字母表顺序的数字编码

然后操作

最后再映射回字母

代码

```python
# 黑神话
k = int(input())
inp = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
case = [0] * len(inp)
new_string = ''
# ind = [len(inp)] * len(inp)
# new_ind = [len(inp)] * len(inp)
for i in range(len(inp)):
    letter = inp[i]
    if letter == '':
        new_letter = letter
    else:
        # 这一段用来记录每个字母的大小写情况
        if not letter.islower():
            case[i] = 1
            # 记录完大小写之后全部变成lowercase在列表里寻找
            letter = letter.lower()
        # 记录一下原来的字母，从1开始编号
        ind = alphabet.find(letter) + 1
        # 变成新的字母（挪k）
        new_ind = ind - k
        # 如果超过26就循环回来
        new_ind = new_ind % 26
        # 然后-1 变成真的索引
        new_letter = alphabet[new_ind-1]
        if case[i] == 1:
            new_letter = new_letter.upper()
    new_string += new_letter
print(new_string)
```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-10 17.59.18](/Users/jiangwenyi/Desktop/截屏2024-10-10 17.59.18.png)

### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：

前两位提取出来

变成数字格式

然后操作

代码

```python
# 字符串中的整数求和
[str1,str2] = input().split()
num1 = int(str1[:2])
num2 = int(str2[:2])
print(num1+num2)

```



代码运行截图 ==（至少包含有"Accepted"）==

![截屏2024-10-10 18.00.49](/Users/jiangwenyi/Desktop/截屏2024-10-10 18.00.49.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：

把前17位和最后一位分开存

然后操作

最后比较

代码

```python
# 验证身份证号
tests = int(input())
for _ in range(tests):
    inp = input()
    numbers = list(map(int,list(inp[:-1])))
    last = str(inp[-1])
    mult = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    mapping = ['1','0','X','9','8','7','6','5','4','3','2']
    z = list(map(lambda x,y : x * y, numbers, mult))
    rem = sum(z) % 11
    if mapping[rem] == last:
        print("YES")
    else:
        print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-10 18.01.51](/Users/jiangwenyi/Desktop/截屏2024-10-10 18.01.51.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：

f-string直接操作

然后print

最后循环外打印结尾

代码

```python

n = int(input())
while n != 1:
    if n % 2 == 1:
        equation = f"{n}*3+1={n*3+1}"
        print(equation)
        n = n * 3 + 1
    else:
        equation = f"{n}/2={n//2}"
        print(equation)
        n = n // 2
print("End")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-10 18.03.04](/Users/jiangwenyi/Desktop/截屏2024-10-10 18.03.04.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：

首先检验是罗马数字还是阿拉伯数字

罗马数字--->阿拉伯数字

直接先转换成每个字母对应的数字

然后相加

最后把带4和9的这些组合处理一下

阿拉伯数字--->罗马数字

先转化为个十百千

然后转化为字母从左到右加到字符串上

##### 代码

```python
# # 罗马数字与整数的转换
inp = input()

rome = ["I","V","X","L","C","D","M","IV","IX","XL","XC","CD","CM"]
arab = [1,5,10,50,100,500,1000,4,9,40,90,400,900]

if not inp[0].isalpha():
    # 是阿拉伯数字
    inp = int(inp)
    rome_string = ''
    # 把每一位的数字都先提取出来
    thousand = 1000 * (inp // 1000)
    inp = inp - thousand
    hundred = 100 * (inp // 100)
    inp = inp - hundred
    ten = 10 * (inp // 10)
    inp = inp - ten
    one = inp
    num = [thousand,hundred,ten,one]
    for digit in num:
        if digit in arab:
            ind = arab.index(digit)
            rome_string += rome[ind]
        else:
            if digit == thousand:
                count = digit // 1000
                rome_string += "M" * count
            elif digit == hundred:
                if digit >= 500:
                    count = (digit - 500) // 100
                    rome_string += "D" + "C" * count
                else:
                    count = digit // 100
                    rome_string += "C" * count
            elif digit == ten:
                if digit >= 50:
                    count = (digit - 50) // 10
                    rome_string += "L" + "X" * count
                else:
                    count = digit // 10
                    rome_string += "X" * count
            elif digit == one:
                if digit >=5:
                    count = (digit - 5)
                    rome_string += "V" + "I" * count
                else:
                    rome_string += "I" * digit
    print(rome_string)
#
else:
    # 是罗马数字
    # inp = inp
    num = []
    for letter in inp:
        num.append(arab[rome.index(letter)])
    arab_number = sum(num)
    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            arab_number -= 2 * num[i]
    print(arab_number)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![截屏2024-10-10 18.05.27](/Users/jiangwenyi/Desktop/截屏2024-10-10 18.05.27.png)

![截屏2024-10-10 18.05.27](/Users/jiangwenyi/Desktop/截屏2024-10-10 18.05.27.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

现在每日选做跟到0927，t-prime那道题的思路很简单，但是实现起来难，学了一招欧拉筛（虽然还是超时但是比原来的朴素方法好多了）

排队这道题思路现在感觉想出来了，但是还需要想怎么实现

现在觉得似乎应该学习一下代码复杂度的计算，之前完全是凭借感觉来优化代码的











