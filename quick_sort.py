
""" implementation of quick sort with a pivot at the end """

def main():
    print(pivot_split([4,7,2,8,23,54,892,54,73,1,64,5,3,7]))

def pivot_split(the_list):
    result = []
    pivot_index = len(the_list)-1
    compare_pointer = 0

    #the base case of the function
    if len(the_list) < 1:
        return the_list
    else:
        while compare_pointer < pivot_index:
            if the_list[compare_pointer] >= the_list[pivot_index]:
                #reduce pivot by one
                pivot_index -= 1

                #pop item off list and stick it on the end
                tmp = the_list.pop(compare_pointer)
                the_list.append(tmp)

            else:
                #increase compare by one
                compare_pointer += 1

        #splits lists (leaving out the sorted item)
        left = split_list(the_list,pivot_index,True)
        right = split_list(the_list,pivot_index,False)

        #pivots then splits lists
        left = pivot_split(left)
        right = pivot_split(right)

        #recombines list and returns result
        result.extend(left)
        result.append(the_list[pivot_index])
        result.extend(right)

    return result



def split_list(the_list,pivot_index,is_left):
    if is_left:
        the_list = the_list[:pivot_index]
    else:
        the_list = the_list[pivot_index+1:]

    return the_list


main()
