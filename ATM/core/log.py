from conf import settings
def log():
    choice=input('是否打印消费流水和ATM操作日志？-->y/n:')
    if choice=='y':
        with open('%s.shopping_log' %settings.SHOPPING_PATH,mode='rt',encoding='utf-8') as f6:
            log_shopping=f6.read()
            print(log_shopping.strip('\n'))