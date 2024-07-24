from obj import Obj
from Mathlib import *
from Modulo_matematico import *
class Model(object):
    def __init__(self, filename):
        objFile = Obj(filename)
        
        self.vertices = objFile.vertices
        self.faces = objFile.faces
        
        
        self.translate = [0,0,0]
        self.rotate = [0,0,0]
        self.scale = [1,1,1] 
        
        
    def GetModelmatrix(self):
        translatemat = traslationmatrix(self.translate[0],
                                        self.translate[1],
                                        self.translate[2])
        rotateMat = Rotationmatrix(self.rotate[0],
                                   self.rotate[1],
                                   self.rotate[2])
        
        ScaleMat = Scalematrix(self.scale[0],
                               self.scale[1],
                               self.scale[2])
        
        roll1 = mult_matrx(translatemat, rotateMat)
        roll2 = mult_matrx(roll1, ScaleMat)
        
        return roll2
        