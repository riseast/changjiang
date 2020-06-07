#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import json

from conf import settings
from DB import db_handler
from lib import common

def register_interface(username,password,balance):
    # 1,查看用户是否存在
    # 2,调用数据处理层中的select 函数 会返回用户字典或者None
    user_dic = db_handler.select(username)
    #{user:user,pwd:pwd...} or None
    # 2,若用户不存在，则保存用户信息
    if user_dic:
        # return  (False,'用户名已存在!')
        return False, '用户名已存在!'
    # 3,组织用户的数据字典信息
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        # 用于记录用户流水的列表
        'flow': [],
        # 用于记录用户的购物车
        'shop_car': {},
        # locked: 用于记录用户是否被冻结
        # False: 未冻结  True： 已被冻结
        'locaked': False
    }
    #保存数据
    db_handler.save(user_dic)
    return True,f'{username} 注册成功!'
    # 存不是目的，目的是为了更方便的取数据
    # 文件名:用户名.json
    # 拼接用户json文件的路径
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    # 查看用户是否存在
    # 若不存在，则让用户重新受保护
    if os.path.exists(user_path):
        print('请重新输入!')
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
        if user_dic:
            print('用户已存在,请重新输入!')

    # 若用户不存在，则保存用户数据
    # 组织用户的数据字典信息
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    with open(user_path, 'w', encoding='utf-8') as f1:
        json.dump(user_dic, f1, ensure_ascii=False)

def login_interface(username,password):
    user_dic = db_handler.select(username)
    # 先查看当前用户数据是否存在
    if user_dic:
        # password = common.get_pwd_md5(password)
        if password == user_dic.get('password'):
            return True,f'用户: [{username}] 登录成功!'
        else:
            return False, '密码错误'
        return False, '用户不存在,请重新输入!'

