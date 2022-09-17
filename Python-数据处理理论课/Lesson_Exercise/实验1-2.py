# 练习 1
#列表 List,元组 tuple，集合 set 和字典 dict 的区别和使用
#产生 list,tuple， set 和 dict
lst=[3,2,"a",3,1] #[ ]产生 list，元素有次序，可重复，任意类型， list 本身是 unhashable
tpl=(3,2,"a",3,1) #( )产生 tuple，元素有次序，可重复，任意类型， tuple 本身是 hashable
sets={3,2,"a",3,1} #{ }产生 set，元素不重复，无次序， set 本身是 unhashable
dicts={"i":3,"j":2,"k":"a","l":3,"m":1} #{index:item}产生 dict，其中 index 是索引，只能是字符、数字、 元组等 hashable 类型； item 是内容，可以是任意类型
#检查列表和提取某个值
#print(lst)
print(lst[0],tpl[0],dicts["i"]) #提取某个元素
print(lst[1:3],tpl[1:3]) #支持切片操作
# print(sets[0]) #结果失败，集合不能提取指定位置的元素，因集合内元素是无序的，用#符号注释后重新运行该程序。

# 练习 2
# 用 for 循环对每个元素进行操作,可用尝试用其他的类型
for i in lst:
    print(i)

#对于 dict 类型，可用 dict.keys， dict.values 和 dict.items 读取
for i,j in dicts.items():
    print(i,":",j)

