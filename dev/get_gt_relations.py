import __init__ as init
from cad_tracks import readSkeletons
import cv2, os, re, csv, itertools, sys


save_relations = True
default_paths = False

if default_paths:
    subject_paths = os.listdir(init.DATASET_PATH)
else:
    subject_paths = ['Subject3_rgbd_images']
    activity_paths = ['stacking_objects']
    task_paths = ['1204175451']

frame_start = 1 if len(sys.argv)==1 else int(sys.argv[1]) # default : 1


for subject in subject_paths:
    print("Press ESC key to skip to next video. Press Ctrl+C to exit.")
    for activity in os.listdir(init.DATASET_PATH+subject+'/') if \
      default_paths else activity_paths:
        for task in os.listdir(init.DATASET_PATH+subject+'/'+activity+\
          '/') if default_paths else task_paths:

            PATH = init.DATASET_PATH+subject+'/'+activity+'/'+task+'/'
            print(PATH)
            lendir = len(os.listdir(PATH))/2
            
            # Compute total number of objects in the video
            object_num = sum(1 for i in os.listdir(init.ANNOTATION_PATH+\
              subject[:9]+'annotations/'+activity+'/') if (task in i) and \
              ('obj' in i) )

            # Save relations in file
            filename = os.getcwd()[:-len('dev')]+'groundtruth_relations/'+\
              subject[:8]+'-'+activity+'-'+task + '.csv'

            pairwise = list(itertools.combinations(range(1,object_num),2))
            interactions = []
            for p in pairwise:
                interactions.append([p[0],p[1]])
            # write first line of task file
            if frame_start == 1:
                with open(filename, mode='a') as csvfile:
                    datawrite = csv.writer(csvfile, delimiter=';', quotechar='"', \
                      quoting=csv.QUOTE_MINIMAL)
                    datawrite.writerow(['frame', interactions])


            # Skeletal information
            file = open(init.ANNOTATION_PATH+subject[:9]+'annotations/'+\
              activity+'/'+task+'.txt')
            skeletal_lines = file.readlines()
            P, ORI,_,_ =readSkeletons(skeletal_lines)

            # Parse frames of video ...
            for frame in range(frame_start,lendir+1):
                print(frame)
                imgname = init.DATASET_PATH+subject+'/'+activity+'/'+task+\
                  '/RGB_'+str(frame)+'.png'
                img = cv2.imread(imgname)

                # For every object in the video ...
                for o in range(object_num-1): # -1 for excluding the table bounding box
                    file = open(init.ANNOTATION_PATH+subject[:9]+'annotations/'+\
                      activity+'/'+task+'_obj'+str(o+1)+'.txt', 'r')
                    lines = file.readlines()
                    line = lines[frame-1]
                    coordinates = re.split(',', line)
                    ulx, uly = float(coordinates[2]), float(coordinates[3])
                    lrx, lry = float(coordinates[4]), float(coordinates[5])
                    #cv2.line(img,(int(ulx),int(uly)),(int(lrx),int(uly)),\
                    #  (255,255,255),4)
                    #cv2.line(img,(int(ulx),int(uly)),(int(ulx),int(lry)),\
                    #  (255,255,255),4)
                    #cv2.line(img,(int(lrx),int(lry)),(int(lrx),int(uly)),\
                    #  (255,255,255),4)
                    #cv2.line(img,(int(lrx),int(lry)),(int(ulx),int(lry)),\
                    #  (255,255,255),4)
                    b_center_x = int(min(ulx,lrx) + abs(lrx-ulx)/2)
                    b_center_y = int(min(uly,lry) + abs(lry-uly)/2)
                    nametext = str(o+1) #'obj_' + str(o+1)
                    cv2.putText(img, nametext, (b_center_x, b_center_y),\
                      cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,150,30), 2, cv2.LINE_AA)
                # Visualize
                cv2.imshow('CAD-120', img)
                k = cv2.waitKey(30) & 0xff

                # Capture pair-wise object relations (w/o table interactions)
                pairwise = list(itertools.combinations(range(1,object_num),2))
                all_relations = []
                for p in pairwise:
                    o1, o2 = p[0], p[1]
                    relation = input("Relation for (%s, %s): " % (str(o1), str(o2)))
                    all_relations.append(relation)
                    #print(relation)
                with open(filename, mode='a') as csvfile:
                    writedata = csv.writer(csvfile, delimiter = ';', quotechar = '"', \
                      quoting=csv.QUOTE_MINIMAL)
                    writedata.writerow([frame, all_relations])
                #while (k!=27):
                #    k = cv2.waitKey(30) & 0xff
                #    if k==27:
                #        break
        frame_start = 1

