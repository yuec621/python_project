# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/10 0010 9:13

money=1000 #余额
s=int(input('请输入取款金额')) #取款金额
#判断余额是否充足
if  money>=s:
    money=money-s
    print('取款成功，余额为：',money)
