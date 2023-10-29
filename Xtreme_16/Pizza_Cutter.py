numberOfLines = int(input())
degrees = []
angles = []
for i in range(numberOfLines):
    degrees = input().split()
    noOfAngles = degrees[0]
    #print("hello")
    degrees.remove(degrees[0])
    for i in range(len(degrees)):
        if int(degrees[i]) < 0:
            degrees[i] = str(int(degrees[i]) + 180);
        
    
    [angles.append(x) for x in degrees if x not in angles]
    angles.sort()
    degrees = []
    [degrees.append(x) for x in angles if str(((abs(int(x)) + 180)%360)) not in degrees]
    #print(degrees)
    
    if len(degrees) == 0:
        print(1)
    else:
        print(len(degrees) * 2)
    angles = []