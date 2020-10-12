# 哔站python学习教程
# 听讲人 cy
# 开发时间：2020/10/12 0012 11:23
'''
字典的创建方式
使用{}创建字典
'''
scores={'张山':20,'李四':60,'王五':30}

'''print(scores)
print(type(scores))

#第二种创建dict()
student=dict(name='jack',age=20)
print(student)
print(scores.get('张山'))
print(scores.get('张三'))
print(scores.get('马奇',99))#99是查找'马奇'所对的value不存在时  提供的个人默认值
'''

'''print('张山' in scores)
print('张山' not in scores)
del scores['张山']
scores['陈留']=98#新增元素
print(scores)
scores['陈留']=666#修改元素
print(scores)
'''

#获取所有元素的key
'''keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))#将所有的key组成的视图转成列表
'''

#获取所有的value
'''values=scores.values()
print(values)
print(type(values))
print(list(values))
'''

#获取所有的key-value对
'''items=scores.items()
print(items)
print(list(items))
'''

#字典元素的遍历

'''for item in scores:
    print(item,scores[item],scores.get(item))'''

'''d={'name':'张山','name':'李四'}#key不允许重复
print(d)'''

'''d={'name':'张山','name1':'张山'}#value可以重复
print(d)'''

'''lst=[10,20,30]
lst.insert(1,100)
print(lst)'''

#字典生成式
'''items=['f','e','t']
prices=[10,33,9,2]
d={
    item.upper():prices
    for item ,prices in zip(items.prices)
}
print(d)'''




