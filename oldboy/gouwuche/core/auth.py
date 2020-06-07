
import sys,os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

# from core import db_handler
from conf import settings

def acess_auth(account,password):
    '''
    用户认证函数
    :param account:
    :param password:
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path.account)
    def out_wrapper(func):
        # print(func)
        def wraaper(*args,**kwargs):
                username = input("Username>>>:").strip()
                password = input("Password>>>:").strip()
                if account_data["username"] == username and account_data["passwd"] == password:
                    print("\033[32;1m user has pass auth\033[0m")
                    func(*args,**kwargs)
                else:
                    print("\033[32;1mInvalid username or password\033[0m")
            # elif auth_type == "ldap":
                print("\033[31;1m--ldap方式验证通过----\033[0m")
                func(*args,**kwargs)
            # else:
                print("\033[31;1m 验证方式无效,请重新输入")
                # func(*args,**kwargs)
                exit()
        return wraaper
    return out_wrapper


