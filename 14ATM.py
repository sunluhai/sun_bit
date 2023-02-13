money = 5000000
name = input("输入您的名称")


def yu(show):
    if show:
        print("-------查询余额-------")
    print(f"{name},您好，您的余额剩余：{money}")


def cun(num):
    global money
    money += num
    print("-------存款-------")
    print(f"{name},您好，您存款{num}元成功")
    yu(False)



def qu(num):
    global money
    money += num
    print("-------取款-------")
    print(f"{name},您好，您取款{num}元成功")
    yu(False)


def main():
    print("--------------------")
    print(f"{name},您好，欢迎来到银行ATM，请选择操作：")
    print("查看余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入你的选择")


while True:
    keybord_input = main()
    if keybord_input == "1":
        yu(True)
        continue
    elif keybord_input == "2":
        num = int(input("您要存款的金额:"))
        cun(num)
        continue
    elif keybord_input == "3爬虫":
        num = int(input("您要取款的金额:"))
        qu(num)
        continue
    else:
        print("程序退出了！")
        break

