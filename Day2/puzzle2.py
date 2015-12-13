file = open('input.txt','r')
totallength=0
for line in file:
    dimensions = line.split('x')
    i= 0
    for dimension in dimensions:
        dimensions[i]=float(dimension.rstrip('\n'))
        i +=1
    dimensions=sorted(dimensions)
    length1 = dimensions[0]  
    length2 = dimensions[1]
    volume  = dimensions[0]*dimensions[1]*dimensions[2]
    totallength += 2*length1+2*length2+volume
print(totallength)
