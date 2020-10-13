# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/13 0013 9:40
#字符串的驻留机制

'''a='python'
b='python'
c=''python''
print(a,id(a))
print(b,id(b))
print(c,id(c))'''

##字符串查询操作

'''s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))'''

##字符串中的大小写转换
'''s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))
print(s.lower(),id(s.lower()))
print(s,id(s))'''

#字符串对齐操作
'''s='hello python'
print(s.center(20,'*'))#居中
print(s.ljust(20,'*'))#左对齐
print(s.rjust(20,'*'))#右对齐
print(s.rjust(20))
print(s.zfill(20))#右对齐 使用0进行填充
print(s.zfill(10))
'''

#字符串分割
'''s='hello world python'
lst=s.split()
print(lst)
sl='hello world|python'
print(sl.split(sep='|'))
print(sl.rsplit(sep='|',maxsplit=1))'''

#判断字符串
'''s='hello,python'
print('1',s.isidentifier())#字符串是否合法
print('\t'.isspace())
print('zzzz'.isalpha())
print('123'.isdecimal())
print('12'.isnumeric())
print('sd2'.isalnum())'''

##字符串替换和合并
'''s='hello'
print(s.replace('hello','ggggg'))

lst=['1','2','3']
print('|'.join(lst))'''

##字符串的比较操作
'''print('12'>'1')
print('123'>'45')
print(ord('1'),ord('4')) #原始值的比较'''

#编码
#byte代表是一个二进制数据
s='天涯共此时'
byte=s.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))


