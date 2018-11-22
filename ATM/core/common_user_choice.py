from core import shopping,withdraw,repayment,transfer,log
def user_choice():
    while True:
        print(
            '''
            1:购物
            2:还款
            3:提现
            4:转账
            q:退出
            '''
        )
        choice = input('请选择：').strip()
        choice_dic={
            '1':shopping.user_shopping,
            '2':repayment.user_repayment,
            '3':withdraw.user_withdraw,
            '4':transfer.user_transfer,
        }
        if choice=='q':
            break
        elif choice not in choice_dic:
            print('选择错误')
            continue
        else:
            choice_dic[choice]()
            log.log()

