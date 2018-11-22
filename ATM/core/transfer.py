from conf import settings
import time
import os
def user_transfer():
    split_user = []
    '''转账接口'''
    with open(r'D:\ATM\db\register_login.txt', mode='rt', encoding='utf-8') as f2:
        f3 = f2.readlines()
        last_line2 = f3[-1].strip('\n')
    USER_PATH = os.path.join(settings.BASE_DIR, 'db',last_line2)
    print('你已选择转账，当前账户为{}'.format(last_line2))
    with open(settings.DB_PATH, mode='rt', encoding='utf-8') as f5:
        for p in f5:
            p = p.strip('\n')
            p = p.split(':')
            split_user.append(p[0])
    zz_user = input('请输入转账用户:')
    if zz_user in split_user:
        with open(USER_PATH, mode='rt', encoding='utf-8') as file1, \
                open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as file5:
            old_user_yue = file1.readline()
            old_user_yue2 = old_user_yue.strip('\n')
            old_user_yue3 = old_user_yue2.split('|')
            old_user_yue4 = old_user_yue3[-1]
            old_user_xf = old_user_yue3[2]
            zz_old_log = '转账前->源用户为{},源用户消费金额为{},源用户余额为{}'.format(last_line2,old_user_xf,old_user_yue4)
            print(zz_old_log)
            zz_old_time = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file3:
                file3.write('%s\t%s\n' % (zz_old_time, zz_old_log))
            zz_jine = float(input('请输入转账金额：'))
            if float(old_user_yue4) >= zz_jine:
                zh_old_yue = float(old_user_yue4) - zz_jine
                old_user_yue = old_user_yue.replace(old_user_yue4, str(zh_old_yue))
                file5.write(old_user_yue)
                old_user_xf2 = float(old_user_xf) + zz_jine
                file5.write('\n%s' % old_user_yue.replace(str(old_user_xf), str(old_user_xf2)))
                zz_new_log = '转账后源用户{},源用户消费金额为{},余额为{}'.format(last_line2,old_user_xf2,zh_old_yue)
                print(zz_new_log)
                zz_new_time = time.asctime(time.localtime(time.time()))
                with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file10:
                    file10.write('%s\t%s\n' % (zz_new_time, zz_old_log))
            else:
                print('余额不足！退出')
                return 255
        os.remove(USER_PATH)
        os.rename('%s.bak' % USER_PATH, USER_PATH)
        with open(USER_PATH, mode='rt', encoding='utf-8') as file1, \
                open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as file5:
            old_user_zh = []
            for j3 in file1:
                old_user_zh.append(j3)
            if len(old_user_zh) >= 1:
                data = old_user_zh[-1]
                file5.write(data)
        os.remove(USER_PATH)
        os.rename('%s.bak' %USER_PATH, USER_PATH)
        with open('%s\%s' %(settings.USER_PATH2,zz_user), mode='rt', encoding='utf-8') as file3, \
                open('%s\%s.bak' %(settings.USER_PATH2,zz_user), mode='wt', encoding='utf-8') as file4:
            new_user_yue = file3.readline()
            new_user_yue2 = new_user_yue.strip('\n')
            new_user_yue3 = new_user_yue2.split('|')
            new_user_yue4 = new_user_yue3[-1]
            zz_old_log2 = '转账前->目标用户为{},目标用户余额为{}'.format(zz_user, new_user_yue4)
            print(zz_old_log2)
            zz_old_time2 = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file11:
                file11.write('%s\t%s\n' % (zz_old_time2, zz_old_log2))
            print('开始转账')
            zh_new_yue5 = float(new_user_yue4) + zz_jine
            new_user_yue = new_user_yue.replace(str(new_user_yue4), str(zh_new_yue5))
            zz_new_log2 = '转账后->目标用户为{}，目标用户余额为{}'.format(zz_user, zh_new_yue5)
            print(zz_new_log2)
            file4.write(str(new_user_yue))
            zz_new_time2 = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file12:
                file12.write('%s\t%s\n' % (zz_new_time2, zz_new_log2))
        os.remove('%s\%s' %(settings.USER_PATH2,zz_user))
        os.rename('%s\%s.bak' %(settings.USER_PATH2,zz_user),'%s\%s' %(settings.USER_PATH2,zz_user))
    else:
        print('转账用户不存在')
