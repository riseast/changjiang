#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
银行相关业务接口

'''
from DB import db_handler
# 提现接口
def withdraw_interface(username,money):
    # 先获取用户字典
    user_dic = db_handler.select(username)
    # 帐户中的金额
    balance = int(user_dic.get('balance'))
    # 提现本金+ 手续费
    money2 = int(money) * 1.05

    #判断用户输入的金额是否大于用户字典里的金额
    if balance > money2:
        # 修改用户字典中的金额
        balance -= money2
        user_dic['balance'] = balance

        # 再保存数据，更新数据
        db_handler.save(user_dic)
        return True,f'用户[{username}] 提现金额[{money}$]成功,手续费为: [{money2 - float(money)}$],余额为: [{balance - money2}$]'
    return False,'提现金额不足，请重新输入!'

def paycash_interface(username,cash):

    #先获取用户字典
    user_dic = db_handler.select(username)
    #获取账户中的金
    user_dic['balance'] += cash
    #更新账户中的金额
    db_handler.save(user_dic)
    return True,f'用户[{username}] 还款金额[{cash}$]成功,余额为: {user_dic["balance"]}$]'
