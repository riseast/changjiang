# -*- coding:utf-8 -*-
#author:boyang

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


DATABASE = {
    'engine': 'file_storage',
    'name': 'user_info',
    'path': "%s/db" % BASE_DIR
}