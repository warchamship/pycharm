'''求出某个自然数的阶乘。一个正整数的阶乘是所有小于等于该数的正整数的积
并且0的阶乘为1，自然数n的阶乘写作n!'''

#方法一：非递归
sum=1
n=eval(input("请输入一个自然数："))
while n<0:
    print("输入有误，请重新输入：")
    n = input("请输入一个自然数：")
else:
    for i in range(1,n+1):
        sum*=i
    print(sum)

#方法二：递归
def jie_cheng(num):
    if num==0:
        return 1
    else:
        return num*jie_cheng(num-1)
