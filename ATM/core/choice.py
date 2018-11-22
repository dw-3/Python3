import sys
from core import administator, common_user
def choice_user():
    while True:
        print(
            '''
            1:管理员
            2:普通用户
            q:退出
            '''
        )
        choice = input('请选择角色：').strip()
        if choice == '1':
            administator.choice_administator()
        elif choice == '2':
            common_user.user()
        elif choice == 'q':
            print('你已选择退出')
            break
        else:
            choice2 = input('选择错误，是否退出？ y/n').strip()
            if choice2 == 'y':
                print('退出')
                break
            elif choice2 == 'n':
                continue
            else:
                print('输入错误，退出！')
                sys.exit(1)
