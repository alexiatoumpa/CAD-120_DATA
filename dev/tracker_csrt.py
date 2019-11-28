import __init__ as init
import cv2, os, re, sys, csv
from random import randint



for subject in os.listdir(init.DATASET_PATH):
    print("\nPress ESC key to skip to next video. Press Ctrl+C to exit.\n")
    for activity in os.listdir(init.DATASET_PATH+subject+'/'):
        for task in os.listdir(init.DATASET_PATH+subject+'/'+activity+'/'):

            PATH = init.DATASET_PATH+subject+'/'+activity+'/'+task+'/'
            lendir = len(os.listdir(PATH))/2
            print(PATH)

            RCNN_PATH = os.getcwd()[:-len('dev')]+'annotations_RAW/'+subject+'/'+\
              activity+'/'+task+'/'

            bboxes = []
            colors = []
            #re_init = False
            # Initialize multiTracker class
            multiTracker = cv2.MultiTracker_create()

            # Parse frames of video ...
            for frame in range(1,lendir+1):
                imgname = init.DATASET_PATH+subject+'/'+activity+'/'+task+\
                  '/RGB_'+str(frame)+'.png'
                img = cv2.imread(imgname)

                #with open(RCNN_PATH+'RCNN_'+str(frame)+'.csv') as csv_file:
                #    newlen = sum(1 for row in csv.reader(csv_file, delimiter=','))
                #print(newlen)
                #if frame != 1 and len(bboxes) < newlen:
                #    print('in here')
                #    re_init = True

                if frame == 1:# or re_init:
                    bboxes = []
                    colors = []
                    #re_init = False
                    with open(RCNN_PATH+'RCNN_'+str(frame)+'.csv') as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        for detections in csv_reader:
                            ulx, uly = float(detections[3]),float(detections[4])
                            lrx, lry = float(detections[5]),float(detections[6])
                            x, y = ulx, uly
                            w = abs(ulx-lrx)
                            h = abs(uly-lry)
                            bbox = (x,y,w,h)
                            bboxes.append(bbox)
                            colors.append((randint(0, 255), randint(0, 255), \
                              randint(0, 255)))

                    for b in bboxes:
                        success = multiTracker.add(cv2.TrackerCSRT_create(), img, b)

                    #for i in multiTracker.getObjects():
                    #    print(i)

                success, boxes = multiTracker.update(img)

                for i, newbox in enumerate(boxes):
                    p1 = (int(newbox[0]), int(newbox[1]))
                    p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
                    cv2.rectangle(img, p1, p2, colors[i],2,1)

                # Visualize
                cv2.imshow('CAD-120', img)
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break

