#coding:gbk
'''list名=["1","e"]'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]


'''删除指定值数据'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
person.remove("嘻哈")
print(person)

'''删除最后一个数据：列表名。pop()'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
person.pop()
print(person)


'''len(list名)'''   '''问题：为啥不显示列表中元素有几个？而是直接显示了列表里具体的元素？'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
len(person)
print(person)


'''单个数据：列表名.append(“数据”)'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
person.append("哈哈哈哈")
print(person)

'''列表名。extend(列表名1)'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
number = [1,2,3,6,"thanks"]
person.extend(number)
print(person)

''''''






