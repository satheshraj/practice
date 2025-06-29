
def shellSort(input_array, array_length):
    gap=array_length//2    # dividing the number of elements by 2 to find the gap 
    while gap>0:
        for iteration in range(gap,array_length):
            temp1=input_array[iteration]
            temp_index=iteration
            while temp_index >= gap and input_array[temp_index - gap] > temp1:
                input_array[temp_index]= input_array[temp_index-gap]
                temp_index-=gap
            input_array[temp_index]=temp1
        gap//=2

input_array=[23,12,1,17,45,2,13]
length=len(input_array)
shellSort(input_array, array_length)
print(input_array)


