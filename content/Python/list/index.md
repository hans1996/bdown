---
authors:
- admin
categories: []
date: "2019-02-05T00:00:00Z"
draft: false
featured: false
image:
  caption: ""
  focal_point: ""
projects: []
subtitle: Learn how to blog in Academic using Jupyter notebooks
summary: Learn how to blog in Academic using Jupyter notebooks
tags: []
title: Display Jupyter Notebooks with Academic
---


```python
a=[9,"中山","math",2.5,[2,8]]
a[-5]
a[0]
```




    9




```python
b = [[1,2],[9,4,5]]
c = b[0][1]
d=b[1][0]
e=len(b)
f= len(b[1])
print("c=",c)
print("d=",d)
print("e=",e)
print("f=",f)
```

    c= 2
    d= 9
    e= 2
    f= 3
    


```python
a =[1,2,3,4,5]
a[1:-1]=a
a[1:-1]=[]
print(a)
```

    [1, 5]
    


```python
a=[1,2]
b = a
b=b+[3]
a

```




    [1, 2]




```python
a=[1,2]
b = a
b+=[3]
a
```




    [1, 2, 3]




```python
import copy
a = [1, 2, 3, 4, ['a', 'b']] #原始对象
 
b = a                       #赋值，传对象的引用
c = copy.copy(a)            #对象拷贝，浅拷贝
d = copy.deepcopy(a)        #对象拷贝，深拷贝
 
a.append(5)                 #修改对象a
a[4].append('c')            #修改对象a中的['a', 'b']数组对象
 
print( 'a = ', a )
print( 'b = ', b )
print( 'c = ', c )
print( 'd = ', d )
```

    a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
    c =  [1, 2, 3, 4, ['a', 'b', 'c']]
    d =  [1, 2, 3, 4, ['a', 'b']]
    


```python
### list comprehension
# 一般寫法

arr1 = []

for i in range(10):
    arr1.append(i)

print(arr1)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
# in-place construction
arr1 = [i for i in range(10)]

print(arr1)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
# in-place construction
arr1 = [i for i in range(10)]

# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]

# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 2, 4, 6, 8]
    [3, 5, 7, 9]
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
    


```python
[x for x in range(4)]
[t*t for t in [1,2,3]]
[[x,x*x] for x in range(3)]
[x for x in range(10) if x not in [3,4,5]]
[[x,x*x] for x in range(4) if x//3]
```




    [[3, 9]]




```python

###############################



a=[3,4]
b=[a]*2
a[1]=8
b
```




    [[3, 8], [3, 8]]




```python
a=[3,4]
b=a[:]*2
a[1]=8
b
```




    [3, 4, 3, 4]




```python
#for 迴圈與串列
```


```python
b =[[1],[8,2],[4,3,3]]
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j],end=" ")
    print()
```

    1 
    8 2 
    4 3 3 
    


```python
#同上
b =[[1],[8,2],[4,3,3]]
for p in b:
    for x in p:
        print(x,end=" ")
    print()
```

    1 
    8 2 
    4 3 3 
    


```python
#同上
for p in [[1],[8,2],[4,3,3]]:
    for x in p:
        print(x,end=" ")
    print()
```

    1 
    8 2 
    4 3 3 
    


```python
#for 迴圈更改 串列元素
```


```python
a =[1,8,3]
for i in range(len(a)):
    a[i]+=10
print(a)
```

    [11, 18, 13]
    


```python
a =[1,8,3]
for x in a:
    x+=10
print(a)
```

    [1, 8, 3]
    


```python
b=[[1],[5,8],[3,4]]
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j]+=10
print(b)
```

    [[11], [15, 18], [13, 14]]
    


```python
b=[[1],[5,8],[3,4]]
for p in b:
    for i in range(len(p)):
        p[i]+=10
print(b)
```

    [[11], [15, 18], [13, 14]]
    


```python
#有誤
b=[[1],[5,8],[3,4]]
for p in b:
    for x in p:
        x +=10
print(b)
```

    [[1], [5, 8], [3, 4]]
    


```python
#字串分解成字元串列
```


```python
list("abc")
```




    ['a', 'b', 'c']




```python
list("123")
```




    ['1', '2', '3']




```python
n=423
a=[int(x) for x in list(str(n))]
a
```




    [4, 2, 3]




```python
#使用index取出下標
```


```python
dirs=["west","north","west","south"]
dirs.index("west")
```




    0




```python
for d in dirs:
    print(d,dirs.index(d),sep=":",end=" ")
