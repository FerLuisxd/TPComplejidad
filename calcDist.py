
from math import sin, cos, sqrt, atan2, radians




def calcularDistancia(x1,y1,x2,y2):        
    R = 6373.0  # approximate radius of earth in km
    lat1 = radians(y1) #y1
    lon1 = radians(x1) #x1
    lat2 = radians(y2)  #y2
    lon2 = radians(x2) #x2  
    dlon = lon2 - lon1 #Distancia entre longitudes
    dlat = lat2 - lat1 #Distancia entre latitudes   
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = R * c
    return distance