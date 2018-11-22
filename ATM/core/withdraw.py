from conf import settings
import time


def user_withdraw():
    z_list = []
    import os
    '''提现接口'''
    print('你已选择提现，提现手续费为5%')
    with open(r'D:\ATM\db\register_login.txt', mode='rt', encoding='utf-8') as f2:
        f3 = f2.readlines()
        last_line2 = f3[-1].strip('\n')
    USER_PATH = os.path.join(settings.BASE_DIR, 'db',last_line2)
    with open(USER_PATH, mode='rt', encoding='utf-8') as file4 \
            , open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as file5:
        xyk_old_edu = file4.readline()
        xyk_old_edu2 = xyk_old_edu.strip()
        xyk_old_edu3 = xyk_old_edu2.split('|')
        xyk_old_yue = xyk_old_edu3[3]
        print('你的余额为{}，你的最大提现金额为{}'.format(xyk_old_yue, xyk_old_yue))
        xyk_tixian = float(input('请输入你的提现金额：'))
        if xyk_tixian <= float(xyk_old_yue):
            haunkuan = float(xyk_old_edu3[2]) + xyk_tixian + xyk_tixian * 0.05
            xyk_new_yue = float(xyk_old_yue) - xyk_tixian
            xyk_old_edu = xyk_old_edu.replace(xyk_old_edu3[3], str(xyk_new_yue))
            file5.write(xyk_old_edu)
            xyk_old_huankuan = xyk_old_edu3[2]
            xyk_old_edu2 = xyk_old_edu.replace(xyk_old_huankuan, str(haunkuan))
            file5.write('\n%s' % xyk_old_edu2)
            tixian_log = '你的提现额度为{},手续费为{}，还款金额为{},余额为{}' \
                .format(xyk_tixian, xyk_tixian * 0.05, haunkuan, xyk_new_yue)
            print(tixian_log)
            tixian_time = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file3:
                file3.write('%s\t%s\n' % (tixian_time, tixian_log))
        else:
            print('额度不够，你的余额为{}，你的提现额度为{}'.format(xyk_old_yue, xyk_tixian))
    os.remove(USER_PATH)
    os.rename('%s.bak' % USER_PATH, USER_PATH)
    with open(USER_PATH, mode='rt', encoding='utf-8') as file6 \
            , open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as file7:
        for z in file6:
            z_list.append(z)
        if len(z_list) >= 1:
            file7.write(z_list[-1])
    os.remove(USER_PATH)
    os.rename('%s.bak' % USER_PATH, USER_PATH)
