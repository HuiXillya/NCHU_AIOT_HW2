import cv2
import numpy as np
import json

cap = cv2.VideoCapture(r"C:\Users\Hui\Desktop\AIoT\v1.mp4")#名为'003.mp4'的文件
c=0
i=0
ret, frame = cap.read()
all_dl={}                            #文件名从0开始
while(ret):
    c=c+1
    if not c%24==0:
        continue
    l=[[],[],[],[]]
    frame=cv2.resize(frame,(23,17),interpolation=cv2.INTER_LINEAR)
    # print(frame.shape)
    for rows in frame[:8]:
        temp_l=[0,0,0,0]
        for i in range(5):
            temp_l[0]*=2
            if rows[i][0]<250:
                temp_l[0]+=1
        l[0].append(temp_l[0])
        for i in range(6,11):
            temp_l[1]*=2
            if rows[i][0]<250:
                temp_l[1]+=1
        l[1].append(temp_l[1])
        for i in range(12,17):
            temp_l[2]*=2
            if rows[i][0]<250:
                temp_l[2]+=1
        l[2].append(temp_l[2])
        for i in range(18,23):
            temp_l[3]*=2
            if rows[i][0]<250:
                temp_l[3]+=1
        l[3].append(temp_l[3])
    all_dl[str(c//4)+"u"]=l.copy()
    l=[[],[],[],[]]
    for rows in frame[9:]:
        temp_l=[0,0,0,0]
        for i in range(5):
            temp_l[0]*=2
            if rows[i][0]<250:
                temp_l[0]+=1
        l[0].append(temp_l[0])
        for i in range(6,11):
            temp_l[1]*=2
            if rows[i][0]<250:
                temp_l[1]+=1
        l[1].append(temp_l[1])
        for i in range(12,17):
            temp_l[2]*=2
            if rows[i][0]<250:
                temp_l[2]+=1
        l[2].append(temp_l[2])
        for i in range(18,23):
            temp_l[3]*=2
            if rows[i][0]<250:
                temp_l[3]+=1
        l[3].append(temp_l[3])
    all_dl[str(c//4)+"d"]=l.copy()
    # cv2.imwrite(r'C:\Users\Hui\Desktop\AIoT\image'+str(c) + '.jpg',frame) #存储为图像
    # break
    ret, frame = cap.read()
print(all_dl)
f=open(r"C:\Users\Hui\Desktop\AIoT\badapple.json","w")
f.write(json.dumps(all_dl))
f.close()
cap.release()
cv2.destroyAllWindows()