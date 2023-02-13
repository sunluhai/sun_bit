money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}绩效分{score},不足5分，不发工资。")
    
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}的积分{score},达5分，领取1000元,工资余额{money}")
    else:
        print("工资发完了，结束发工资")
        break


    # else:
    #     money -= 1000
    #     print(f"员工{i}的积分{score},达5分，领取1000元,工资余额{money}")
    # if money == 0:
    #     print("工资发完了，结束发工资")
    #     break