"""bubbleSort"""
import json
def bubblesort(list_up, last_index):
    '''sorting'''
    list_main = json.loads(list_up)
    compare_time = 0
    already_sorted = False
    for i in range(last_index + 1):
        if already_sorted == False:
            already_sorted = True
            for j in range(last_index, i, -1):
                if list_main[j] < list_main[j - 1] and j != 0:
                    list_main[j], list_main[j-1] = list_main[j-1], list_main[j]
                    compare_time += 1
                    already_sorted = False
                else:
                    compare_time += 1
        if already_sorted == True:
            pass
        else:
            print(list_main)
    print(list_main)
    print("Comparison times: %i" % compare_time)
bubblesort(input(), int(input()))