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
        # 记录流水
        flow = f'用户[{username}] 提现金额[{money}$]成功,手续费为: [{money2 - float(money)}$],余额为: [{balance - money2}$]'
        user_dic['flow'].append(flow)
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

def transfer_interface(login_user,username,money):
    # 先获取转入用户字典
    to_user_dic=db_handler.select(username)
    # 获取转出用户字典
    from_user_dic = db_handler.select(login_user)
    # 获取转入账号中的金额,并转换为数字型
    # balance_in = int(user_dic.get('balance'))
    if from_user_dic['balance'] >= money > 0:
        # 转入账户增加转入金额
        to_user_dic['balance'] += money

        # 获取转出账户中的金额
        from_user_dic['balance'] -= money
        # balance_out = int(user_dic.get('balance'))
        # 更新转入账户中的金额
        db_handler.save(to_user_dic)
        # 更新转出账户中的金额
        db_handler.save(from_user_dic)
    else:
        print('你的余额不足,请重新输入...')
    return True,f'用户[{login_user}] 转出金额[{money}]成功 剩余金额 [{from_user_dic["balance"]}],用户[{username}] 转入金额为: [{money}]'


def check_flow_interface():
    pass

