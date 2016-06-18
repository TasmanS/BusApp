##This is a problem from Uber and Codefights
## GIven two sets of X,Y coordinates in a city, with float numbers, find the shortest distance,
## whole values (non floats, though repped as floats) are the only way to move

# to solve:
##research recursive movement evaulator - recitation #10 has example
## Find multiple paths to destinatin, store, find lowest path, return lowest path

def perfectCity(departure, destination):
    
    depX=float(departure[0])
    depY=float(departure[1])

    desX=float(destination[0])
    desY=float(destination[1])

    remainDepX=depX%1
    remainDepY=depY%1
    
    remainDesX=desX%1
    remainDesY=desY%1

    first=0.0
    second=0.0
    third=0.0
    
    if remainDepX==0 and remainDepY!=0:

        if desY>depY:
            first=1-depY
                   
        elif desY<depY:
            first=-depY

        second=desX-depX
        
        third=desY-(depY+first)

        return abs(first)+abs(second)+abs(third)
        
    if remainDepX!=0 and remainDepY==0:
        
        ## doesn't account for opposite
        ## something wrong with decision making in this sub -tree
        ## makes inefficent choices. Maybe store multiple values?
        if desX<depX and desX+depX>1:
            first=1-depX
        if desX<depX and desX+depX<1:
            first=-depX

        second=desY-depY
        
        third=desX-(depX+first)

        return abs(first)+abs(second)+abs(third)
        
        
    
print(perfectCity([1,1.1],[2,2.1]))
                    
