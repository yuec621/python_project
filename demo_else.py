# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 14:53
'''for item in range(3):
    pwd=input('请输入密码')
    if pwd=='333':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起 三次密码均输入错误')
   '''
a=0
while a<3:
        pwd = input('请输入密码')
        if pwd == '333':
            print('密码正确')
            break
        else:
            print('密码错误')
else:
        print('对不起 三次密码均输入错误')