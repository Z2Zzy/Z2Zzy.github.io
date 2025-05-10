import argparse
import ctypes

import os



from math import fabs

import numpy as np
from goto import with_goto
cpp = ctypes.CDLL(r'./ICO.so')
cpp.angleCheck.restype = ctypes.c_double
def vector(atomi, atomj):
    disx = atomi[1] - atomj[1]
    disy = atomi[2] - atomj[2]
    disz = atomi[3] - atomj[3]
    return (disx, disy, disz)
def checkBoundary(x, y, z):
    (x1, x2) = x.split(maxsplit=2)
    (y1, y2) = y.split(maxsplit=2)
    (z1, z2) = z.split(maxsplit=2)
    LX = float(x2) - float(x1)
    LY = float(y2) - float(y1)
    LZ = (float(z2) - float(z1))
    return LX, LY, LZ, x2, x1, y2, y1, z2, z1
def checkPBC(matrix, box,cutoff):
    [LX, LY, LZ, x2, x1, y2, y1, z2, z1] = box
    listcopy = []
    dO_O = cutoff
    for atomsarray in matrix:
        dx = fabs(atomsarray[0][1] - float(x2))
        dy = fabs(atomsarray[0][2] - float(y1))
        dz = fabs(atomsarray[0][3] - float(z1))
        if (dx <= dO_O or dy <= dO_O or dz <= dO_O):
            if dx <= dO_O:
                movex = -LX
                k = [atomsarray[0][0], atomsarray[0][1] + movex, atomsarray[0][2], atomsarray[0][3]]

                listcopy.append([k])
            if dy <= dO_O:
                movey = LY
                k = [atomsarray[0][0], atomsarray[0][1], atomsarray[0][2] + movey, atomsarray[0][3]]

                listcopy.append([k])
            if dz <= dO_O:
                movez = LZ
                k = [atomsarray[0][0], atomsarray[0][1], atomsarray[0][2], atomsarray[0][3] + movez]

                listcopy.append([k])
            if dx <= dO_O and dy <= dO_O:
                movex = -LX
                movey = LY
                movez = 0
                k = [atomsarray[0][0], atomsarray[0][1] + movex, atomsarray[0][2] + movey, atomsarray[0][3] + movez]

                listcopy.append([k])
            if dx <= dO_O and dz <= dO_O:
                movex = -LX
                movez = LZ
                movey = 0
                k = [atomsarray[0][0], atomsarray[0][1] + movex, atomsarray[0][2] + movey, atomsarray[0][3] + movez]

                listcopy.append([k])
            if dy <= dO_O and dz <= dO_O:
                movex = 0
                movey = LY
                movez = LZ
                k = [atomsarray[0][0], atomsarray[0][1] + movex, atomsarray[0][2] + movey, atomsarray[0][3] + movez]

                listcopy.append([k])
            if dx <= dO_O and dy <= dO_O and dz <= dO_O:
                movex = -LX
                movey = LY
                movez = LZ
                k = [atomsarray[0][0], atomsarray[0][1] + movex, atomsarray[0][2] + movey, atomsarray[0][3] + movez]

                listcopy.append([k])
        else:
            pass
    return listcopy

def data_extractor(line):
    (aid, atype, ax, ay, az) = line.split(maxsplit=4)
    return [float(aid), float(ax), float(ay), float(az)]


def search_neighbor(matrix, atomcopy,cutoff):
    listj = []
    listneighboring = []
    arr, col, _ = matrix.shape
    dO_O = cutoff
    dO_O2 = cutoff ** 2

    for i in range(arr):
        idi = matrix[i][0][0]
        dist = np.square(matrix[i][0][1:] - matrix[:, 0, 1:]).sum(axis=1)
        for j in np.where(dist <= dO_O2)[0]:
            da = dist[j]
            if i == j:
                continue
            else:

                if j not in listj:
                    listj.append(j)

        whereCopy = np.where(atomcopy[:, 0, 0] == idi)
        for copyorder in whereCopy[0]:
            dist = np.square(atomcopy[copyorder][0][1:] - matrix[:, 0, 1:]).sum(axis=1)
            for order in np.where(dist <= dO_O2)[0]:
                distic = dist[order]


                if order not in listj:
                    listj.append(order)

        for copyorder in whereCopy[0]:
            dist = np.square(atomcopy[copyorder][0][1:] - atomcopy[:, 0, 1:]).sum(axis=1)
            for N in np.where(dist <= dO_O2)[0]:
                distic = dist[N]
                if N == copyorder:
                    continue
                else:

                    wherem = np.where(matrix[:, 0, 0] == atomcopy[N][0][0])
                    for order in wherem[0]:
                        if order not in listj:
                            listj.append(order)

        dist = np.square(matrix[i][0][1:] - atomcopy[:, 0, 1:]).sum(axis=1)
        for orderC2 in np.where(dist <= dO_O2)[0]:
            distci = dist[orderC2]
            if distci >= 3 * dO_O2:
                print('wrong!/n')

            wherem = np.where(atomcopy[orderC2][0][0] == matrix[:, 0, 0])
            for order in wherem[0]:
                if order not in listj:
                    listj.append(order)

        listneighboring.append(listj.copy())
        listj = []
    return listneighboring
