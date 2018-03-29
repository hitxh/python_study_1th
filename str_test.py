
# 字符串运算

# \ 代表转义字符
'''
使用条件:
    1、单引号中单引号需要使用转义字符
       print('He isn\'t a stupid man')
'''
# 1
print('He isn\'t a stupid man')
# 也可以这样表达
print("He isn't a stupid man")

'''
如何输出反斜线\
    1、使用r可以让反斜线\作为反斜线输出
    2、\\
'''
print('C:\some\name')  # here \n means newline!
print("使用r,取消转义字符输出")
print(r'C:\some\name')  # note the r before the quote
print("使用\\\\作为\\,输出反斜杠\\")
print('C:\\some\\name')

'''
字符串还有其他的输出方法
以空格或Tab间隔的两个字符串会自动合并起来
'''
print("以空格或Tab间隔的两个字符串会自动合并起来")
print('xuhan'   'zhazha'  'doubi')

print("###################################################################")
'''
如何输出多行
反斜杠作为行与行之间的连接符
'''
# 方法1、
print("多行字符输出")
out_str="""第一行  xu
2   han   
3   zha
4   zha
最后一行   哈哈哈哈"""
print(out_str)

print("多行串成一行输出")
out_str="""第一行  xu \
2   han               \
3   zha               \
4   zha               \
最后一行   哈哈哈哈"""
print(out_str)

print("###################################################################")

print("格式化输出字符串")

print("1、打印字符串")
print ("His name is %s"%("Aviad"))

print("2、打印整数")
print ("He is %d years old"%(25))

print("3、打印浮点数")
print ("His height is %f m"%(1.83))

print("4、打印浮点数（指定保留小数点位数）")
print("His height is %.2f m"%(1.83))

print("5、指定占位符宽度   默认右对齐")
print("Name:%10s Age:%8d Height:%8.2f"%("Aviad", 25, 1.83))

print("6.指定占位符宽度（左对齐）")
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))

print("7.指定占位符（只能用0当占位符）")
print("Name:%-10s Age:%08d Height:%08.2f"%("Aviad",25,1.83))

print("8、科学计数法")
print(format(0.0015,'.2e'))
tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"   # {1:{3}^10} 1表示位置，{3}表示用第3个参数来填充，^表示居中，10表示占10个位置
print(tplt.format("排名","学校名称","总分",'*'))
# 输出结果     排名    	***学校名称***	    总分
# tplt中的{3}代表给的最后一个参数’*’，这样第2个位置的“学校名称”就会居中，空白位置用’*’代替
