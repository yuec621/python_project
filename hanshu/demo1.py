# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/13 0013 10:50

'''def calc(a,b):#a,b称为形式参数 简称形参  形参的位置是在函数的定义处
    c=a+b
    return c
result=calc(10,20)#10,20为实参 实参的位置是在函数的调用处
print(result)'''


#函数返回多个值时  结果为元组
'''def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
        return odd,even
print(fun([10,20,30,55,7]))'''

'''name='杨老师'#name的作用范围为函数内部和外部都可以使用--->全局变量
print(name)
def fun2():
    print(name)
#调用函数
fun2()

def fun3():
    global age#函数内部定义的变量 局部变量 局部变量使用gloal声明 这个变量就变成了全局变量
    age=10
    print(age)
fun3()
print(age)'''

'''def fun(n):
    if n==1:
        return 1
    else:
        res=n*fun(n-1)
        return res
print(fun(5))'''

#抛异常
'''try:
    a=int(input('请输入第一个'))
    b=int(input('请输入第二个'))
    result=a/b
    print('结果',result)
except ZeroDivisionError:
    print('余数不能为0')
print('程序结束')'''

'''try:
    a=int(input('第一个'))
    b=int(input('第二个'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    result = a / b
    print('结果为',result)
finally:
    print('谢谢您的使用')'''

'''i=1
while i<=10:
    print(i)
    i+=1
'''



