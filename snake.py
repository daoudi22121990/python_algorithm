import numpy as np
#https://www.geeksforgeeks.org/algorithms-gq/recursion-gq/
def buubleSort(arr):
    swap=True
    
    while swap:
        i=0
        
        swap=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swap=True
          
            
        i+=1
        print(arr)
li=[3,8,9,75,108,2,106,105,140,1,2,8,7,42,5,2,9,4,5,1,15,13]

def selctionsort(arr):
    
    for j in range(len(arr)):
        indexmin=j
        temp=arr[j]
        for i in range(j,len(arr)):
            
            if temp>arr[i]:
                temp=arr[i]
                indexmin=i
        
        swap=arr[j]
        arr[j]=arr[indexmin]
        arr[indexmin]=swap
        
    print(arr)    
        
def isertsort(arr):
    for i in range(1,len(arr)):
        k=arr[i]
        j=i-1
        while j>=0 and arr[j]>k:

            temp=arr[j]
            arr[j]=k
            arr[j+1]=temp
            j-=1    
    print(arr)
def fib(n):
    if n<=1:
        
        return 1
        
    else:
        
        return fib(n-2)+fib(n-1)
lih=[19,24,60,70,4,4,5,70,80,91,96,88]    

def merr(lis,s,e,m):
    
    
    
    poin_1=0
    poin_2=0
    lis_1=lis[s:m+1]
    lis_2=lis[m+1:e+1]
   
   
   
    
    index=s
   
    while poin_1<m+1-s and poin_2<e-m:
       
        if lis_1[poin_1]>lis_2[poin_2]:
            lis[index]=lis_1[poin_1]
            poin_1+=1
            index+=1
        elif lis_1[poin_1]==lis_2[poin_2]:
            lis[index]=lis_1[poin_1]
            lis[index+1]=lis_2[poin_2]
            poin_1+=1
            poin_2+=1
            index+=2
            
            
            
            
        else:
            lis[index]=lis_2[poin_2]
            poin_2+=1
            
            index+=1
   
        
    if poin_1==m+1:
        rest_list=lis_2[poin_2:]
        x=e+1-len(rest_list)
        
        for i in range(len(rest_list)):
            lis[index]=rest_list[i]
            x+=1
            index+=1
            
        
        
       
        
    else:
        rest_list=lis_1[poin_1:]
        x=e+1-len(rest_list)
        for i in range(len(rest_list)):
            lis[index]=rest_list[i]
            x+=1
            index+=1
        
      
    
def mer(arr_1,arr_2,arr):
    
    i=0
    j=0
    index=0
    while i <len(arr_1) and j<len(arr_2):
        if arr_1[i]<arr_2[j]:
            arr[index]=arr_1[i]
            i+=1
            index+=1
        elif arr_1[i]>arr_2[j]:
            arr[index]=arr_2[j]
            j+=1
            index+=1
        else:
            arr[index]=arr_1[i]
            arr[index]=arr_2[j]
            j+=1
            i+=1
            index+=2
            
    if i==len(arr_1):
        arr[index:]=arr_2[j:]
    else:
        arr[index:]=arr_1[i:]
       
    
def ME(arr):
    if len(arr)>1:
        m=int(len(arr)/2)
        left=arr[0:m]
        right=arr[m:len(arr)]
        ME(left)
        ME(right)
        mer(left,right,arr)
def merge(arr,s,e):
    if e>s:
        m=int(s+((e-s)/2))
       
        merge(arr,s,m)
        merge(arr,m+1,e)
        merr(arr,s,e,m)
        

lis=[19,24,60,70,4,4,5,70,80,91,96,88]
lip=[9,6,3,1,0,7,5,4,2,99]
merge(lis,0,11)
lis=[19,24,60,4,4,5,70,80,91,96,88]
def qui(arr,s,e):
    i=-1
    valuechosse=int((e-s)/2)+s
    num=arr[valuechosse]
    for j in range(len(arr)):
        if arr[j]<num:
           i+=1
           te=arr[i]
           arr[i]=arr[j]
           arr[j]=te
           
          
    i+=1
    index=0
    for g in range (len(arr)):
        if arr[g]==num:
            index=g
            break
            
    if arr[i]!=num:
        sub=arr[i]
        arr[i]=num
        arr[index]=sub
    print(arr)    
    return i
    

def quick(arr,s,e):
    if e>s:
        pivot=qui(arr,s,e)
        quick(arr,s,pivot-1)
        quick(arr,pivot+1,e)
    


def mini_coin(n,ls):
    c=0
    c= int(n/ls[0])
    ls[0]=(ls[0],c)
    n=n%ls[0][0]
    
    c=int(n/ls[1])
    ls[1]=(ls[1],c)
    n=n%ls[1][0]

    c=int(n/ls[2])
    ls[2]=(ls[2],c)
    n=n%ls[2][0]

    c=int(n/ls[3])
    ls[3]=(ls[3],c)
    n=n%ls[3][0]

    print(ls)
#fibonashi seires dynamic algorithm
arr=[0]*10

def fib(n):
    print("hi")
    if n==1 or n==2:
        arr[n]=1
        return 1
    if arr[n]==0:
        arr[n]=fib(n-1)+fib(n-2)
        
    return arr[n]
#0 or 1 knapsack proplem:
w=[1,2,3]
v=[60,100,120]
c=5
k=np.zeros((len(w)+1,c+1))
for i in range(len(w)+1):
    for j in range(c+1):
        if i==0 or j==0:
            k[i][j]=0
        else:
            if w[i-1]<=j:
                k[i][j]=max(v[i-1]+k[i-1][j-w[i-1]],k[i-1][j])
            else:
                k[i][j]=k[i-1][j]
print(k[len(w)][c])                
                
         
            
 
    






