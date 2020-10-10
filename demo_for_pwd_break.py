# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 13:56
'''
从键盘录入密码 最多录入3次 如果正确就结束循环
'''

'''for item in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
'''

a=0
while a<3:
    #条件执行体
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    #改变变量
    a+=1

