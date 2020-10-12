# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/12 0012 9:53
#lst=['hello','world',98,'hello']
'''print(lst.index('hello')) #如果列表中有相同元素只返回列表中相同元素的第一个元素索引
print(lst.index('hello',1,4))#在指定范围内查找相应元素'''


''' #获取索引为2的元素
print(lst[2])
#获取索引为-3的元素
print(lst[-3])
'''

lst=[10,20,30,40,50,60,70,80,90]
#start=1,stop=6,step=1
print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6])#默认步长1
print(lst[1:6:])
#start=1 stop=6 step=2
print(lst[1:6:2])

#stop=6 step=2 start默认
print(lst[:6:2])
#start=1 step=2 stop默认
print(lst[1::2])

#step步长为负数的情况
print(lst[::-1])

#start=7 stop省略 step-1
print(lst[7::-1])

#start=6  stop=0 step=-2
print(lst[6:0:-2])#不包括0

for i in lst:
    print(i)


print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
lst2=['hello','world']
#lst.append(lst2)#将lst2作为一个元素添加到列表的末尾
#lst.extend(lst2)#向列表的末尾 一次添加多个元素
#lst.insert(1,120)#在任意（指定）位置上添加一个元素
#lst3=[True,False,'hello']
#在任意的位置上添加N多个元素
#lst[1:]=lst3#将切到的部分用新的列表替换
#lst.remove(30)#从列表中移除一个元素 如果有重复元素只移动第一个元素
#lst.pop(1)#pop根据索引移除元素
#lst.pop()#如果不指定索引 将删除列表中的最后一个元素

#切片 删除至少一个元素 将产生一个新的列表的对象
'''new_list=lst[1:3]
print('原列表',lst)
print('新列表',new_list)

#不产生新的列表对象 二十删除原列表中的内容
lst[1:3]=[]

#清空列表中的所有元素
lst.clear()
'''
#del 语句将列表对象删除
print('=============')
del lst
print(lst)






