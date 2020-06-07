#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
存放公共方法
'''

import hashlib

#md5加密

def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '一二三四五，上山打老虎'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()