NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def check_mul_string(string, i):
    if i > len(string) - 5:
        return 0
    if string[i] + string[i + 1] + string[i + 2] + string[i + 3] == 'mul(':
        j = i + 4

        start_of_num1 = j
        while string[j] in NUM_LIST:
            j += 1
        if string[j] != ',':
            print('Failed: No comma')
            return 0
        end_of_num1 = j

        if j > len(string) - 1:
            print('Failed: Not enough numbers')
            return 0
        j += 1
        start_of_num2 = j
        while string[j] in NUM_LIST:
            j += 1
        if string[j] != ')':
            print(string[j])
            print("Failed: No closed bracket")
            return 0
        end_of_num2 = j

        print(int(string[start_of_num1:end_of_num1]), int(string[start_of_num2:end_of_num2]))
        print(int(string[start_of_num1:end_of_num1]) * int(string[start_of_num2:end_of_num2]))
        return int(string[start_of_num1:end_of_num1]) * int(string[start_of_num2:end_of_num2])
    return 0

f = open("../Inputs/day3_input.txt", "r")
massive_text_string = f.read()
f.close()

without_spaces = massive_text_string.replace(' ', '')

totals = 0

# This is not going to be efficient...
# After finishing, I think it's quite efficient :)
for i in range(len(without_spaces)):
    if without_spaces[i] == 'm':
        totals += check_mul_string(without_spaces, i)

print(totals)