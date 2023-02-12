count = 0
import random
num = random.randint(1, 100)
flag = True
while flag:
    guess_num = int(input("请输入你要猜的数字"))
    count += 1
    if guess_num == num:
        print("中了！！")
        flag = False
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")

print(f"猜测的次数为：{count}")