```

    west:0 north:1 west:0 south:3 


```python
####tuple##
```


```python
(one,two,three)=(1,2,3)
three
```




    3




```python
[one,two,three]=[1,2,3]
three
```




    3




```python
a=(4,5,6)
(four,five,six) = a
six
```




    6




```python
###小括號省略

one ,two =1,2
two
```




    2




```python
from random import*
```


```python
nums = [uniform(-1,1) for i in range(4)]
for x in nums : print(x)
```

    0.4867200676882866
    0.6229973999177287
    -0.5681957844554919
    0.39087687240861757
    


```python
nums = [uniform(-1,1) for i in range(4)]
print(nums)
```

    [-0.5903251082623902, 0.3351431014940154, -0.5958451499766018, 0.568850457028085]
    


```python
## 10 人擲骰子'

import random

foo = [random.randint(1,6) for i in range(10)]
print(foo)
```

    [6, 1, 6, 3, 1, 3, 4, 5, 5, 1]
    


```python
# 10個號碼隨意分給4個人,每人2球
balls=list(range(1,11))

#打亂順序

random.shuffle(balls)
print(balls)
#分給4人,美人2球
pno,m=4,2

for i in range(pno):
    print(i+1,end=": ")
    for x in balls[i*m:i*m+m]:
        print(x,end=" ")
    print()
```

    [4, 7, 9, 8, 2, 3, 5, 10, 1, 6]
    1: 4 7 
    2: 9 8 
    3: 2 3 
    4: 5 10 
    


```python
#三人各擲四次色子

dices = "牛馬獅虎龍鳳"

#3人任意投擲4次

pno , m = 3 ,4

for p in range(pno):
    print(p+1,end=": ")
    
    for k in range(m):
        print(random.choice(dices),end=" ")
    print()
```

    1: 馬 馬 獅 馬 
    2: 獅 鳳 馬 牛 
    3: 鳳 牛 牛 馬 
    


```python
import random 

while True :

	# 斜條線數量
	n = int( input("> ") )

	# m 最長直線高
	# w 直條圖寬 
	m , w = 9 , 3

	# 使用亂數設定各直條線長
	vals = [ random.randint(1,m) for i in range(1,n+1) ]

	# 畫直條線
	for s in range(m,0,-1) :
		
		for val in vals :

			if s > val :
				print( " "*w , end=" " )
			elif s == val :
				print( "\\" + str(val) + "/" , end=" " )
			else :
				print( " | " , end=" " )

		print() 

	# 畫底部等號
	print( "="*( (w+1)*n - 1) )

```

    > 10
    \9/                                     
     |          \8/                         
     |           |                  \7/     
     |           |          \6/ \6/  |      
     |           |  \5/      |   |   |      
     |           |   |       |   |   |      
     |           |   |       |   |   |  \3/ 
     |  \2/      |   |  \2/  |   |   |   |  
     |   |  \1/  |   |   |   |   |   |   |  
    =======================================
    > -1
    
    
    
    
    
    
    
    
    
    
    > 10
                                \9/         
                                 |          
                        \7/      |  \7/     
            \6/          |       |   |      
        \5/  |           |       |   |      
         |   |      \4/  |       |   |      
         |   |       |   |  \3/  |   |  \3/ 
    \2/  |   |  \2/  |   |   |   |   |   |  
     |   |   |   |   |   |   |   |   |   |  
    =======================================
    


```python
1+1

```


```python
from random import *

n , total = 5 , 50000

counts = [ 0 for x in range(n+1) ]

for k in range(total) :

    # 起始落下的位置
    ball_pos = 2*randint(1,n) - 1

    # 第一層釘子
    move = 2*randint(0,1) - 1
    ball_pos += move 

    # 第二到第五層釘子
    for i in range(2) :
        
        move = 2*randint(0,1) - 1
        ball_pos += move 

        # 碰到兩側，提前離開
        if ball_pos < 0 or ball_pos > 2*n : break 

        move = 2*randint(0,1) - 1
        ball_pos += move 

    # 球數統計
    if ball_pos < 0 : 
        counts[0] += 1
    elif ball_pos > 2*n :
        counts[-1] += 1
    else :
        counts[ball_pos//2] += 1

# 列印
for no in counts :
    s = int(160*no/total+0.5)
    print(str(s)+"/160",end=" ")

print()        

```

    24/160 25/160 31/160 31/160 25/160 24/160 
    
