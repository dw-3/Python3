from conf import settings
import os
import time


def quota_ma():
    split_user = []
    username_ma = input('请输入调整额度的用户：')
    user_quota = os.path.join(settings.USER_PATH2,username_ma)
    with open(settings.DB_PATH, mode='rt', encoding='utf-8') as f5:
        for p in f5:
            p = p.strip('\n')
            p = p.split(':')
            split_user.append(p[0])
        if username_ma in split_user:
            with open(user_quota, mode='rt', encoding='utf-8') as f2, \
                    open('%s.bak' %user_quota, mode='wt', encoding='utf-8') as f3:
                xyk_old_edu = f2.readline()
                xyk_old_edu2 = xyk_old_edu.strip('\n')
                xyk_old_edu3 = xyk_old_edu2.split('|')
                xyk_old_edu4 = xyk_old_edu3[1]
                print('当前的登录账户为{},你可以提高额度,因为我不允许自己的钱越来越少，当前用户额度为{}！'.format(username_ma, xyk_old_edu4))
                xyk_new_edu = input('请输入新的额度：').strip()
                xyk_old_edu = xyk_old_edu.replace(xyk_old_edu4, xyk_new_edu)
                f3.write(xyk_old_edu)
                xyk_new_edu = float(xyk_new_edu)
                xyk_new_edu1 = abs(xyk_new_edu - float(xyk_old_edu4)) + float(xyk_old_edu3[3])
                xyk_new_yue = xyk_old_edu.replace(xyk_old_edu3[3], str(xyk_new_edu1))
                f3.write('\n%s' % xyk_new_yue)
            os.remove(user_quota)
            os.rename('%s.bak' %user_quota,user_quota)
            with open(user_quota, mode='rt', encoding='utf-8') as f4, \
                    open('%s.bak' % user_quota, mode='wt', encoding='utf-8') as f6:
                num_list = []
                for f in f4:
                    num_list.append(f)
                if len(num_list) > 1:
                    last_data = num_list[-1]
                    f6.write(last_data)
            os.remove('%s' % user_quota)
            os.rename('%s.bak' % user_quota, user_quota)
            edu_log = '额度调整成功，当前的信用卡额度为{},余额为{}'.format(xyk_new_edu, xyk_new_edu1)
            print(edu_log)
            edu_time = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % username_ma, mode='a+t', encoding='utf-8') as file3:
                file3.write('%s\t%s\n' % (edu_time, edu_log))

        else:
            print('用户不存在！')