@with_goto
def ring_identification(listmap):
    list4ring = []
    list4pair = []
    list5ring = []
    list5pair = []
    list6ring = []
    list6pair = []
    for host in range(len(listmap)):
        if len(listmap[host]) <= 2:
            pass
        else:
            for node1 in listmap[host]:
                if len(listmap[node1]) < 2:
                    continue
                else:
                    for node2 in listmap[node1]:
                        if node2 == host:
                            label.new2
                            continue
                        elif len(listmap[node2]) < 2:
                            continue
                        for node3 in listmap[node2]:
                            if (node3 in listmap[host]) and (node3 != node1):

                                goto.new2
                        for node3 in listmap[node2]:
                            if node3 == host:
                                continue
                            elif node3 == node1:
                                continue
                            elif len(listmap[node3]) < 2:
                                continue
                            for node4 in listmap[node3]:
                                if (node4 in listmap[host]) and (node4 not in [node1, node2, host]):

                                    goto.new2
                            for node4 in listmap[node3]:
                                if node4 == node1:
                                    continue
                                elif node4 == node2:
                                    continue
                                elif len(listmap[node4]) < 2:
                                    continue
                                for node5 in listmap[node4]:
                                    if (node5 in listmap[host]) and (node5 not in [node1, node2, node3, host]):
                                        sixMRing = {host, node1,
                                                    node2, node3,
                                                    node4, node5}
                                        if sixMRing not in list6ring:
                                            list6pair.append([{host, node1},
                                                              {node1, node2},
                                                              {node2, node3},
                                                              {node3, node4},
                                                              {node4, node5},
                                                              {node5, host}])
                                            list6ring.append(sixMRing)
                                    else:
                                        continue
    return list6ring, list6pair


def cage_identification(data,filename,output,cutoff):
    listRing = []
    listUnion = []
    listNeighboring = []
    listStep = []
    listSets = []
    listStat = []
    wallTime = [0, 0, 0, 0, 0, 0]
    Frame=0

    for eachData in data:
        out=os.path.join(output, str(Frame)+'.txt')
        copyDB = checkPBC(eachData[0], eachData[2],cutoff)
        listn = search_neighbor(eachData[0], np.array(copyDB),cutoff)

        print('neighbor')
        listr6, listp6 = ring_identification(listn)
        print('done')


        listr6 = np.array(listr6)
        print(len(listr6))


        Results=[eachData[0][list(r)][:, 0, 0] for r in listr6]

        np.savetxt(out, Results, delimiter=' ',fmt='%d')





        Frame+=1

    print('\n')
    for each in wallTime:
        print(each)
    return  []
def is_suffix_lmp(suffix: str):
    if suffix == '.lammpstrj':
        return True
    return True
def mainfun(args, fn,output):
    filename = fn
    PATH = os.path.abspath((os.path.abspath(filename)))
    foldername = args.i
    DIR = os.path.dirname(PATH)
    name, suffix = os.path.splitext(PATH)

    CAGEStype = []
    cagetype_total = []

    listdata = []
    listUnion = []
    listRing = []
    listNeighboring = []
    listStep = []
    listSets = []
    listStat = []
    if is_suffix_lmp(suffix):
        os.system('clear')
        print(DIR + '/' + foldername + '/' + filename)
        datafile = open(DIR + '/' + foldername + '/' + filename, 'r')
        ending = datafile.seek(0, 2)
        datafile.seek(0, 0)
        print('Loading...')
        data=datafile.readlines()
        data=np.array(data)
        frame=np.sum(data == 'ITEM: NUMBER OF ATOMS\n')

        listdata=[]
        for f in range(frame):
            listatom = []
            start=np.where(data == 'ITEM: NUMBER OF ATOMS\n')[0] + 7
            title=data[start[f]-8]

            aaa = data[start[f]-6].strip('\n')
            aaa= aaa.split()
            natoms=int(aaa[0])
            atoms = data[start[f]:start[f]+natoms-1]
            (x1, x2)= data[start[f] - 4].split(maxsplit=2)
            (y1, y2) = data[start[f] - 3].split(maxsplit=2)
            (z1, z2)= data[start[f] - 2].split(maxsplit=2)
            LX = float(x2) - float(x1)
            LY = float(y2) - float(y1)
            LZ = (float(z2) - float(z1))
            title=title.split()[0]


            for atomstr in atoms:
                (aid, atype, ax, ay, az) = atomstr.split(maxsplit=4)
                if atype == args.t:
                    O = [float(aid), float(ax), float(ay), float(az)]
                    listatom.append([O])
            atomnum = len(listatom)
            print(title,atomnum)
            listdata.append([np.array(listatom),title , [LX, LY, LZ, x2, x1, y2, y1, z2, z1],atomnum ])





        print('Done!\n\n\n')



        cage_identification(np.array(listdata),name,output,args.c)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Notice:\n' + '\n 1.The code and the folder containing the trajectories to be analyzed should be in the same directory.\n' + ' 2.trajectories must be in lammpstrj format and contain only water molecules.')
    parser.add_argument('-i', type=str, default='1101', help="Path of folder containing the trjs to be analysed")
    parser.add_argument('-t', type=str, default='1', help="Symbol of Carbon")
    parser.add_argument('-c', type=float, default=2.0, help="Cutoff")

    args = parser.parse_args()


    foldername = args.i

    PROJECT_DIR_PATH = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
    DIR_PATH = os.path.join(PROJECT_DIR_PATH, foldername)
    files = os.listdir(DIR_PATH)
    ringslist=[]
    for filename in files:
        abs=os.path.abspath(args.i)


        upper=os.path.split(abs)[0]

        output=os.path.join(upper, os.path.splitext(filename)[0])
        try:
            os.mkdir(output)
        except FileExistsError:
            pass
        else:
            pass
        mainfun(args, filename,output)



