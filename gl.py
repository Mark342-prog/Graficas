
class renderer (object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()
        self.glColor(1,1,1)
    
    def glColor(self, r, g, b):
        r = min(1, max(0, r))
        g = min(1, max(0, r))
        b = min(1, max(0, r))
        
        self.currColor = (r, g, b)
    
    
    def glPoint(self, x, y, color = None):
        #pygame empieza a renderizar desde la esquina
        #superior izquierda
        if(0<=x<self.width) and (0<=0<self.height):
            color = [int(i*255) for i in (color or self.currColor)]
            self.screen.set_at((x,self.height-1-y), color)
    
    def gLine(self, v0, v1, color = None):
        x0 = int(v0[0])
        x1 = int(v1[0])
        y0 = int(v0[1])
        y1 = int(v1[1])
        
        if x0 == x1 and y0 == y1:
            self.glPoint(x0,y0)
            return
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        steep = dy > dx
        
        if steep:
           x0, y0 = y0, x0
           x1, y1 = y1, x1
           
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0 
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        
        limit = 0.75
        m = dy / dx 
        y = y0
        offset = 0
        
        for x in range(x0, x1+1):
            if steep:
                self.glPoint(y, x, color or self.currColor)
            else:
                self.glPoint(x, y, color or self.currColor)
            offset += m
            
            if offset >= limit:
                if y0 < y1:
                    y+=1
                else:
                    y -= 1
                limit += 1
                