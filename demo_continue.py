# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 14:06
'''
要求输出1到50之间所有的倍数 5,10，15
5的倍数的共同点 和5的余数为0的数都是5的倍数
要求使用continue实现
'''
for item in range(1,51):
    if item%5==0:
        print(item)
#使用continue
for item in range(1,51):
    if item%5!=0:
        continue
        print(item)
