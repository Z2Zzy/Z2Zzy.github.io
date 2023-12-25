import numpy as np
import random
n_delete = 27 #要删客体分子的个数

num = 648 - 3 * n_delete

num = num + 3726 #小笼内气体原子数 + 大笼内气体原子数 + 水的原子数
check = 0 #判别笼子类型
a_arry = [] #同晶胞内排列
all = [] #整体晶胞的排列
c_out = [] #笼子的排列
f_out = [] #输出用序列

i = 0
j = 0
k = 0

choose = open('..\\result\\choose.txt', 'w')
choose.write("哪些晶胞内的气体将会扣除\n（0为扣除，1为未扣除）\n")
"""将扣除co2后的气体坐标写入"""
count = 0
i = 0
for i in range(216):
    if(i < n_delete):
        all.append(0)
    else:
        all.append(1)
random.shuffle(all)
"""寻找被扣除的晶胞是哪个"""
j = 0
for i in range(27):
    flag = 1
    for j in range(8):
        if(all[i * 8 + j] == 0 ):
            flag -= 1
    if(flag < 1):
        c_out.append(0)
    else:
        c_out.append(1)
print(c_out)
choose.write(str(c_out) + "\n")


for i in range(27):
    if(c_out[i] == 0):
        for j in range(8):
            a_arry.append(all[i * 8 + j])
            if (a_arry[j] == 0):
                f_out.append(0)
                f_out.append(0)
                f_out.append(0)

            else:
                f_out.append(1)
                f_out.append(1)
                f_out.append(1)
        print(a_arry)
        choose.write("第" + str(i+1) + "个晶胞：" + str(a_arry) + "\n")
        a_arry=[]
    else:
        for j in range(24):
            f_out.append(1)


co2_read = open('..\\hyd\\big-and-small.txt', 'r')
line = co2_read.readlines()
resultco2 = open('..\\result\\result.data', 'w')
resultco2.write("# LAMMPS data file written by OVITO Basic 3.5.4\n" + str(num) + " atoms\n\n")
head = open('..\\hyd\\head.txt', 'r')
for hang in head:
    """将data的头文件写入"""
    resultco2.writelines(hang)
i = 0
for i in range(648):
    if (f_out[i] == 1):
        resultco2.writelines(line[i])
#resultco2.write("\n")
"""将水分子坐标写入"""
water = open('..\\hyd\\waterdata.txt')
for line2 in water:
    resultco2.writelines(line2)

"""将每个气体是否存在写入"""
zong = []
flag = 1
sn = 0

for i in range(0,648,3):

    zong.append(f_out[sn])
    sn = sn + 3
    flag = flag + 1
    if(flag == 9):
        flag = 1
choose.write("\n")
choose.write(str(zong) + "\n")

choose.close()
water.close()
co2_read.close()
head.close()
resultco2.close()