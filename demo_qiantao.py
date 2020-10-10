# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 15:01
#输出一个二行的矩形
'''for i in range(1,4):
    for j in range(1,5):
        print('*',end='\t')#不换行输出
    print()#换行
'''

#乘法表
for i in range(1,10):#行数
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
