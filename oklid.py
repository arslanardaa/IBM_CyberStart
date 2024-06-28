import math
points=[[(2,2),(5,5)],[(10,10),(1,1)],[(3,4),(5,5)]]

distances = []

def euclideanDistance(nokta):
    for i in nokta:
        distances.append(math.sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2))

       
euclideanDistance(points)     
            
    
