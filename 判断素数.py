#素数是因数只有1和他本身的自然数
a=37
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
if flag:
    print("是合数")
else:
    print("是素数")

b=eval(input("请输入一个数："))
while b<=1:
    print("输入数字有误，请重新输入")
    b = eval(input("请输入一个数："))
else:
    for i in range(2,b):
        if b%i==0:
            flag=True
            break
    if flag:
        print("是合数")
    else:
        print("是素数")



