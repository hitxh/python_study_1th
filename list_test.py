
'''
列表
列表是可变的(mutable)——可以改变列表的内容，
这不同于字符串和元组，字符串和元组都是不可变的。接下来讨论一下列表所提供的方法
list函数

可以使用list函数来创建列表：
'''
print("shu")
list('Hello')
['H', 'e', 'l', 'l', 'o']
print(list('hello')[4])

# 列表的基本操作
# 在Python 序列通用操作介绍中提及的操作全部适用于列表，例如索引、分片、连接、乘法等。
# 而且由于列表是可以修改的，所以多了一些元素赋值、元素删除、分片赋值的方法。

print("改变列表元素的值")
a=list('ooooo')
a[2]='A'
print(a)

# 删除列表元素

# 使用del对列表元素进行删除：
del a[2]
print(len(a))

# 删除之后，列表的长度也变成了4.关于del语句的使用后续介绍。

# 分片赋值

# 使用分片赋值可以同时改变一个范围内的字符：

str1 = list('abcdef')
print(str1)
str1[3:] = list('abc')
print(str1)

# 不止如此，分片赋值更强大的功能是使用长度不等的序列替换分片：

#长序列替换短分片
str2 = list('ppp')
print(str2)
str2[1:]=('ython')
print(str2)


#短序列替换长分片
str2= list('abcdefg')
str2[1:]= list('bc')
print(str2)


# 利用分片操作，我们可以实现序列的插入操作---插入不过是替换掉某段“空”分片：
str3=[1,5]
str3[1:1]=[2,3,4]
print(str3)

'''
列表方法

方法与函数关系密切。方法本身就是函数，只不过这函数是和对象结合在一起的，通过对象来调用方法。面向对象语言中这些方法可称为接口。方法调用的语法为：

对象.方法（参数）

接下来我们就来看看列表这种类型的对象提供了什么方法（接口）。

append

功能：用于在列表末尾追加新的元素
'''
lst=[1,2,3]
lst.append(4)
print(lst)
'''
功能：用于统计某个元素在列表中出现的次数
'''
print([1,2,3,4,5,2,3,1,2,3,42,1,2,3,5].count(1))

'''
extend

功能：在列表末尾一次性追加另一个序列中的多个值

'''
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

'''
index

功能：用于从列表中找出某个值第一个匹配项的索引位置
'''
a = ['Me', 'and', 'my', 'broken']
a.index('my')
print(a)


'''
insert

功能：用于将对象插入到列表中对应位置
'''

number=[1, 2, 3, 4, 5]
print(number)
number.insert(3, 'hello')
print(number)
number.insert(3, 6)
print(number)

'''
pop

功能：该方法从列表中弹出一个元素，默认是最后一个。并且返回弹出的元素

'''

number=[1, 2, 3, 4, 5, 6, 7, 8]
a = number.pop()
print(number)


'''
利用append（从末尾添加一个元素）方法，我们可以来实现一种常见的数据结构--栈。

当然，POP方法可以从序列中弹出任意位置的元素：
'''

number.pop(3)

'''
remove

功能：从列表中移除某个值的第一个匹配项。与pop不同的是，该方法并不返回移除的元素。
'''

str4 = list('hello')
str4.remove('l')
print(str4)

'''
reverse

功能：该方法对序列方向存放
'''

number.reverse()
print(number)

'''
注意该方法改变了列表但是没有返回值。

如果需要对一个序列进行反向迭代，可以使用reversed函数。这个函数并不返回一个列表，而是返回一个迭代器对象，可以使用list把迭代器对象转换成列表：
'''

number = list(reversed(number))

'''
sort

功能：用于在原位置度列表进行排序。 在原位置意味着列表会被修改。
'''

number.sort()
print(number)

# 应注意的是，sort()方法的返回值并不是序列本身，而是None。



# 如何保存原序列顺序而进行排序？

# 方法一

x = [3,5,7,3,1,2,4]
y =x[:]
y.sort()
print(x)
print(y)

'''
注意将列表x赋值给列表y时千万别使用直接赋值，否则y与x指向了相同的对象，对y的修改即是对x的修改：
'''
# 例如：

str1 = list('abcdef')

y = str1[:]
print(id(y))
# print(id(str1)
# 结果y和str1的id不同

x = str1
print(id(x))
print(id(str1))


# 结果x和str1的id相同

y=x
y.sort()
print(x)
print(y)

'''
方法二
当然，你也可以使用函数来进行排序。

函数：sorted().

功能：对任何序列进行排序，结果返回一个排好序的列表。
'''


x=[3,5,2,1,7,4,8,9,3]
y=sorted(x)
print(x)
print(y)

'''
如何修改排序规则？

从上面的例子我们看到，sort方法的默认排序都是升序的。sort方法有两个可选的参数，可以通过它来修改排序规则：

key
key参数提供一个在排序过程中使用的函数，利用该函数来为列表中元素创造一个键（key），依据键来对列表元素（值）进行排序。
'''

str5 = ['one','year','like','any','old','other','year']
# 默认的排序依据字符串排序规则
str5.sort()
print(str5)
#使用key参数来修改排序规则
#我们使用字符长度作为键来排序
str5.sort(key=len)
print(str5)

'''
reverse
另一个参数reverse是个简单的bool值，用来指明是否要反向排序;
'''


num=[2,3,4,5,6,78,4,3,3,4,5,8,9]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

# 借助参数key，我们可以定义自己的比较函数来自定义比较规则。函数的定义在后面进行介绍。