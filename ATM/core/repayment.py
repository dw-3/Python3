from conf import settings
import time
import os


def user_repayment():
    '''还款接口'''
    with open(r'D:\ATM\db\register_login.txt', mode='rt', encoding='utf-8') as f2:
        f3 = f2.readlines()
        last_line2 = f3[-1].strip('\n')
    USER_PATH = os.path.join(settings.BASE_DIR, 'db',last_line2)
    print('你已选择还款，当前账户为{}'.format(last_line2))
    with open(USER_PATH, mode='rt', encoding='utf-8') as zfile \
            , open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as zfile2:
        user_qingkuang = zfile.readline()
        user_qingkuang1 = user_qingkuang.strip('\n')
        user_qingkuang2 = user_qingkuang.split('|')
        qianfei = user_qingkuang2[2]
        print('你的需还款金额为{},你的余额为{}'.format(qianfei, user_qingkuang2[3]))
        cc_hk = float(input('请输入你此次还款金额:').strip())
        if cc_hk <= float(qianfei):
            now_qk = float(user_qingkuang2[2]) - cc_hk
            user_qingkuang = user_qingkuang.replace(str(qianfei), str(now_qk))
            zfile2.write('%s\n' % user_qingkuang)
            now_yue = float(user_qingkuang2[3]) + cc_hk
            user_now_yue = user_qingkuang.replace(str(user_qingkuang2[3]), str(now_yue))
            zfile2.write(user_now_yue)
            huankuan_log = '你此次还款金额为{},余额为{}'.format(cc_hk, now_yue)
            print(huankuan_log)
            huankuan_time = time.asctime(time.localtime(time.time()))
            with open('%s.shopping_log' % settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file3:
                file3.write('%s\t%s\n' % (huankuan_time, huankuan_log))
        else:
            print('输入的还款金额不正确')
    os.remove(USER_PATH)
    os.rename('%s.bak' % USER_PATH, USER_PATH)
    with open(USER_PATH, mode='rt', encoding='utf-8') as zfile3, \
            open('%s.bak' % USER_PATH, mode='wt', encoding='utf-8') as zfile4:
        huankuan_list = []
        for j2 in zfile3:
            huankuan_list.append(j2)
        if len(huankuan_list) >= 1:
            zfile4.write(huankuan_list[-1])
    os.remove(USER_PATH)
    os.rename('%s.bak' %USER_PATH, USER_PATH)
