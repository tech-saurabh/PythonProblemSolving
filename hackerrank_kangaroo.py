import math
import os
import random
import re
import sys
def kangaroo(x1, v1, x2, v2):
        a=x1+v1
        b=x2+v2
        sum1=v1
        sum2=v2
        while(((1<=v1<=1000) and (1<=v2<=1000)) and (0<=x1<x2<=1000)):
                if((a+sum1)==(b+sum2)):
                    return("YES")
                    exit(0)
                sum1+=sum1
                sum2+=sum2
                x1+=1
                x2+=1
                v1+=1
                v2+=1
        return("NO")


x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
