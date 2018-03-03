#coding:gbk
'''
问题集锦：如何一个在列表中所有female前面都插入“王者荣耀”？如何插入第二female前面？
'''

person = ["male","female","kid",23,1.4,"female"]

position = person.index("female" )
person.insert(position, "王者荣耀")
print(person)


'''定义函数'''
def sad(a,b,c,d,e,f,Flag=True,g=8):
    if Flag == True:
        sum = a+b+c+d+e+f
    else:
        sum = a+g
    return sum
'''调用函数'''#z怎么调用函数？？？主要是对变量的理解不到位…………
getaway = [1,2,3,4,5,6,7,8]
print(sum)


    
    