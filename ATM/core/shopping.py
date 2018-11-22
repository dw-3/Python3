from conf import settings
import time
import sys
import os


def user_shopping():
    '''购物车接口'''
    shopping_goods = []
    shopping_price = []
    shopping_total_price = 0
    product_list = [['IphoneXS', 8600],
                    ['Coffee', 30],
                    ['MacBookPro', 16800],
                    ['Python Book', 99],
                    ['Bike', 199],
                    ['Samsung Galaxy Note9', 6999]]
    money = input('请输入信用卡额度：').strip()
    if int(money) >= 30:
        with open(settings.REGISTER_LOGIN_PATH, mode='rt', encoding='utf-8') as f:
            lines = f.readlines()
            last_line = lines[-1].strip('\n')
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            USER_PATH = os.path.join(BASE_DIR, 'db', last_line)
            while True:
                print('商品如下:')
                for i in range(len(product_list)):
                    print('\t商品名称为{},商品编号为{},价格为{}'.format(product_list[i][0], i + 1, product_list[i][1]))
                choice_number = int(input('请选择商品编号:').strip())
                if 1 <= choice_number <= 6:
                    choice_count = int(input('请输入购买个数:').strip())
                    for j in range(len(product_list)):
                        if j + 1 == choice_number:
                            shopping_goods.append(product_list[j][0])
                            shopping_price.append(product_list[j][1] * choice_count)
                            shopping_total_price += product_list[j][1] * choice_count
                            money2 = int(money)
                            surplus_money = money2 - shopping_total_price
                            if surplus_money >= 30:
                                print('你已购买的商品如下:')
                                for goods in shopping_goods:
                                    print(goods,end=',')
                                shopping_log = '你当前的登录账户为{},此次消费金额为{},总还款金额为{},余额为{}' \
                                    .format(last_line,product_list[j][1] * choice_count,
                                            shopping_total_price, surplus_money)
                                print(shopping_log)
                                shopping_time = time.asctime(time.localtime(time.time()))
                                with open('%s.shopping_log' %settings.SHOPPING_PATH, mode='a+t', encoding='utf-8') as file3:
                                    file3.write('%s\t%s\n' %(shopping_time, shopping_log))
                                with open('%s' % USER_PATH, mode='w+t', encoding='utf-8') as l1:
                                    l1.write('%s|' % last_line)
                                    l1.write('%s|' % money)
                                    shopping2_total_price = str(shopping_total_price)
                                    l1.write('%s|' % shopping2_total_price)
                                    l1.write(str(surplus_money))
                                    l1.write('\n')
                                choice_again = input('是否继续购买? y/n:')
                                if choice_again == 'y' or choice_again == 'Y':
                                    break
                                elif choice_again == 'n' or choice_again == 'N':
                                    print('你选择退出!')
                                    print('你已购买的商品如下:')
                                    for goods in shopping_goods:
                                        print(goods, end=',')
                                    print('你当前的登录账户为{},此次总消费金额为{},总还款金额为{},余额为{}' \
                                          .format(last_line,product_list[j][1] * choice_count,
                                                  shopping_total_price,surplus_money))
                                    with open('%s' % USER_PATH, mode='w+t', encoding='utf-8') as l2:
                                        l2.write('%s|' % last_line)
                                        l2.write('%s|' % money)
                                        shopping3_total_price = str(shopping_total_price)
                                        l2.write('%s|' % shopping3_total_price)
                                        l2.write(str(surplus_money))
                                        l2.write('\n')
                                    return 0
                                else:
                                    print('输入错误,将退出')
                                    return 1
                            else:
                                print('余额不足，将退出！')
                                sys.exit(1)
                        else:
                            continue
                else:
                    print('请输入1-6之间的整数!')
    else:
        print('额度无法购买')
