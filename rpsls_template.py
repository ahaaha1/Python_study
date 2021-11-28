#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：杨强龙
日期：2021年11月27日
"""


#0-石头
#1-史波克
#2-纸
#3-蜥蜴
#4-剪刀


import random

#以下为完成游戏所需要用的自定义函数
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":                #使用if/elif/else语句将各个游戏对象对应到不同的整数
        number=0
    elif name=="史波克":
        number=1
    elif name=="布":
        number=2
    elif name=="蜥蜴":
        number=3
    else:
        number=4
    return number                 #返回结果

def number_to_name(number):
    """
    将整数（0,1,2,3 or 4）对应到游戏的不同对象
    """

    if number==0:                # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
        name="石头"
    elif number==1:
        name="史波克"
    elif number==2:
        name="布"
    elif number==3:
        name="蜥蜴"
    else:
        name="剪刀"
    return name                  #返回结果

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """

    print("------------")                                             # 输出"-------- "进行分割
    print("您的选择为%s"%player_choice)                                 # 在屏幕上显示用户选择的对象
    player_choice_number=name_to_number(player_choice)                # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    comp_number=random.randrange(0,5)                                 # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
    comp_name=number_to_name(comp_number)                             # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
    print("计算机的选择为%s"%comp_name)                                   # 在屏幕上显示计算机选择的随机对象
    if comp_number==player_choice_number:                             # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果（如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”）
        print("您和机器出的一样")
    else:
        if player_choice_number==0:
            if comp_number==3:
                print("您赢了")
            elif comp_number==4:
                print("您赢了")
            else:
                print("机器赢了")
        if player_choice_number==1:
            if comp_number==4:
                print("您赢了")
            elif comp_number==0:
                print("您赢了")
            else:
                print("机器赢了")
        if player_choice_number==2:
            if comp_number==0:
                print("您赢了")
            elif comp_number==1:
                print("您赢了")
            else:
                print("机器赢了")
        if player_choice_number==3:
            if comp_number==1:
                print("您赢了")
            elif comp_number==2:
                print("您赢了")
            else:
                print("机器赢了")
        if player_choice_number==4:
            if comp_number==2:
                print("您赢了")
            elif comp_number==3:
                print("您赢了")
            else:
                print("机器赢了")

#对程序进行测试
print("欢迎使用RPSLS游戏")                                         # 在屏幕显示“欢迎使用RPSLS游戏”
choice_name=input("请输入您的选择")                                # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
if choice_name!="石头":                                          # 使用if嵌套语句判断用户的选择是不是石头/剪刀/布/蜥蜴/史波克中的任意一个，如果不是则输出“Error: No Correct Name”
    if choice_name!="剪刀":
        if choice_name!="布":
            if choice_name!="蜥蜴":
                if choice_name!="史波克":
                    print("Error: No Correct Name")

if choice_name=="石头":                                          # 用户的选择是石头/剪刀/布/蜥蜴/史波克中的任意一个时调用rpsls()函数
    rpsls(choice_name)
if choice_name=="剪刀":
    rpsls(choice_name)
if choice_name=="布":
    rpsls(choice_name)
if choice_name=="蜥蜴":
    rpsls(choice_name)
if choice_name=="史波克":
    rpsls(choice_name)



