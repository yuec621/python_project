# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/9 0009 14:35
#可以输出数字
print(120)
print(98.5)
#可以输出字符串
print("frfr")
#含有运算符的表达式
print(3+1)
#将数据输出文件中
fp=open('D:/test.txt','a+')
print('helloworld',file=fp)
fp.close()
#不进行换行输出 （输出内容在一行当中）
print('hello','world','python')

#转义字符
print('hello\nworld') #\+转义功能的首字母 n-->newline的表示换行
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')#world将hello进行了覆盖
print('hello\bworld')#\b是退一个格  将o退没了
print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

#原字符,不希望字符串中的转义字符起作用, 就使用原字符,就是在字符串之前加上R 或R
#最后一个字符不能是反斜杠
print(r'hello\nworld')
print(chr())
print(ord('成'))

