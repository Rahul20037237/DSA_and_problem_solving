def bubbblesort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    print(array) 
if __name__=="__main__":
    array=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubbblesort(array)
