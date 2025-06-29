
def selSort(input_array,array_length):
    for iteration in range(array_length):
        minimum_value=iteration # first value is expected to be minimum
        for iter_inner_loop in range(iteration+1 ,array_length ):
            if input_array[iter_inner_loop] < input_array[minimum_value]:  #Comparing minimum with the next element
                minimum_value=iter_inner_loop
        (input_array[iteration],input_array[minimum_value]) =(input_array[minimum_value],input_array[iteration]) # Swap if required


input_array=[34,23,1,67,4]
array_length=len(input_array)
selSort(input_array,array_length)
print(input_array)