import Modulo_matematico as np
from math import pi, sin, cos
def traslationmatrix(x, y, z):
    
    tMat = np.matrix2([[1,0,0,x],
                      [0,1,0,y],
                      [0,0,1,z],
                      [0,0,0,1]])
    return tMat


def Scalematrix(x, y, z):
    
    tMat = np.matrix1([[x,0,0,0],
                      [0,y,0,0],
                      [0,0,z,0],
                      [0,0,0,1]])

def Rotationmatrix(pitch, yaw, roll):
    
    pitch *= pi/180
    yaw *= pi/180
    roll *= pi/180
    
    pitchMat = np.matrix2([[1,0,0,0],
                          [0,cos(pitch),-sin(pitch),0],
                          [0,sin(pitch),cos(pitch),0],
                          [0,0,0,1]])
    yawmat = np.matrix2([[cos(yaw), 0, sin(yaw), 0],
                         [0, 1, 0, 0],
                         [-sin(yaw), 0, cos(yaw), 0],
                         [0, 0, 0, 1]])
    
    rollMat = np.matrix2([[cos(roll),-sin(roll),0,0],
                        [sin(roll),cos(roll),0,0],
                        [0,0,1,0],
                        [0,0,0,1]])
    
    pass1 = np.mult_matrx(pitchMat, yawmat)
    total = np.mult_matrx(pass1, rollMat)
    return total