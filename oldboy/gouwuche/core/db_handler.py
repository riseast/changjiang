# -*- coding:utf-8 -*-
#author:boyang


def file_db_handler(conn_params):
    '''
    parse the db file path
    :param conn_params:
    :return:
    '''


    print('file db:',conn_params)
    db_path = '%s/%s' %(conn_params['path'],conn_params['name'])
    return db_path
def db_handler(conn_parms):
    '''
    connect to db
    :param conn_parms:
    :return:
    '''

    if conn_parms['engine'] == 'file_storage':
        return file_db_handler(conn_parms)