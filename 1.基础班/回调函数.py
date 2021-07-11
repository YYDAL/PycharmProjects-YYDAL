def hhh():
    print('哈哈哈')

def fuwu(qqq,eee):                    #qqq的作用是起回调作用，
    if eee == 1:                      #eee做形参决定下一步的运算
        return qqq
    elif eee == 2:
        print('阿狸')
    else:
        print('永远')                 #以else结尾的话应使用print


def qiantao(aaa,eee2):
    if eee2 == 1:
        return aaa()                  #可以进行多层嵌套
    else:
        print('你错了哈哈')            #以else结尾的话应使用print

fuwu(qiantao(hhh,2),1)                #此处输入值就是eee可以决定下一步运算