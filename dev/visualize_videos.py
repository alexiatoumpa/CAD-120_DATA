import __init__ as init
from cad_tracks import readSkeletons
import cv2, os,re

for subject in os.listdir(init.DATASET_PATH):
    print("Press ESC key to skip to next video. Press Ctrl+C to exit.")
    for activity in os.listdir(init.DATASET_PATH+subject+'/'):
        for task in os.listdir(init.DATASET_PATH+subject+'/'+activity+'/'):

            PATH = init.DATASET_PATH+subject+'/'+activity+'/'+task+'/'
            lendir = len(os.listdir(PATH))/2
            print(PATH)
            # Compute total number of objects in the video
            object_num = sum(1 for i in os.listdir(init.ANNOTATION_PATH+\
              subject[:9]+'annotations/'+activity+'/') if (task in i) and \
              ('obj' in i) )

            # Skeletal information
            file = open(init.ANNOTATION_PATH+subject[:9]+'annotations/'+\
              activity+'/'+task+'.txt')
            skeletal_lines = file.readlines()
            P, ORI,_,_ =readSkeletons(skeletal_lines)

            # Parse frames of video ...
            for frame in range(1,lendir):
                imgname = init.DATASET_PATH+subject+'/'+activity+'/'+task+\
                  '/RGB_'+str(frame)+'.png'
                img = cv2.imread(imgname)

                # For every object in the video ...
                for o in range(object_num):
                    file = open(init.ANNOTATION_PATH+subject[:9]+'annotations/'+\
                      activity+'/'+task+'_obj'+str(o+1)+'.txt', 'r')
                    lines = file.readlines()
                    line = lines[frame]
                    coordinates = re.split(',', line)
                    ulx, uly = float(coordinates[2]), float(coordinates[3])
                    lrx, lry = float(coordinates[4]), float(coordinates[5])
                    cv2.line(img,(int(ulx),int(uly)),(int(lrx),int(uly)),\
                      (255,255,255),4)
                    cv2.line(img,(int(ulx),int(uly)),(int(ulx),int(lry)),\
                      (255,255,255),4)
                    cv2.line(img,(int(lrx),int(lry)),(int(lrx),int(uly)),\
                      (255,255,255),4)
                    cv2.line(img,(int(lrx),int(lry)),(int(ulx),int(lry)),\
                      (255,255,255),4)

                # Visualize
                cv2.imshow('CAD-120', img)
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break

