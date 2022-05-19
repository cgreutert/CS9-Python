def bubbleSort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
list1 = [1, 10, 3, 7, 9, 5]
bubbleSort(list1)
print(list1)
