
from conf import settings
def register():
    print('注册')
    username = input('username:').strip()
    password = input('password:').strip()
    print(settings.DB_PATH)
    with open(settings.DB_PATH, mode='a', encoding='utf-8') as f:
        f.write('{}:{}\n'.format(username,password))
        print('{}注册成功'.format(username))
def withdraw():
    print('提现')
def transfer():
    print('转账')
def pay():
    print('支付')
func_dic={
    '1':register,
    '2':pay,
    '3':transfer,
    '4':withdraw,
}
def run():
    while True:
        print(
            '''
            1 注册
            2 支付
            3 转账
            4 提现
            '''
        )
        choice=input('请输入：').strip()
        if choice in func_dic:
            func_dic[choice]()
        else:
            print('输入错误！')
            continue
if __name__ == '__main__':
    run()