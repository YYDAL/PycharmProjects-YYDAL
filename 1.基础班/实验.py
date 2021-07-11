# # gongzi = int(input('你的工资'))
# # if gongzi<=500:
# #     print('欢迎加入史塔克穷人帮')
# #     if gongzi<=100:
# #         print('恭喜您荣获美元队长称号')
# #     else :
# #         print('请找弗瑞队长加薪')
# # elif 500<=gongzi<=1000:
# #     print('祝贺您至少可以温饱了')
# # else:
# #     print('经济危机都难不倒你')
# #     if 1000<gongzi<=20000:
# #         print('您快比钢铁侠有钱了')
# #     elif 20000<gongzi:
# #         print('您是不是来自瓦坎达国？')
# # print('程序结束')
#
# #
# #
# # a = int(input("请输入第一个数"))
# # b = int(input("请输入第二个数"))
# # c = int(input("请输入第三个数"))
# # if a > b:
# #     if a > c:
# #         print(a)
# #     elif b >c:
# #         print(b)
# #     else:
# #         print(c)
# # else:
# #     if a >c:
# #         print(b)
# #     elif c >b:
# #         print(c)
# #
#
#
# import time
# import random
#
# print('本游戏是Rocky小朋友研发的，版本1.0')
# print('------------------------')
# player_victory = 0
# enemy_victory = 0
# i = 1
# status = True
# name = input('请输入你的名字：')
#
# print('%s真是个骨骼清奇的好名字' % name)
#
# while status:
#     time.sleep(1.5)
#     print('  \n——————现在是第 %s 局——————' % i)
#     i = i + 1
#     if name != 'Rocky':
#         player_life = random.randint(100, 150)
#         player_attack = random.randint(30, 50)
#         enemy_life = random.randint(100, 150)
#         enemy_attack = random.randint(30, 50)
#     else:
#         player_life = 999
#         player_attack = random.randint(50, 100)
#         enemy_life = random.randint(100, 150)
#         enemy_attack = random.randint(30, 50)
#
#     print('【%s】\n血量：%s\n攻击：%s' % (name, player_life, player_attack))
#     print('------------------------')
#     time.sleep(1)
#     print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
#     print('-----------------------')
#     time.sleep(1)
#
#     while player_life > 0 and enemy_life > 0:
#         attack_type = int(input('''
# 请选择攻击种类:
# 1.普通攻击
# 2.蓄力攻击（1.5倍攻击，跳过下次攻击)
# 3.绝地反击（额外自爆10点血，造成随机伤害）
# 你的选择是：'''))
#         print('-----------------------')
#         if attack_type == 1:
#             player_life = player_life - enemy_attack
#             enemy_life = enemy_life - player_attack
#             print('你发起了普通攻击，【敌人】剩余血量%s' % enemy_life)
#             print('敌人向你发起了攻击，【%s】的血量剩余%s' % (name, player_life))
#             print('-----------------------')
#             time.sleep(1.2)
#
#         elif attack_type == 2:
#             player_life = player_life - enemy_attack
#             enemy_life = int(enemy_life - 1.5 * player_attack)
#             print('你发起了蓄力攻击，【敌人】剩余血量%s' % enemy_life)
#             print('敌人向你发起了攻击，【%s】的血量剩余%s' % (name, player_life))
#             print('-----------------------')
#             if player_life <= 0 or enemy_life <= 0:
#                 break
#                 # 此地多做一次判断
#             time.sleep(1.2)
#             player_life = player_life - enemy_attack
#             print('此回和跳过，你挨打了，你还有%s的血' % player_life)
#             print('-----------------------')
#             time.sleep(1.2)
#
#         else:
#             player_life = player_life - enemy_attack - 10
#             enemy_life = enemy_life - random.randint(40, 60)
#             print('%s自己来了一发强心剂，损失了10点血' % name)
#             print('你发起了蓄力攻击%s' % enemy_life)
#             print('敌人向你发起了攻击，【%s】的血量剩余%s' % (name, player_life))
#             print('-----------------------')
#             time.sleep(1.2)
#
#     if player_life > 0 and enemy_life <= 0:
#         player_victory += 1
#         print('敌人死翘翘了，你赢了！')
#     elif player_life <= 0 and enemy_life > 0:
#         enemy_victory += 1
#         print('悲催，敌人把你干掉了！')
#     else:
#         print('哎呀，你和敌人同归于尽了！')
#     choice = input('还想再玩么？请回答 “Y” or “N”：')
#     if choice == 'Y':
#         status = True
#     else:
#         status = False
#
# if player_victory > enemy_victory:
#     time.sleep(1)
#     print('\n【最终结果：你赢了！】')
# elif enemy_victory > player_victory:
#     print('\n【最终结果：你输了！】')
# else:
#     print('\n【最终结果：平局！】')
#
#
#
#
#
#
#
#
#
#
#
#
#

#
# class QQ:
#     def __new__(cls, *args, **kwargs):
#         if cls.instant is None:
#             cls.instant = super().__new__(cls)
#         return cls.instant
#     def hhh(self):
#         print(2222)
#     print(1111)
#
# a = QQ
# aa = a.hhh(1111)
# print(id(aa))
# b = QQ
# bb = b.hhh(1111)
# print(id(bb))
# c = QQ
# cc = c.hhh(1111)
# print(id(cc))
# #

# a = [1,2,3,4]
# print(len(a))
#
# class House:
#     mianji = 100
#     name = '我的房子'
#     jiage = 1000000
#     # def goumai():
    #     print('你需要支付足够的钱')
    # def chushou():
    #     print('1111')
    #     global b
#     #     b = 'mai'
#
# class Furniture(House):
#     pass
#
# wo = Furniture


# a = "中国欢迎您".encode("utf-8")
# print(a)  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'
# b = a.decode("utf-8")
# print(b)  # 中国欢迎您

#
# import binascii
# # 方法中不传参数则是以默认的utf-8编码进行转换
# a = "中国欢迎您".encode("utf-8")
# print(a)  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'
# c = binascii.b2a_hex('中国欢迎您'.encode())
# c = b'4e1a88e7269bfc2bdac86c6bb23251ec'
# print("c===", c)  # c=== b'e4b8ade59bbde6aca2e8bf8ee682a8'
# d = binascii.a2b_hex(c)
# print(d)  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\xac\xa2\xe8\xbf\x8e\xe6\x82\xa8'
# v = binascii.a2b_hex(c).decode("utf-8")
# print(v)  # 中国欢迎您
# b = a.decode("utf-8")
# print(b)  # 中国欢迎您
# print(c)


# x = int(input("请输入每年学费:"))
# y = int(input("请输入每年住宿费:"))
# z = int(input("请输入年数:"))
# sum = (x + y) * z
# print(sum)
#
# shuju = input('12')
# shuju.split(',')
# q = list(shuju)
# print(q)

# a = [1, 2, 3, '1212']
# b = list(filter(str, a))
# print(b)
# import math
# print(filter(math.sqrt(x) % 7 ==0, range(1, 101)))



# a = int(input())
# s = 2**a
# print('2^%s=%s' % (a, s))
# exit(0)


# import time
# for i in range(101):
#     print(str(i) + '%')
#     time.sleep(0.1)
#
# while 1 :
#
#      continue

print("hhh")



