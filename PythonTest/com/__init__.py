#coding:gbk
'''list��=["1","e"]'''
from com.PythonLearning import person
person = ["male","female","kid",23,24.5,"female","����"]


'''ɾ��ָ��ֵ����'''
person = ["male","female","kid",23,24.5,"female","����"]
person.remove("����")
print(person)

'''ɾ�����һ�����ݣ��б�����pop()'''
person = ["male","female","kid",23,24.5,"female","����"]
person.pop()
print(person)


'''len(list��)'''   '''���⣺Ϊɶ����ʾ�б���Ԫ���м���������ֱ����ʾ���б�������Ԫ�أ�'''
person = ["male","female","kid",23,24.5,"female","����"]
len(person)
print(person)


'''�������ݣ��б���.append(�����ݡ�)'''
person = ["male","female","kid",23,24.5,"female","����"]
person.append("��������")
print(person)

'''�б�����extend(�б���1)'''
person = ["male","female","kid",23,24.5,"female","����"]
number = [1,2,3,6,"thanks"]
person.extend(number)
print(person)

'''�б�����insert(0,"aa")'''
person = ["male","female","kid",23,24.5,"female","����"]
person.insert(4,"happy")
print(person)


'''���ʼ����еļ���'''#����ʲô��˼��������
person = ["male","female","kid",23,24.5,"female","����"]
freedom = [1,2,3,3,"day","so"]
newlife = [1,2,3,4,5,6]
a = 3
'''��֪�б����ͣ���ȷ���б����ͣ�ʹ��isinstance(�б���.�б�����)'''
print(isinstance(person, int))
print(isinstance(newlife,list))
print(isinstance(a,int))
'''δ֪�б����ͣ�ʹ��type(�б���)���м��'''
print(type(freedom))
print(type(a))

''' forѭ����for����in�б�����
 �������
'''
beach = [1,24,5,9,10] #??������ʲô��Ϊɶ���ܹ�������������
for i in beach:
    f = 0+i
print(f)

'''�����ֵ�'''
#��һ�ַ��� data={}
mood = {"happy":22,"sad":34,"angry":"DUUF","blue":"00","anxiety":"799"}
#�ڶ��ַ��� data=dict()
mood1 = dict()
mood1["iii"] = "ooo"
#������ʲô���𣿣���
print(mood["happy"],mood1["iii"])
data = ["Monday","Thursday"]
print(data)


    
    
    
  
    



 







