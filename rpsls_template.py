#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ǿ��
���ڣ�2021��11��27��
"""


#0-ʯͷ
#1-ʷ����
#2-ֽ
#3-����
#4-����


import random

#����Ϊ�����Ϸ����Ҫ�õ��Զ��庯��
def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":                #ʹ��if/elif/else��佫������Ϸ�����Ӧ����ͬ������
        number=0
    elif name=="ʷ����":
        number=1
    elif name=="��":
        number=2
    elif name=="����":
        number=3
    else:
        number=4
    return number                 #���ؽ��

def number_to_name(number):
    """
    ��������0,1,2,3 or 4����Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number==0:                # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
        name="ʯͷ"
    elif number==1:
        name="ʷ����"
    elif number==2:
        name="��"
    elif number==3:
        name="����"
    else:
        name="����"
    return name                  #���ؽ��

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """

    print("------------")                                             # ���"-------- "���зָ�
    print("����ѡ��Ϊ%s"%player_choice)                                 # ����Ļ����ʾ�û�ѡ��Ķ���
    player_choice_number=name_to_number(player_choice)                # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    comp_number=random.randrange(0,5)                                 # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_name=number_to_name(comp_number)                             # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("�������ѡ��Ϊ%s"%comp_name)                                   # ����Ļ����ʾ�����ѡ����������
    if comp_number==player_choice_number:                             # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��������û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ���
        print("���ͻ�������һ��")
    else:
        if player_choice_number==0:
            if comp_number==3:
                print("��Ӯ��")
            elif comp_number==4:
                print("��Ӯ��")
            else:
                print("����Ӯ��")
        if player_choice_number==1:
            if comp_number==4:
                print("��Ӯ��")
            elif comp_number==0:
                print("��Ӯ��")
            else:
                print("����Ӯ��")
        if player_choice_number==2:
            if comp_number==0:
                print("��Ӯ��")
            elif comp_number==1:
                print("��Ӯ��")
            else:
                print("����Ӯ��")
        if player_choice_number==3:
            if comp_number==1:
                print("��Ӯ��")
            elif comp_number==2:
                print("��Ӯ��")
            else:
                print("����Ӯ��")
        if player_choice_number==4:
            if comp_number==2:
                print("��Ӯ��")
            elif comp_number==3:
                print("��Ӯ��")
            else:
                print("����Ӯ��")

#�Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")                                         # ����Ļ��ʾ����ӭʹ��RPSLS��Ϸ��
choice_name=input("����������ѡ��")                                # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
if choice_name!="ʯͷ":                                          # ʹ��ifǶ������ж��û���ѡ���ǲ���ʯͷ/����/��/����/ʷ�����е�����һ������������������Error: No Correct Name��
    if choice_name!="����":
        if choice_name!="��":
            if choice_name!="����":
                if choice_name!="ʷ����":
                    print("Error: No Correct Name")

if choice_name=="ʯͷ":                                          # �û���ѡ����ʯͷ/����/��/����/ʷ�����е�����һ��ʱ����rpsls()����
    rpsls(choice_name)
if choice_name=="����":
    rpsls(choice_name)
if choice_name=="��":
    rpsls(choice_name)
if choice_name=="����":
    rpsls(choice_name)
if choice_name=="ʷ����":
    rpsls(choice_name)



