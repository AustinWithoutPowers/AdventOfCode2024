def merge_sort(unmerged_list):
    mid_index = len(unmerged_list) // 2
    if mid_index < 1:
        return unmerged_list
    else:
        left_half = merge_sort(unmerged_list[:mid_index])
        right_half = merge_sort(unmerged_list[mid_index:])

        sorted_list = []
        for i in range(len(unmerged_list)):
            if len(left_half) < 1:
                sorted_list += right_half
                break
            if len(right_half) < 1:
                sorted_list += left_half
                break
            if left_half[0] <= right_half[0]:
                sorted_list += [left_half.pop(0)] # I KNOW THIS ISN'T EFFICIENT
            else:
                sorted_list += [right_half.pop(0)]
        
        return sorted_list