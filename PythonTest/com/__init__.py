#coding:gbk
'''list名=["1","e"]'''
from com.PythonLearning import person
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

'''列表名。insert(0,"aa")'''
person = ["male","female","kid",23,24.5,"female","嘻哈"]
person.insert(4,"happy")
print(person)


'''访问集合中的集合'''#这是什么意思？？？？
person = ["male","female","kid",23,24.5,"female","嘻哈"]
freedom = [1,2,3,3,"day","so"]
newlife = [1,2,3,4,5,6]
a = 3
'''已知列表类型，想确认列表类型，使用isinstance(列表名.列表类型)'''
print(isinstance(person, int))
print(isinstance(newlife,list))
print(isinstance(a,int))
'''未知列表类型，使用type(列表名)进行检测'''
print(type(freedom))
print(type(a))

''' for循环：for变量in列表名：
 处理代码
'''
beach = [1,24,5,9,10] #??发生了什么，为啥不能构造出来这个函数
for i in beach:
    f = 0+i
print(f)

'''创建字典'''
#第一种方法 data={}
mood = {"happy":22,"sad":34,"angry":"DUUF","blue":"00","anxiety":"799"}
#第二种方法 data=dict()
mood1 = dict()
mood1["iii"] = "ooo"
#两者有什么区别？？？
print(mood["happy"],mood1["iii"])
data = ["Monday","Thursday"]
print(data)


    
    
    
  
    



 







