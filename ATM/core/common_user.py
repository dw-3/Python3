from conf import settings
from core import common_user_choice
import sys


def registerr(func):
    def wapper(*args, **kwargs):
        settings.user_register()
        res = func()
        return res

    return wapper


def logger_in(func):
    def wapper(*args, **kwargs):
        settings.user_log_in()
        res = func()
        return res

    return wapper


@logger_in
def log_in():
    print('登录成功')


@registerr
def register():
    print('注册且已登录成功')


choice_dic = {
    '1': register,
    '2': log_in,
}


def user():
    while True:
        print('你已选择普通用户！')
        print(
            '''
            1:注册
            2:登录
            q:退出
            '''
        )
        choice = input('请选择：').strip()
        if choice == 'q':
            print('你已选择退出！')
            break
        elif choice not in choice_dic:
            print('选择错误,请重新选择！')
            continue
        else:
            choice_dic[choice]()
            common_user_choice.user_choice()
