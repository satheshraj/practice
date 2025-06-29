
def insertion_sort(input_array):
    for iteration in range(1,len(input_array)):
        first_element=input_array[iteration] # element present at index 1
        prev_element=iteration - 1
        while prev_element >= 0 and first_element < input_array[prev_element]:
            input_array[prev_element+1] =input_array[prev_element]
            prev_element -= 1
        input_array[prev_element+1]=first_element


input_array=[24,56,1,50,17]

insertion_sort(input_array)

print(input_array)
