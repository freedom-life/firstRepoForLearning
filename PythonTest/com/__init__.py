#coding:gbk
'''list��=["1","e"]'''
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

''''''






