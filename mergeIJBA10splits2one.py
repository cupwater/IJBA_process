import cv2
import numpy as np

strList = []
prefix = '/home/cupwater/data/IJBA_process/IJB-A_1N_sets/split'
# merge 1N tasks 
for splitIndex in range(10):
    train_name = prefix + str(splitIndex+1) + '/search_gallery_' + str(splitIndex+1) + '.csv'
    print train_name
    lines = open(train_name)
    index = 0
    for line in lines:
        if(index == 0):  # drop the header line
            index = index+1
            continue
            
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        print s
        strList.append(s)
        
    
    train_name = prefix + str(splitIndex+1) + '/search_probe_' + str(splitIndex+1) + '.csv'
    lines = open(train_name)
    index = 0
    for line in lines:
        if(index == 0): # drop the header line
            index = index+1
            continue
            
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        strList.append(s)


prefix = '/home/cupwater/data/IJBA_process/IJB-A_11_sets/split'
# merge 11 tasks 
for splitIndex in range(10):
    train_name = prefix + str(splitIndex+1) + '/verify_metadata_' + str(splitIndex+1) + '.csv'
    lines = open(train_name)
    index = 0
    for line in lines:
        if(index == 0):  # drop the header line
            index = index+1
            continue
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        strList.append(s)
        


allImgPathList = list(set(strList))
allImgPathList.sort()
IJBAallOne = open('/home/cupwater/data/IJBA_process/IJBAallInOne.csv', 'w')
for i in range(len(allImgPathList)):
    print >> IJBAallOne, allImgPathList[i],
IJBAallOne.close()



prefix = '/home/cupwater/data/IJBA_process/IJB-A_1N_sets/split'
# find each split index in IJBAallInOne file
for splitIndex in range(10):
    train_name = prefix + str(splitIndex+1) + '/search_gallery_' + str(splitIndex+1) + '.csv'
    print train_name
    lines = open(train_name)
    index = 0
    posList = []
    for line in lines:
        if(index == 0):  # drop the header line
            index = index+1
            continue
            
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        pos = allImgPathList.index(s)
        posList.append(pos)
    posOut = open(prefix + str(splitIndex+1) + '/search_gallery_index_' + str(splitIndex+1) + '.txt', 'w')
    for i in range(len(posList)):
        print >> posOut, posList[i]
    posOut.close()
        
    
    train_name = prefix + str(splitIndex+1) + '/search_probe_' + str(splitIndex+1) + '.csv'
    lines = open(train_name)
    index = 0
    posList = []
    for line in lines:
        if(index == 0): # drop the header line
            index = index+1
            continue
            
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        pos = allImgPathList.index(s)
        posList.append(pos)
    posOut = open(prefix + str(splitIndex+1) + '/search_probe_index_' + str(splitIndex+1) + '.txt', 'w')
    for i in range(len(posList)):
        print >> posOut, posList[i]
    posOut.close()


prefix = '/home/cupwater/data/IJBA_process/IJB-A_11_sets/split'
# merge 11 tasks 
for splitIndex in range(10):
    train_name = prefix + str(splitIndex+1) + '/verify_metadata_' + str(splitIndex+1) + '.csv'
    lines = open(train_name)
    index = 0
    posList = []
    for line in lines:
        if(index == 0):  # drop the header line
            index = index+1
            continue
        tempStrs = line.split(',')
        s = tempStrs[0] + ',' + tempStrs[1] + ',' + tempStrs[2]
        for i in range(6,16):
            if tempStrs[i]:
                s = s + ',' + str(round(float(tempStrs[i]), 1))
            else :
                s = s + ','
        s = s + '\n'
        pos = allImgPathList.index(s)
        posList.append(pos)
    posOut = open(prefix + str(splitIndex+1) + '/verify_metadata_index_' + str(splitIndex+1) + '.txt', 'w')
    for i in range(len(posList)):
        print >> posOut, posList[i]
    posOut.close()
        