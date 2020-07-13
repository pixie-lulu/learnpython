#约瑟夫环 （n个人，最后只留一个人活着,直接输出活着的人编号）
'''
问题描述：
n个人围成一个圈，按 1，2，...，n 依次编号。第一个人从 1 开始报数，数到 k 的人会被杀掉，然后下一个人重新从 1 开始报数。如此往复，直到最后只剩下一个人。问题是，你应该如何选择自己的初始位置，才能保证最后不被杀掉呢？
问题分析：
假设最终活下来的人，在原序列中第一次排序编号为Pn,第二次重新排序后编号为Pn-1。我们可知规律：(Pn-1 + k) % n = Pn
'''

# ！/usr/bin/env python3  # 根据PATH环境变量中指定的第一个python解释器，执行python脚本
# coding=utf-8  # 声明该文件的编码格式为 utf-8

def alive_Joseph_ring(num, step):

    if num == 1:
        return num
    if (alive_Joseph_ring(num - 1, step) + step) % num == 0:
        return num
    return (alive_Joseph_ring(num - 1, step) + step) % num


#测试代码：

alive = alive_Joseph_ring(7, 8) 
assert(alive == 4)

alive = alive_Joseph_ring(7, 7) 
assert(alive == 5)

alive = alive_Joseph_ring(7, 6) 
assert(alive == 3)

alive = alive_Joseph_ring(7, 5) 
assert(alive == 6)

alive = alive_Joseph_ring(7, 4) 
assert(alive == 2)

alive = alive_Joseph_ring(7, 3) 
assert(alive == 4)

alive = alive_Joseph_ring(7, 2) 
assert(alive == 7)

