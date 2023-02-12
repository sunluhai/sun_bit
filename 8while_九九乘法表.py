i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end='')   #\t:对齐  ，end='' 不会输出换行回车符，连在一行
        j += 1
    i += 1
    print()  # print空内容，就是输出一个换行
