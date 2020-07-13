#约瑟夫环：（n个人，最后只留一个人活着,输出被杀次序）

# ！/usr/bin/env python3  # 根据PATH环境变量中指定的第一个python解释器，执行python脚本
# coding=utf-8  # 声明该文件的编码格式为 utf-8

def skilled_Joseph_ring(num, step):
    input_ = [x for x in range(1, num + 1)]
    output_killed = []
    
    for i in range(num-1):
        killed_index = (step-1) % len(input_)
        killed = input_[(step-1) % len(input_)]
        output_killed.append(killed)
        
        start_index = (killed_index + 1) % len(input_)
        end_index = (killed_index - 1) % len(input_)
        
        if killed_index == 0:
            input_ = input_[start_index:]
        elif killed_index == len(input_)-1:
            input_ = input_[:end_index+1] 
        else:
            input_ = input_[start_index:] + input_[:end_index+1]
    return output_killed
    

#测试代码：

killed = skilled_Joseph_ring(7, 8) 
assert(killed == [1,3,6,5,2,7])

killed = skilled_Joseph_ring(7, 7) 
assert(killed == [7,1,3,6,2,4])

killed = skilled_Joseph_ring(7, 6) 
assert(killed == [6,5,7,2,1,4])

killed = skilled_Joseph_ring(7, 5) 
assert(killed == [5,3,2,4,7,1])

killed = skilled_Joseph_ring(7, 4) 
assert(killed == [4,1,6,5,7,3])

killed = skilled_Joseph_ring(7, 3) 
assert(killed == [3,6,2,7,5,1])

killed = skilled_Joseph_ring(7, 2) 
assert(killed == [2,4,6,1,5,3])