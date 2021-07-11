class hhh:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            #hasattr(类名，属性名)若没有该属性则创建一个，         #初始化基本格式
            cls.instance = super().__new__(cls)
            return cls.instance

    def __init__(self):
        self.shuxin = 11111

aaa = hhh()
print(aaa.shuxin)              #第一次正常调用
bbb = hhh()
print(bbb.shuxin)              #第二次被调用时则会无法获取该属性