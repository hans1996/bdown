
# coding: utf-8

# In[3]:


a=[9,"中山","math",2.5,[2,8]]
a[-5]
a[0]


# In[13]:


b = [[1,2],[9,4,5]]
c = b[0][1]
d=b[1][0]
e=len(b)
f= len(b[1])
print("c=",c)
print("d=",d)
print("e=",e)
print("f=",f)


# In[18]:


a =[1,2,3,4,5]
a[1:-1]=a
a[1:-1]=[]
print(a)


# In[30]:


a=[1,2]
b = a
b=b+[3]
a


# In[31]:


a=[1,2]
b = a
b+=[3]
a


# In[32]:


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


# In[70]:


### list comprehension
# 一般寫法

arr1 = []

for i in range(10):
    arr1.append(i)

print(arr1)


# In[71]:


# in-place construction
arr1 = [i for i in range(10)]

print(arr1)


# In[72]:


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


# In[41]:


[x for x in range(4)]
[t*t for t in [1,2,3]]
[[x,x*x] for x in range(3)]
[x for x in range(10) if x not in [3,4,5]]
[[x,x*x] for x in range(4) if x//3]


# In[42]:



###############################



a=[3,4]
b=[a]*2
a[1]=8
b


# In[43]:


a=[3,4]
b=a[:]*2
a[1]=8
b


# In[ ]:


#for 迴圈與串列


# In[45]:


b =[[1],[8,2],[4,3,3]]
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j],end=" ")
    print()


# In[51]:


#同上
b =[[1],[8,2],[4,3,3]]
for p in b:
    for x in p:
        print(x,end=" ")
    print()


# In[48]:


#同上
for p in [[1],[8,2],[4,3,3]]:
    for x in p:
        print(x,end=" ")
    print()


# In[ ]:


#for 迴圈更改 串列元素


# In[50]:


a =[1,8,3]
for i in range(len(a)):
    a[i]+=10
print(a)


# In[52]:


a =[1,8,3]
for x in a:
    x+=10
print(a)


# In[57]:


b=[[1],[5,8],[3,4]]
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j]+=10
print(b)


# In[58]:


b=[[1],[5,8],[3,4]]
for p in b:
    for i in range(len(p)):
        p[i]+=10
print(b)


# In[61]:


#有誤
b=[[1],[5,8],[3,4]]
for p in b:
    for x in p:
        x +=10
print(b)


# In[ ]:


#字串分解成字元串列


# In[62]:


list("abc")


# In[63]:


list("123")

n=423
a=[int(x) for x in list(str(n))]
a
# In[ ]:


#使用index取出下標


# In[2]:


dirs=["west","north","west","south"]
dirs.index("west")


# In[68]:


for d in dirs:
    print(d,dirs.index(d),sep=":",end=" ")


# In[ ]:


####tuple##


# In[74]:


(one,two,three)=(1,2,3)
three


# In[75]:


[one,two,three]=[1,2,3]
three


# In[76]:


a=(4,5,6)
(four,five,six) = a
six


# In[77]:


###小括號省略

one ,two =1,2
two


# In[79]:


from random import*


# In[82]:


nums = [uniform(-1,1) for i in range(4)]
for x in nums : print(x)


# In[85]:


nums = [uniform(-1,1) for i in range(4)]
print(nums)


# In[88]:


## 10 人擲骰子'

import random

foo = [random.randint(1,6) for i in range(10)]
print(foo)


# In[100]:


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


# In[101]:


#三人各擲四次色子

dices = "牛馬獅虎龍鳳"

#3人任意投擲4次

pno , m = 3 ,4

for p in range(pno):
    print(p+1,end=": ")
    
    for k in range(m):
        print(random.choice(dices),end=" ")
    print()


# In[ ]:


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


# In[ ]:


1+1


# In[10]:


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

