# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 11:24
for item in 'Python':
    print(item)
#range()产生一个整数序列 也是一个可迭代对象
for i in range(10):
    print(i)
#如果在循环体中不需要使用到自定义变量 可将自定义变量写为"_"
for _ in range(5):
    print('人生苦短 我用python')

#使用for循环 计算1到100之间的偶数和
sum=0 #用于存储偶数和
for item in range(1,101):
    if item%2==0:
        sum+=item
    print('1到100之间的偶数和为;',sum)