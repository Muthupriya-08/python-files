import numpy as smp
"""arr=smp.array([1,2,3,4])
dup=arr.copy()
print(arr,dup)"""

a=smp.array([1,2,3,4])
d1=a.copy()
d2=a.view()
print(a,d1,d2)

