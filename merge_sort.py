
def main():
    sorted_list = split_merge([1,3,4,7,3,5,6,7])
    
    print(sorted_list)

def split_merge(the_list):

    #the base case
    if len(the_list) < 2:
        return the_list

    middle = len(the_list)//2
    left = the_list[:middle]
    right = the_list[middle:]

    left = split_merge(left)
    right = split_merge(right)

    result = merge(left,right)

    return result
        


def merge(left,right):
    result = []
    left_pointer = 0
    right_pointer = 0
    
    #if the sum of the lengths are equal to the sum of the pointers
    while len(left) > left_pointer and len(right) > right_pointer:
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1

        else:
            result.append(right[right_pointer])
            right_pointer += 1


    #one pointer will always complete before the other one
    #so the rest of the list is added to the result
    if left_pointer == len(left):
        result.extend(right[right_pointer:len(right)])
    else:
        result.extend(left[left_pointer:len(left)])

    return result

main()
