"""求出某个自然数的阶乘。一个正整数的阶乘是所有小于等于该数的正整数的积
并且0的阶乘为1，自然数n的阶乘写作n!"""

#方法一：非递归
sum=1
n=int(input("请输入一个自然数："))
while n<0:
    print("输入有误，请重新输入：")
    n = int(input("请输入一个自然数："))
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
def main():
    m = int(input("请输入一个自然数："))
    while m<0:
        print("输入有误，请重新输入：")
        m = int(input("请输入一个自然数："))
    else:
        print(jie_cheng(m))
#执行主程序，原来没有这一句运行直接结束没有结果
if __name__ == '__main__':
    main()


def jie_cheng(num):
    if num == 0:
        return 1
    else:
        return num * jie_cheng(num - 1)


def main():
    while True:
        try:
            user_input = input("请输入一个自然数：")
            m = int(user_input)  # 使用 int() 而不是 eval()

            if m < 0:
                print("输入有误，不能为负数，请重新输入。")
            else:
                result = jie_cheng(m)
                print(f"{m}的阶乘是：{result}")
                break

        except ValueError:
            print("输入有误，请输入一个整数，请重新输入。")
        except RecursionError:
            print("数字太大，超出递归深度限制！")
            break
if __name__ == "__main__":
    main()


'''调用栈（Call Stack）的限制
当函数调用自身时，每次调用都会在内存的"调用栈"中创建一个新的栈帧（Stack Frame），用于存储：
函数的参数
局部变量
返回地址
# 计算 3! 的递归过程
jie_cheng(3)
→ 3 * jie_cheng(2)
    → 2 * jie_cheng(1)
        → 1 * jie_cheng(0)
            → return 1
        → return 1 * 1 = 1
    → return 2 * 1 = 2
→ return 3 * 2 = 6
在这个过程中，调用栈会积累4个栈帧，直到遇到基准情况（num==0）才开始逐层返回。
2. Python的栈深度限制
Python为了防止栈溢出（Stack Overflow）导致程序崩溃，设置了递归深度限制：
默认深度限制通常是 1000 层左右

可以通过 sys.setrecursionlimit() 修改，但不推荐:
import sys
print(sys.getrecursionlimit())  # 通常输出 1000
3. 内存消耗
每个栈帧都占用内存，深度递归会消耗大量内存，可能导致程序变慢甚至崩溃。

为什么迭代版本没有限制？
1. 只使用常量空间
迭代版本只需要固定的几个变量：
def jie_cheng_iterative(num):
    result = 1           # ← 1个变量
    for i in range(1, num + 1):  # ← 1个循环计数器
        result *= i      # ← 简单的乘法运算
    return result
2. 没有函数调用开销
不需要创建新的栈帧
不需要保存返回地址
不需要管理调用关系
'''