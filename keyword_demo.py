# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/9 0009 16:10
import keyword
print(keyword.kwlist)


name='玛利亚'
print('标识',id(name))
print('类型',type(name))
print('值',name)

#布尔
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))

#类型转换
s1='128'
f1=98.7
s2='76.66'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1))) #将str转成int类型 字符串为数字
print(int(f1),type(int(f1))) #float转成int类型 截取证书部分 射雕小数部分
#print(int(s2),type(int(s2)))#将str转成int类型 报错 因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3))) #将str转成int类型时 字符串必须为数字串(整数)  非数字串不允许转换

#float函数  将其他数据类型转成float类型
s1='128.98'
s2='76'
ff=True
s3='hello'
i=98
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3))) #字符串中的数据如果非数字串 则不允许转换
print(float(i),type(float(i)))



