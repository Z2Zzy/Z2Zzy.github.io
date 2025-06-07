import numpy as np
import random
n_delete = 0 #要删笼中客体分子的晶胞个数
n_together = 0 #一个晶胞删除的个数
n_delete2 = 0 #不规则删除的晶胞个数
n_together2 = 0 #不规则删除的一个晶胞内需扣除笼子数

num = 648 - 3 * n_together * n_delete - 3 * n_together2 * n_delete2

num = num + 3726 #小笼内气体原子数 + 大笼内气体原子数 + 水的原子数
check = 0 #判别笼子类型
a_arry = [] #同晶胞内排列
c_out = [] #笼子的排列
f_out = [] #输出用序列

i = 0
j = 0
k = 0

choose = open('..\\result\\choose.txt', 'w')
choose.write("哪些晶胞内的气体将会扣除\n（0为扣除，1为未扣除）\n")
"""写入哪个晶胞需要删除CO2"""
i = 0
flag = -1
if(n_delete2 != 0):
    flag = n_delete2
for i in range(27):
    if (flag > 0): #其中一个晶胞扣除不同个数
        c_out.append(0.5)
        flag -= 1
    elif (i < n_delete + n_delete2):
        c_out.append(0)
    else:
        c_out.append(1)
random.shuffle(c_out)
print(c_out)
choose.write(str(c_out) + "\n")
for i in range(27):
    check = c_out[i]
    if (check == 0.5):
        for l in range(8):
            if(l<n_together2):
                a_arry.append(0)
            else:
                a_arry.append(1)
        random.shuffle(a_arry)
        print(a_arry)
        choose.write("第" + str(i+1) + "个晶胞：" + str(a_arry) + "\n")
        for j in range(8):
             if(a_arry[j] == 0):
                 f_out.append(0)
                 f_out.append(0)
                 f_out.append(0)

             else:
                f_out.append(1)
                f_out.append(1)
                f_out.append(1)

        a_arry=[]
    elif (check == 0) :
        for l in range(8):
            if(l<n_together):
                a_arry.append(0)
            else:
                a_arry.append(1)
        random.shuffle(a_arry)
        print(a_arry)
        choose.write("第" + str(i+1) + "个晶胞：" + str(a_arry) + "\n")
        for j in range(8):
             if(a_arry[j] == 0):
                 f_out.append(0)
                 f_out.append(0)
                 f_out.append(0)

             else:
                f_out.append(1)
                f_out.append(1)
                f_out.append(1)

        a_arry=[]
    else :
         for m in range(24):
             f_out.append(1)

co2_read = open('..\\hyd\\big-and-small.txt', 'r')
line = co2_read.readlines()
resultco2 = open('..\\result\\result.data', 'w')
resultco2.write("# LAMMPS data file written by OVITO Basic 3.5.4\n" + str(num) + " atoms\n\n")
head = open('..\\hyd\\head.txt', 'r')
for hang in head:
    """将data的头文件写入"""
    resultco2.writelines(hang)
"""将co2分子坐标写入"""
i = 0
for i in range(648):
    if (f_out[i] == 1):
        resultco2.writelines(line[i])
#resultco2.write("\n")
"""将水分子坐标写入"""
water = open('..\\hyd\\waterdata.txt')
for line2 in water:
    resultco2.writelines(line2)

"""将每个气体是否存在写入choose"""
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