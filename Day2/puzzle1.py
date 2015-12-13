file = open('input.txt','r')
area=0
for line in file:
    dimensions = line.split('x')
    i= 0
    for dimension in dimensions:
        dimensions[i]=float(dimension.rstrip('\n'))
        i +=1
    area1 = 2*dimensions[0]*dimensions[1]
    area2 = 2*dimensions[0]*dimensions[2]  
    area3 = 2*dimensions[1]*dimensions[2]
    area += area1+area2+area3+min(area1,area2,area3)/2
print(area)
