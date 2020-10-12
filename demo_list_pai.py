# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/12 0012 10:49
lst=[10,20,30,40]
print('排序前的列表',lst,id(lst))
#开始排序 调用列表对象的sort方法 升序降序
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数 将列表中的元素进行降序升序
lst.sort(reverse=True)
print('降序',lst,id(lst))

#使用内置函数sorted()对列表进行排序 将产生新的列表对象
lst2=[20,40,60,10,99]
print('开始排序')
new_list=sorted(lst2)
print(new_list)

#指定关键字参数 实现列表元素的降序排序
desc_list=sorted(lst2,reverse=True)
print(desc_list)

lst3=[i*i for i in range(1,10)]
print(lst3)
