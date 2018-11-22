# 设置默认路径
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'db', 'db.txt')
LOG_PATH = os.path.join(BASE_DIR, 'log', 'access.log')
REGISTER_LOGIN_PATH = os.path.join(BASE_DIR, 'db', 'register_login.txt')
freeze_user_list = []
freeze_user = os.path.join(BASE_DIR, 'db', 'freeze')
with open(freeze_user, mode='rt', encoding='utf-8') as file1:
    for i3 in file1:
        freeze_user_list.append(i3.strip('\n'))
def user_register():
    while True:
        print('你已选择注册')
        username = input('请输入用户名：').strip()
        with open(DB_PATH, mode='rt', encoding='utf-8') as f, \
                open(DB_PATH, mode='at', encoding='utf-8') as f1, \
                open(REGISTER_LOGIN_PATH, mode='at', encoding='utf-8') as f2:
            list_user = []
            for i in f:
                i = i.strip('\n')
                i = i.split(':')
                list_user.append(i[0])
            if username not in list_user:
                password = input('请输入用户名密码：').strip()
                f1.write('%s:%s\n' % (username, password))
                f2.write('%s\n' % username)
                f2.flush()
                print('{}添加成功'.format(username))
                break
            else:
                print('{}已存在，添加失败！'.format(username))
                continue


def user_log_in():
    while True:
        print('你已选择登录！')
        username = input('请输入用户名：').strip()
        with open(DB_PATH, mode='rt', encoding='utf-8') as f, \
                open(REGISTER_LOGIN_PATH, mode='at', encoding='utf-8') as f2:
            list_user = []
            pwd_user = []
            for i in f:
                i = i.strip('\n')
                i = i.split(':')
                list_user.append(i[0])
                pwd_user.append(i[1])
            if username not in list_user:
                print('{}不存在'.format(username))
                continue
            elif username not in freeze_user_list:
                password = input('请输入密码：')
                if password == pwd_user[list_user.index(username)]:
                    f2.write('%s\n' % username)
                    f2.flush()
                    break
                else:
                    print('密码错误，请重试！')
                    continue
            else:
                print('{}已被冻结，无法登录！'.format(username))
                continue

list_user=[]
with open(REGISTER_LOGIN_PATH, mode='rt', encoding='utf-8') as f:
    for i in f:
        list_user.append(i.strip('\n'))
    last_line=list_user[-1]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_PATH = os.path.join(BASE_DIR, 'db', last_line)
SHOPPING_PATH = os.path.join(BASE_DIR, 'log', last_line)
USER_PATH2=os.path.join(BASE_DIR,'db')

