from conf import settings
from core import freeze, user_quota_management


def choice_administator():
    adm_name = input('管理员用户名：').strip()
    adm_pwd = input('管理员密码：').strip()
    while True:
        if adm_name == 'admin' and adm_pwd == 'admin':
            print('管理员认证通过')
            print(
                '''
                1:添加用户
                2:用户额度管理
                3:冻结用户
                q:退出
                '''
            )
        else:
            print('认证错误！')
            continue
        choice_dic = {
            '1': add_user,
            '2': user_quota,
            '3': user_freeze,
        }
        choice = input('请选择：')
        if choice == 'q':
            print('你已选择退出！')
            break
        elif choice in choice_dic:
            choice_dic[choice]()
        else:
            print('输入错误！')


def add_user():
    settings.user_register()


def user_quota():
    user_quota_management.quota_ma()


def user_freeze():
    freeze.freeze_user()
