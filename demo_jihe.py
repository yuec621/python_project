# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/12 0012 14:04
#第一种创建方式使用[]
'''a=[2,3,4,5,6,7,8]#集合中的元素不允许重复
print(a)
#第二种创建方式使用set()
sl=set(range(6))
print(sl,type(sl))'''

#两个集合是否相等 元素相同就相等
# s={10,20,30,40}
# s2={40,30,20,10}
# print(s==s2)
# print(s!=s2)

#一个集合是否是另一个集合的子集
# s={10,20,30,40}
# s2={10,20,30}
# s3={10,20,30,40,50}
# print(s2.issubset(s))
# print(s3.issubset(s))
#
# #一个集合是否是另一个集合的超集
# print(s3.issuperset(s))
# print(s3.issuperset(s2))
#
# #两个集合是否有交集
# print(s3.isdisjoint(s2))#有交集为false
# s4={33}
# print(s2.isdisjoint(s4))#无交集为true

#交集
s={10,20,30,40}
s2={10,20,30}
print(s2.intersection(s))
print(s2 & s) #intersection与&等价 交集操作

#并集操作
print(s2.union(s))
print(s| s2)#union与|等价 并集操作

#差集操作
print(s.difference(s2))
print(s-s2)#difference与-等价 差集操作

#对称差集
print(s2.symmetric_difference(s))
print(s2^ s)




