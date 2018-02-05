'''
Created on 2018年1月31日

@author: 陈佳文
'''
'''
创建列表
'''
listName = [1.1,3,'上海','深圳']
listShow = ['aaa','bbb']


'''添加数据'''
listName.extend(listShow)
listName.append('小蜗')
listName.insert(2, '北京')
print(999)

'''删除数据2种方法'''
listName.pop(2)
listName.remove('bbb')
print(listName)

'''统计列表值的数量'''
print('aaa 的数量 :',listName.count('aaa'),' 列表值的个数 :',listName.__len__())





