import os

h_f= -25.0 #分层起始下限 
h_e = 25  #分层上限
n_layer = 5  #层数
trj = open("test.lammpstrj",'r')  #改为lammpstrj文件名称



h_c= (h_e-h_f)/n_layer #每层高度
if not os.path.exists(".//trajectory"):
    os.mkdir(".//trajectory")
for i in range(n_layer):
    if not os.path.exists(".//trajectory//"+str(i+1)):
        os.mkdir(".//trajectory//"+str(i+1))
name = 0
flag = 0 #判定是否开始写入
for line in trj:
    line = line.strip('\n')
    if(line == 'ITEM: TIMESTEP'):
        flag = 1
        files = {f'file{jj}': open(f".//trajectory//"+str(jj)+"//"+str(name)+".txt", "w") for jj in range(1, n_layer + 1)}

        name =name + 1
        continue
    flag = flag + 1
    if(flag > 9):
        data = line
        data = data.strip('\n')
        data = data.split(' ')
        cs = int((float(data[4])-h_f)/((h_e-h_f)/n_layer))+1
        if(cs<=n_layer and cs>=1):
            files[f'file{cs}'].writelines(line+'\n')


