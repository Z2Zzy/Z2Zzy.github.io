import numpy as np
import random
n_smalldelete = 0 #要删小笼中客体分子的小笼晶胞个数
n_smalltogether = 0 #一个晶胞删除小笼的个数（1 or 2）
n_bigdelete = 0 #要删客体分子的的大笼晶胞个数（0 - 27）
n_bigtogether = 0 #一个晶胞删除大笼的个数（1 - 6）

numsmall = 162 - 3 * n_smalltogether * n_smalldelete
numbig = 486 - 3 * n_bigtogether * n_bigdelete
num = numbig + numsmall + 3726 #小笼内气体原子数 + 大笼内气体原子数 + 水的原子数
check = 0 #判别笼子类型
a_arry = [] #同晶胞内排列
c_big = [] #小笼子的排列
c_small = [] #大笼子的排列
f_bigout = [] #输出用序列
f_smallout = [] #输出用序列

i = 0
j = 0
k = 0

choose = open('..\\result\\choose.txt', 'w')
choose.write("哪些晶胞内的气体将会扣除\n（0为扣除，1为未扣除）\n")

"""将扣除co2后的小笼气体坐标写入"""
choose.write("\n\n以下为小笼扣除序列：\n")
i = 0
for i in range(27):
    if (i < n_smalldelete):
        c_small.append(0)
    else:
        c_small.append(1)
random.shuffle(c_small)
choose.write(str(c_small) + "\n")
for i in range(27):
    check = c_small[i]
    if (check == 0) :
        for l in range(2):
            if(l<n_smalltogether):
                a_arry.append(0)
            else:
                a_arry.append(1)
        random.shuffle(a_arry)
        choose.write("第" + str(i + 1) + "个晶胞：" + str(a_arry) + "\n")
        for j in range(2):
             if(a_arry[j] == 0):
                 f_smallout.append(0)
                 f_smallout.append(0)
                 f_smallout.append(0)

             else:
                f_smallout.append(1)
                f_smallout.append(1)
                f_smallout.append(1)

        a_arry=[]
    else :
         for m in range(6):
             f_smallout.append(1)

smallco2_read = open('..\\hyd\\small.txt', 'r')
line = smallco2_read.readlines()
resultco2 = open('..\\result\\result.data', 'w')
resultco2.write("# LAMMPS data file written by OVITO Basic 3.5.4\n" + str(num) + " atoms\n\n")
head = open('..\\hyd\\head.txt', 'r')
for hang in head:
    """将data的头文件写入"""
    resultco2.writelines(hang)
i = 0
for i in range(162):
    if (f_smallout[i] == 1):
        resultco2.writelines(line[i])

smallco2_read.close()
head.close()

"""将扣除co2后的大笼气体坐标写入"""
choose.write("\n\n以下为大笼扣除序列：\n")
i = 0
for i in range(27):
    if (i < n_bigdelete):
        c_big.append(0)
    else:
        c_big.append(1)
random.shuffle(c_big)
choose.write(str(c_big) + "\n")
i = 0
for i in range(27):
    check = c_big[i]
    if (check == 0) :
        for l in range(6):
            if(l<n_bigtogether):
                a_arry.append(0)
            else:
                a_arry.append(1)
        random.shuffle(a_arry)
        choose.write("第" + str(i + 1) + "个晶胞：" + str(a_arry) + "\n")
        for j in range(6):
            if(a_arry[j] == 0):
                f_bigout.append(0)
                f_bigout.append(0)
                f_bigout.append(0)

            else:
                f_bigout.append(1)
                f_bigout.append(1)
                f_bigout.append(1)

        a_arry = []
    else:
        for m in range(18):
            f_bigout.append(1)

bigco2_read = open('..\\hyd\\big.txt', 'r')
line = bigco2_read.readlines()

i = 0
for i in range(486):
    if (f_bigout[i] == 1):
        resultco2.writelines(line[i])

bigco2_read.close()
head.close()

"""将水分子坐标写入"""
water = open('..\\hyd\\waterdata.txt')
for line2 in water:
    resultco2.writelines(line2)


"""将每个气体是否存在写入"""
zong = []
flag = 1
sn = 0
bn = 0
for i in range(0,648,3):
    if(flag ==2 or flag == 7):
        zong.append(f_smallout[sn])
        sn = sn + 3
    else:
        zong.append(f_bigout[bn])
        bn = bn + 3
    flag = flag + 1
    if(flag == 9):
        flag = 1
choose.write("\n")
choose.write(str(zong) + "\n")

choose.close()
water.close()
resultco2.close()
