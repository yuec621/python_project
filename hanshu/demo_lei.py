# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/13 0013 15:37
#实例方法
class Student:
    name='吉林'
    def __init__(self,name,age):
        self.name='44'
        self.age='12'
    def eat(self):
        print('学生在吃饭')

#在类之外定义的称为函数 在类之内的定义的称为方法
def drink():
    print('喝水')
drink()

#创建Student类的对象
stu=Student('zz',12)
print(id(stu))
print(type(stu))


