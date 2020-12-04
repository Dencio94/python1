import copy
import random

row=random.randint(10,20)
col=random.randint(10,20)

image=[]
tmp=[]
for i in range(row):
    tmp=[]
    for k in range(col):
        tmp.append(0)
    image.append(tmp)

for i in range(row):
    for k in range(col):
        image[i][k]=random.randint(0,255)



