# class QQQ:
#     def __init__(self, gao, kuan):
#         self.gao = gao
#         self.kuan = kuan
#
#     def ZFX(self):
#         mianji = self.kuan*self.gao
#         return "矩形形的面积是%s平方米"%mianji
#
# shuru = QQQ(3,5)
# print(shuru.ZFX())



# class Mianji:
#     def __init__(self,long,height):
#         self.long = long
#         self.height = height
#
#     def Zhengfangxing(self):
#         mianji = self.long * self.height
#         return "面积是%sm"%mianji
#
# class tiji(Mianji):
#     def __init__(self, long, height):
#         if long == height:
#             Mianji.__init__(self,long,height)
#         else:
#             pass
#
# shuju = tiji(12, 12)
# # print(shuju.Zhengfangxing())
#
#
# # class HHH:
# #     def __new__(cls, *args, **kwargs):
# #         if not hasattr(cls,"hhh"):
# #             cls.hhh = object.__new__(cls)
# #         return cls.hhh
# #
# # AAA = HHH("WWW")
# # BBB = HHH("QQQ")
# # print(id(AAA))
# # print(id(BBB))
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
#             print('?惴⑵鹆司胤椿鳎镜腥恕渴Ｓ嘌?%s' % enemy_life)
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
























































































