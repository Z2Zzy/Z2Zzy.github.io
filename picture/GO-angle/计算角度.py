import numpy as np
import os

framenum = 2 #帧数
n_layer = 5 #切片层数

def calculate_angle_between_triangle_and_horizontal_plane(x, y, z):
    # 计算三角形的法向量
    normal_vector = np.cross(y - x, z - x)

    # 水平面的法向量是(0, 0, 1)
    horizontal_vector = np.array([0, 0, 1])

    # 计算两个向量的夹角
    dot_product = np.dot(normal_vector, horizontal_vector)
    magnitudes = np.linalg.norm(normal_vector) * np.linalg.norm(horizontal_vector)

    # 使用 arccos 计算夹角（弧度）
    angle_radians = np.arccos(dot_product / magnitudes)

    # 将弧度转换为度
    angle_degrees = np.degrees(angle_radians)

    return angle_degrees



if not os.path.exists(".//angle"):
    os.mkdir(".//angle")

files = {f'file{jj}': open(f".//angle//"+str(jj)+".txt", "w") for jj in range(1, n_layer + 1)}
all = open('.//angle//all.txt','w')
for i in range(framenum):

    rings = []
    source_ring = open('ring//'+str(i)+'.txt')
    for line in source_ring:
        list_ring = []
        line = line.strip('\n')
        data = line.split(' ')
        list_ring.append(int(data[0]))
        list_ring.append(int(data[1]))
        list_ring.append(int(data[2]))
        list_ring.append(int(data[3]))
        list_ring.append(int(data[4]))
        list_ring.append(int(data[5]))
        rings.append(list_ring)
    source_ring.close()
    all.writelines(str(i)+' ')
    for j in range(n_layer):
        angles = []  # 保存角度
        layerC = open('trajectory//'+str(j+1)+'//'+str(i)+'.txt')
        xh=[]
        Cx=[]
        Cy=[]
        Cz=[]
        setC = set()
        for line in layerC:
            line = line.strip('\n')
            data = line.split(' ')
            xh.append(int(data[0]))
            setC.add(int(data[0]))
            Cx.append(float(data[2]))
            Cy.append(float(data[3]))
            Cz.append(float(data[4]))
        layerC.close()
        for k in range(len(rings)):
            if((rings[k][0] in setC) and (rings[k][1] in setC) and (rings[k][2] in setC) and (rings[k][3] in setC) and (rings[k][4] in setC) and (rings[k][5] in setC)):
                a0 = -1
                a1 = -1
                a2 = -1
                for kk in range(len(xh)):
                    if(rings[k][0] == xh[kk]):
                        a0 = kk
                    elif(rings[k][2] == xh[kk]):
                        a1 = kk
                    elif (rings[k][4] == xh[kk]):
                        a2 = kk
                a0_list = []
                a1_list = []
                a2_list = []
                a0_list.append(Cx[a0])
                a0_list.append(Cy[a0])
                a0_list.append(Cz[a0])
                a1_list.append(Cx[a1])
                a1_list.append(Cy[a1])
                a1_list.append(Cz[a1])
                a2_list.append(Cx[a2])
                a2_list.append(Cy[a2])
                a2_list.append(Cz[a2])
                a00 = np.array(a0_list)
                a11 = np.array(a1_list)
                a22 = np.array(a2_list)
                jd = calculate_angle_between_triangle_and_horizontal_plane(a00, a11, a22)
                angles.append(jd)
        for ll in range(len(angles)):
            if(angles[ll]>90):
                angles[ll] = abs(angles[ll]-180)
        sum = 0
        for ll in range(len(angles)):
            sum = sum + angles[ll]
        ave = 0
        if(len(angles) != 0):
            ave = sum / len(angles)

        files[f'file{j+1}'].writelines(str(ave) + '\n')

        all.writelines(str(ave) + ' ')
    all.writelines('\n')
    print(str(i)+'已完成')






