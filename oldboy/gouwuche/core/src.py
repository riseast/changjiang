#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import os
from conf import settings
from interface import user_interface
from lib import common
from interface import bank_interface
login_user = None
# 1.注册功能
def register():
    while True:
        # 1) 让用户输入用户名与密码进行校验
        username = input("请输入用户名>>>:").strip()
        password = input("请输入密码>>>:").strip()
        re_passwd = input("输入正确的密码>>>:").strip()
        #可以输入自定义的金额
        balance = input("请输入要存入银行卡的金额>>>:").strip()
        # 小的逻辑处理：比如两次密码是否一致
        if password == re_passwd:
            # 调用接口层的注册接口，将用户名与密码交给接口层来处理
            flag,msg = user_interface.register_interface(username,password,balance)
            #根据falg判断用户注册是否成功,flag控制break结束
            if flag:
                print(msg)
                break
            else:
                print(msg)



# 2.登录功能
def login():
    while True:
        # 让用户输入用户名与密码
        username = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        # 调用接口层，将数据传给登录接口
        # (True f'用户：·[{username}] 登录成功!')
        # (return False,'密码错误'),(False, '用户不存在,请重新输入')
        flag,msg = user_interface.login_interface(username,password)
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)
# 3.查看余额
@common.login_auth
def check_blance():
    balance = user_interface.check_balance(login_user)
    print(f'用户[{login_user}] 帐户余额为: {balance}')

# 4.提现功能
@common.login_auth
def withdraw():
    while True:
        # 让用户输入提现金额
        input_money = input('请输入提现金额:')
        # 判断用户输入的金额是否是数字
        if not input_money.isdigit():
            print('请重新输入')
            continue
        # 用户输入的提现金额，将提现金额交付给接口层来处理
        flag,msg = bank_interface.withdraw_interface(login_user,input_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 5.还款功能
def repay():
    pass
# 6.转账功能
def transfer():
    pass
# 7.查看流水
def check_flow():
    pass

# 8.购物功能
def shopping():
    pass

# 9.查看购物车
def check_shop():
    pass
# 10.管理员功能
def admin():
    pass

# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_blance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop,
    '10': admin,
}


# 视图层主程序
def run():

    while True:
        print('''
        ============ATM + 购物车==========
            1. 注册功能
            2. 登录功能
            3. 查看余额
            4. 提现功能
            5. 还款功能
            6. 转账功能
            7. 查看流水
            8. 购物功能
            9. 查看购物车
            10. 管理员功能
        ===========END=============
        ''')
        choice = input('请输入功能编号:').strip()

        if choice not in func_dic:
            print('请输入正确的功能编号!')
            continue
        func_dic.get(choice)()
