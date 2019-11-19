# Functions for parsing and transforming into the visualized image size the
# skeleton tracks and the objects for the CAD-120 dataset.

import os, re
import numpy as np

# Real World to Image projection of skeleton - parameters
# tan of FoV
krealX = 1.122133
krealY = 0.84176
# resolution of image in pixels
kResX = 640
kResY= 480
kCoeffX = kResX / krealX
kCoeffY = kResY / krealY


def readSkeletons(lines):

    # Initialize skeletal matrices
    P = np.zeros(((len(lines),15,1,3)))
    ORI = np.zeros(((len(lines),11,3,3)))
    P_CONF = np.zeros((len(lines),15))
    ORI_CONF = np.zeros((len(lines),11))

    # Parse each line of the file and save into ORI and P
    for line in lines[:-1]:
        #print(line)
        prsl = re.split(',', line)
        fr = int(prsl[0])-1 # index 0
    
        # HEAD
        j1ori0,j1ori1,j1ori2,j1ori3,j1ori4,j1ori5,j1ori6,j1ori7,j1ori8 = \
          float(prsl[1]),float(prsl[2]),float(prsl[3]),float(prsl[4]),\
          float(prsl[5]),float(prsl[6]),float(prsl[7]),float(prsl[8]),float(prsl[9])
        j1oriconf = int(prsl[10])
        j1px,j1py,j1pz = float(prsl[11]),float(prsl[12]),float(prsl[13])
        j1pconf = int(prsl[14])
        # NECK
        j2ori0,j2ori1,j2ori2,j2ori3,j2ori4,j2ori5,j2ori6,j2ori7,j2ori8 = \
          float(prsl[15]),float(prsl[16]),float(prsl[17]),float(prsl[18]),\
          float(prsl[19]),float(prsl[20]),float(prsl[21]),float(prsl[22]),float(prsl[23])
        j2oriconf = int(prsl[24])
        j2px,j2py,j2pz = float(prsl[25]),float(prsl[26]),float(prsl[27])
        j2pconf = int(prsl[28])
        # TORSO
        j3ori0,j3ori1,j3ori2,j3ori3,j3ori4,j3ori5,j3ori6,j3ori7,j3ori8 = \
          float(prsl[29]),float(prsl[30]),float(prsl[31]),float(prsl[32]),\
          float(prsl[33]),float(prsl[34]),float(prsl[35]),float(prsl[36]),float(prsl[37])
        j3oriconf = int(prsl[38])
        j3px,j3py,j3pz = float(prsl[39]),float(prsl[40]),float(prsl[41])
        j3pconf = int(prsl[42])
        # LEFT_SHOULDER
        j4ori0,j4ori1,j4ori2,j4ori3,j4ori4,j4ori5,j4ori6,j4ori7,j4ori8 = \
          float(prsl[43]),float(prsl[44]),float(prsl[45]),float(prsl[46]),\
          float(prsl[47]),float(prsl[48]),float(prsl[49]),float(prsl[50]),float(prsl[51])
        j4oriconf = int(prsl[52])
        j4px,j4py,j4pz = float(prsl[53]),float(prsl[54]),float(prsl[55])
        j4pconf = int(prsl[56])
        # LEFT_ELBOW
        j5ori0,j5ori1,j5ori2,j5ori3,j5ori4,j5ori5,j5ori6,j5ori7,j5ori8 = \
          float(prsl[57]),float(prsl[58]),float(prsl[59]),float(prsl[60]),\
          float(prsl[61]),float(prsl[62]),float(prsl[63]),float(prsl[64]),float(prsl[65])
        j5oriconf = int(prsl[66])
        j5px,j5py,j5pz = float(prsl[67]),float(prsl[68]),float(prsl[69])
        j5pconf = int(prsl[70])
        # RIGHT_SHOULDER
        j6ori0,j6ori1,j6ori2,j6ori3,j6ori4,j6ori5,j6ori6,j6ori7,j6ori8 = \
          float(prsl[71]),float(prsl[72]),float(prsl[73]),float(prsl[74]),\
          float(prsl[75]),float(prsl[76]),float(prsl[77]),float(prsl[78]),float(prsl[79])
        j6oriconf = int(prsl[80])
        j6px,j6py,j6pz = float(prsl[81]),float(prsl[82]),float(prsl[83])
        j6pconf = int(prsl[84])
        # RIGHT_ELBOW
        j7ori0,j7ori1,j7ori2,j7ori3,j7ori4,j7ori5,j7ori6,j7ori7,j7ori8 = \
          float(prsl[85]),float(prsl[86]),float(prsl[87]),float(prsl[88]),\
          float(prsl[89]),float(prsl[90]),float(prsl[91]),float(prsl[92]),float(prsl[93])
        j7oriconf = int(prsl[94])
        j7px,j7py,j7pz = float(prsl[95]),float(prsl[96]),float(prsl[97])
        j7pconf = int(prsl[98])
        # LEFT_HIP
        j8ori0,j8ori1,j8ori2,j8ori3,j8ori4,j8ori5,j8ori6,j8ori7,j8ori8 = \
          float(prsl[99]),float(prsl[100]),float(prsl[101]),float(prsl[102]),\
          float(prsl[103]),float(prsl[104]),float(prsl[105]),float(prsl[106]),\
          float(prsl[107])
        j8oriconf = int(prsl[108])
        j8px,j8py,j8pz = float(prsl[109]),float(prsl[110]),float(prsl[111])
        j8pconf = int(prsl[112])
        # LEFT_KNEE
        j9ori0,j9ori1,j9ori2,j9ori3,j9ori4,j9ori5,j9ori6,j9ori7,j9ori8 = \
          float(prsl[113]),float(prsl[114]),float(prsl[115]),float(prsl[116]),\
          float(prsl[117]),float(prsl[118]),float(prsl[119]),float(prsl[120]),\
          float(prsl[121])
        j9oriconf = int(prsl[122])
        j9px,j9py,j9pz = float(prsl[123]),float(prsl[124]),float(prsl[125])
        j9pconf = int(prsl[126])
        # RIGHT_HIP
        j10ori0,j10ori1,j10ori2,j10ori3,j10ori4,j10ori5,j10ori6,j10ori7,j10ori8 = \
          float(prsl[127]),float(prsl[128]),float(prsl[129]),float(prsl[130]),\
          float(prsl[131]),float(prsl[132]),float(prsl[133]),float(prsl[134]),\
          float(prsl[135])
        j10oriconf = int(prsl[136])
        j10px,j10py,j10pz = float(prsl[137]),float(prsl[138]),float(prsl[139])
        j10pconf = int(prsl[140])
        # RIGHT_KNEE
        j11ori0,j11ori1,j11ori2,j11ori3,j11ori4,j11ori5,j11ori6,j11ori7,j11ori8 = \
          float(prsl[141]),float(prsl[142]),float(prsl[143]),float(prsl[144]),\
          float(prsl[145]),float(prsl[146]),float(prsl[147]),float(prsl[148]),\
          float(prsl[149])
        j11oriconf = int(prsl[150])
        j11px,j11py,j11pz = float(prsl[151]),float(prsl[152]),float(prsl[153])
        j11pconf = int(prsl[154])
    
        # LEFT_HAND
        j12px,j12py,j12pz = float(prsl[155]),float(prsl[156]),float(prsl[157])
        j12pconf = int(prsl[158])
        # RIGHT_HAND
        j13px,j13py,j13pz = float(prsl[159]),float(prsl[160]),float(prsl[161])
        j13pconf = int(prsl[162])
        # LEFT_FOOT
        j14px,j14py,j14pz = float(prsl[163]),float(prsl[164]),float(prsl[165])
        j14pconf = int(prsl[166])
        # RIGHT_FOOT
        j15px,j15py,j15pz = float(prsl[167]),float(prsl[168]),float(prsl[169])
        j15pconf = int(prsl[170])
    
        # Save orientations and positions of joints into ORI and P matrices
        ORI[fr][0][0] = j1ori0,j1ori1,j1ori2
        ORI[fr][0][1] = j1ori3,j1ori4,j1ori5
        ORI[fr][0][2] = j1ori6,j1ori7,j1ori8
        ORI[fr][1][0] = j2ori0,j2ori1,j2ori2
        ORI[fr][1][1] = j2ori3,j2ori4,j2ori5
        ORI[fr][1][2] = j2ori6,j2ori7,j2ori8
        ORI[fr][2][0] = j3ori0,j3ori1,j3ori2
        ORI[fr][2][1] = j3ori3,j3ori4,j3ori5
        ORI[fr][2][2] = j3ori6,j3ori7,j3ori8
        ORI[fr][3][0] = j4ori0,j4ori1,j4ori2
        ORI[fr][3][1] = j4ori3,j4ori4,j4ori5
        ORI[fr][3][2] = j4ori6,j4ori7,j4ori8 
        ORI[fr][4][0] = j5ori0,j5ori1,j5ori2
        ORI[fr][4][1] = j5ori3,j5ori4,j5ori5
        ORI[fr][4][2] = j5ori6,j5ori7,j5ori8 
        ORI[fr][5][0] = j6ori0,j6ori1,j6ori2
        ORI[fr][5][1] = j6ori3,j6ori4,j6ori5
        ORI[fr][5][2] = j6ori6,j6ori7,j6ori8 
        ORI[fr][6][0] = j7ori0,j7ori1,j7ori2
        ORI[fr][6][1] = j7ori3,j7ori4,j7ori5
        ORI[fr][6][2] = j7ori6,j7ori7,j7ori8 
        ORI[fr][7][0] = j8ori0,j8ori1,j8ori2
        ORI[fr][7][1] = j8ori3,j8ori4,j8ori5
        ORI[fr][7][2] = j8ori6,j8ori7,j8ori8 
        ORI[fr][8][0] = j9ori0,j9ori1,j9ori2
        ORI[fr][8][1] = j9ori3,j9ori4,j9ori5
        ORI[fr][8][2] = j9ori6,j9ori7,j9ori8
        ORI[fr][9][0] = j10ori0,j10ori1,j10ori2
        ORI[fr][9][1] = j10ori3,j10ori4,j10ori5
        ORI[fr][9][2] = j10ori6,j10ori7,j10ori8 
        ORI[fr][10][0] = j11ori0,j11ori1,j11ori2
        ORI[fr][10][1] = j11ori3,j11ori4,j11ori5
        ORI[fr][10][2] = j11ori6,j11ori7,j11ori8
    
        P[fr][0] = j1px,j1py,j1pz     # HEAD
        P[fr][1] = j2px,j2py,j2pz     # NECK
        P[fr][2] = j3px,j3py,j3pz     # TORSO
        P[fr][3] = j4px,j4py,j4pz     # LEFT_SHOULDER
        P[fr][4] = j5px,j5py,j5pz     # LEFT_ELBOW
        P[fr][5] = j6px,j6py,j6pz     # RIGHT_SHOULDER
        P[fr][6] = j7px,j7py,j7pz     # RIGHT_ELBOW
        P[fr][7] = j8px,j8py,j8pz     # LEFT_HIP
        P[fr][8] = j9px,j9py,j9pz     # LEFT_KNEE
        P[fr][9] = j10px,j10py,j10pz  # RIGHT_HIP
        P[fr][10] = j11px,j11py,j11pz # RIGHT_KNEE
        P[fr][11] = j12px,j12py,j12pz # LEFT_HAND
        P[fr][12] = j13px,j13py,j13pz # RIGHT_HAND
        P[fr][13] = j14px,j14py,j14pz # LEFT_FOOT
        P[fr][14] = j15px,j15py,j15pz # RIGHT_FOOT
    
        ORI_CONF[fr][0], P_CONF[fr][0] = j1oriconf, j1pconf
        ORI_CONF[fr][1], P_CONF[fr][1] = j2oriconf, j2pconf
        ORI_CONF[fr][2], P_CONF[fr][2] = j3oriconf, j3pconf
        ORI_CONF[fr][3], P_CONF[fr][3] = j4oriconf, j4pconf
        ORI_CONF[fr][4], P_CONF[fr][4] = j5oriconf, j5pconf
        ORI_CONF[fr][5], P_CONF[fr][5] = j6oriconf, j6pconf
        ORI_CONF[fr][6], P_CONF[fr][6] = j7oriconf, j7pconf
        ORI_CONF[fr][7], P_CONF[fr][7] = j8oriconf, j8pconf
        ORI_CONF[fr][8], P_CONF[fr][8] = j9oriconf, j9pconf
        ORI_CONF[fr][9], P_CONF[fr][9] = j10oriconf, j10pconf
        ORI_CONF[fr][10], P_CONF[fr][10] = j11oriconf, j11pconf
    
        P_CONF[fr][11] = j12pconf
        P_CONF[fr][12] = j13pconf
        P_CONF[fr][13] = j14pconf
        P_CONF[fr][14] = j15pconf

    return P, ORI, P_CONF, ORI_CONF


# IMPORTANT
# Transformation needed on the skeletal data to be visualized on the image frame.
def TransformToFoV(x,y,z):
    xnew = int(kCoeffX*x/z + kResX/2)
    ynew = int(kResY/2 - kCoeffY*y/z)
    return xnew, ynew





