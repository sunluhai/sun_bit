print("欢迎来到儿童游乐园，儿童免费，成人收费。")
age =int(input("请输入你的年龄："))
#age = int(age)
if age >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可免费游玩")
print("祝您游戏愉快。")