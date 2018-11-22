from lib import common
from conf import settings


def freeze_user():
    username = input('请输入需要冻结的账户！')
    with open('%s\db.txt' % (settings.USER_PATH2), mode='rt', encoding='utf-8') as f3:
        list1 = []
        for i in f3:
            i = i.strip('\n')
            i = i.split(':')
            list1.append(i[0])
        if username not in list1:
            print('{}用户不存在,无法冻结！')
        else:
            with open(r'%s\freeze' % settings.USER_PATH2, mode='at', encoding='utf-8') as f2:
                f2.write('%s\n' %username)
            print('{}已被冻结，无法登录！'.format(username))
