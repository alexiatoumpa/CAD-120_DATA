import __init__ as init
import cv2, os

for subject in os.listdir(init.DATASET_PATH):
    for activity in os.listdir(init.DATASET_PATH+subject+'/'):
        for task in os.listdir(init.DATASET_PATH+subject+'/'+activity+'/'):
            lendir = len(os.listdir(init.DATASET_PATH+subject+'/'+activity+'/'+task+'/'))/2
            for frame in range(1,lendir+1):
                imgname = init.DATASET_PATH+subject+'/'+activity+'/'+task+'/RGB_'+str(frame)+'.png'
                img = cv2.imread(imgname)
                cv2.imshow('CAD-120', img)
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break

