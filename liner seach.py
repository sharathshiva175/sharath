import matplotlib.pyplot as plt
import numpy as np
import time
start=time.time()
def liner(ar,n,k):
    for i in range(n):
        if ar[i]==k:
            return i
        return -1
arr=[]
n=int(input("enter the element"))
for i in range(n):
    arr.append(int(input("enter the element")))
print("the array element are",arr)
k=int(input("enter search key"))
res=liner(arr,len(arr),k)
if res == -1:
    print("invaild input")
else:
    print("the %d found at element "%k,res)
end=time.time()
print({end-start})
xpoints=np.array([500,1000,1500,2000,2500,5000])
ypoints=np.array([0.00009,0.00010,0.00011,0.00020,0.00203,0.09292])
plt.plot(xpoints,ypoints)
plt.show()
