#原来
def HHH(a,b):
    c = a['name']
    b,c = c,b
    a['name'] = c                               #貌似是暴力换值法
    print(a)
    print(b)
HHH({'name':222},(1, 2, 3, 4))                  #分别输入字典和元组

#修正后
def HHH(*args,**kwargs):
    print(args)
    print(kwargs)
    q = list(kwargs.values())               #不太了解tuple（应该是强行转化为元组的方法吧），我用的是list
    print(q)
    b = dict(zip(kwargs.keys(),args))       #这个是看完讲解后的代码，原来那个偏的太离谱了
    print(b)

HHH(1,3,4,2,z=32,x=43,c=75,v=30)
