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

f = open("day1_input.txt", "r")
double_array = f.readlines()
f.close()

left_list, right_list = [], []

for row in double_array:
    left_list += [row.strip().split()[0]]
    right_list += [row.strip().split()[1]]

sorted_left_list = merge_sort(left_list)
sorted_right_list = merge_sort(right_list)

# total_sum = 0
# for i in range(len(sorted_left_list)):
#     total_sum += abs(int(sorted_left_list[i]) - int(sorted_right_list[i]))

# print(total_sum)

similarity_score = 0
checked_list = []
for number in sorted_left_list:
    if number not in checked_list:
        similarity_score += int(number) * (sorted_right_list.count(number))
        checked_list += [number]

print(similarity_score)