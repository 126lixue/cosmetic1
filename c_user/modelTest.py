# from c_user.models import Address
# #查询
# adds=Address.objects.all()  #获取所有地址
# add=Address.objects.get(id=1,reciver='刘诗诗')  #获取指定字段的字段记录，可以加多个条件
# adds2=Address.objects.all().values_list('id','reciver')   #过滤字段
# add2=Address.objects.filter(uid=1,reciver='刘诗诗').all()   #符合过滤的所有记录
# add3=Address.objects.filter(uid=1,reciver='刘诗诗').first()   #符合过滤的第一条记录
# #新僧
# Address.objects.create(reciver='刘诗诗',sheng='黑龙江')  #新增一条数据
# add4=Address()
# add4.reciver='唐禹哲'
# add4.save()
# #删除
# Address.objects.filter(uid=1,reciver='刘诗诗').delete()    #删除指定数据
# #更新
# Address.objects.filter(uid=1,reciver='刘诗诗').update(reciver='刘诗',sheng='沈阳')
#
#
# def foo(arg,a):
#     x=100
#     y='hello python!'
#     for i in range(10):
#         j=1
#         k=1
#     def b(a):
#         print(locals())
#     b(a)
#     print(locals())
# foo(1,2)
# print(locals

# class A:
#     def __init__(self):
#         self.name='lss'
#     def method(self):
#         print('method print')
# Instance=A()
# # print(getattr(Instance,'name','not find'))
# # print(getattr(Instance,'age','not find'))
# getattr(Instance,'method','default')()

# class Shape:
#     def __dir__(self):
#         return ['area','perimeter','location']
#     def __len__(self):
#         return 1
# s=Shape()
# print(dir(s))
#
# a='abcd'
# print(len(a))
# print(a.__len__())
# print(len(s))
# print(dir())
# print(locals())

# class test():
#     name='xiaohua'
#     def __init__(self):
#         self.name='lss'
#     def run(self):
#         return 'hello world'
# t=test()
# t1=test()
# test.name='list'
# # t.name='张三'
# print(test.name)
# print(hasattr(t,'name'))  #判断对象有name属性
# print(hasattr(t,'rum'))    #判断对象有run方法
# print(t.name+'%%%'+t1.name)
# print()
#
# '''True'''
# '''True'''


# from sys import *
# # print(globals())
# __name__='1'
# d=dict(globals())
# print(len(d))
# if __name__=='__main__':
#     for i,j in d.items():
#         print(i,j)
# a='ashcdbchj'
# class B (a):
#
#     c='bdhb'
# print(dir())
# print(vars())
# print(dir(B))
# print(vars(B))
# import json
# a=[{1:'a',2:'b',3:'c',4:'d',5:'e'}]
# jsons=json.dumps(a)
# print(jsons)
# print(type(jsons))
#
#
# obj=json.loads(jsons)
# print(obj)
# print(a)
# print(type(obj))
#


a=[{'id':1,'name':'zhu1','pid':0},{'id':2,'name':'zhu2','pid':0},{'id':3,'name':'1sub1','pid':1},{'id':4,'name':'1sub4','pid':1},{'id':5,'name':'2sub1','pid':3}]


def tojson(sr=None,sc=[]):
	if sc:
		for i in sc:
			for j in sr:
				if i['id']==j['pid']:i['sub'].append(j)
			if i['sub']:tojson(sr,i['sub'])
	else:
		for i in sr:
			i['sub']=[]
			if i['pid']==0:sc.append(i)
		tojson(sr,sc)
b=[]
tojson(a,b)
print(b)
'''[{'sub': [{'sub': [{'sub': [], 'name': '2sub1', 'id': 5, 'pid': 3}], 'name': '1sub1', 'id': 3, 'pid': 1}, {'sub': [], 'name': '1sub4', 'id': 4, 'pid': 1}], 'name': 'zhu1', 'id': 1, 'pid': 0}, {'sub': [], 'name': 'zhu2', 'id': 2, 'pid': 0}]
'''






