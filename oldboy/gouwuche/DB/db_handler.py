#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
数据处理层
    - 专门用户处理数据的
'''


import json
import os
from conf import settings

# 查看数据

def select(username):
    '''
    接收接口层传过来的username用户名,拼接用户json文件路径
    :param username:
    :return:
    '''
    user_path = os.path.join(
        settings.USER_DATA_PATH, f'{username}.json'
    )
    # 校验用户json文件是否存在
    if os.path.exists(user_path):
        #打开数据，并返回给接口层
        with open(user_path,'r',encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


#保存数据
def save(user_dic):
    # 拼接用户的数据字典
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH,f'{username}.json'
    )

    with open(user_path,'w',encoding='utf-8')as f:
        #ensure_ascii=False 让文件中的中文数据，显示中文，默认显示字节
        json.dump(user_dic,f,ensure_ascii=False)