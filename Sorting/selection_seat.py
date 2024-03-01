"""selectionSort"""
import json
def selectionsort(list_up, last_index):
    '''sorting'''
    list_main = json.loads(list_up)
    compare_time = 0
    for i in range(last_index + 1):
        current__mini = list_main[i]
        for j in range(i + 1, last_index + 1):
            if list_main[j][0] == current__mini[0]:
                if int(list_main[j][1:]) < int(current__mini[1:]):
                    current__mini = list_main[j]
                    compare_time += 1
                else:
                    compare_time += 1
            elif ord(list_main[j][0]) < ord(current__mini[0]):
                current__mini = list_main[j]
                compare_time += 1
            else:
                compare_time += 1
        list_main[list_main.index(current__mini)], list_main[i] = \
            list_main[i], list_main[list_main.index(current__mini)]
        if i != last_index:
            print(list_main)
    print("Comparison times: %i" % compare_time)
selectionsort(input(), int(input()))