def vertexShader (vertex, **kwargs):
    
    modelmatrix = kwargs["modelmatrix"]
    
    vt = [vertex[0], 
          vertex[1],
          vertex[2],
          1]
    vt = modelmatrix @ vt
    
    vt = vt.tolist()[0]
    
    vt = [vt[0]/ vt[3],
          vt[1]/ vt[3],
          vt[2]/ vt[3]]
    return vt