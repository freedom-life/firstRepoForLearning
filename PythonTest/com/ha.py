from com.ModuleTest import listName, listShow
listName = [1,3,1,4,'小蜗','大爷']
listShow = ['长长久久',999,'hahaha']
'''插入数据'''
listName.append('大爷')
listName.extend(listShow)
listName.insert(5,'爱')
print(listShow)
print(listName)
print('大爷的数量:',listName.count('大爷'),'列表的数量:',listName)
print('第f三次改动！')
print('第f三 ngjjj次改动！')