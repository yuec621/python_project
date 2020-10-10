# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 10:32
#range()的三种创建方式
'''
第一种创建方式 只有一个参数（小括号中只给了一个数）
'''
r=range(10) #[]
print(r)#range(0,10)
print(list(r)) #用于查看range对象中的整数序列 -->list是列表的意思
'''
第二种创建方式 给了两个参数（小括号中给了两个数）
'''
r=range(1,10)
print(list(r))
'''
第三种创建方式 给了三个参数 （小括号中给了三个数
'''
r=range(1,10,2)
print(list(r))
'''
判断指定的整数 在序列中是否存在in， not in
'''
print(10 in r) #false  10不在当前的r这个整数序列中
print(9 in r) #true 9在当前的r这个序列中
print(10 not in r)#true
print(9 not in r) #false
print(range(1,20,1))
print(range(1,101,1))
