class HHH:
    _weizhi = None
    def __new__(cls, *args, **kwargs):
        if cls._weizhi == None:
            cls._weizhi = object.__new__(cls)
            return cls._weizhi                     #标准单例模式，需要记住
        else:
            return cls._weizhi

A = HHH()
B = HHH()
print(id(A))                                      #此时的A,B同属于一个单例
print(id(B))