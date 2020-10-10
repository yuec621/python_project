# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 9:23
#分支结构 多选一执行
#从键盘录入一个整数 成绩
'''
9-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或大于100 为非法数据（不是成绩的有效范围）

score=int(input('请输入一个成绩'))
#判断
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score<=69:
    print('D')
elif score>=0 and score<=59:
    print('E')
else:
    print('对不起 成绩有误 不在成绩的有效范围')


#简易写法

if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
elif 0<=score<=59:
    print('E')
else:
    print('对不起 成绩有误 不在成绩的有效范围')


    会员 >=200 8折
    >=100 9折
    不打折
    
    非会员 >=200 9.5折
    不打折
    '''
answer =input('您是会员么?y/n')
money=float(input('请输入您的购物金额:'))
#外层判断是否是会员
if answer=='y': #会员
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else: #非会员
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)

