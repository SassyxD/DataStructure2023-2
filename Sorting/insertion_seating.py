"""insertionSort"""
import json
 
def insertion(list_raw, last_index):
    '''insert'''
    list_load = json.loads(list_raw)
    compare_time = 0
    for i in range(last_index + 1):
        if i == 0:
            pass
        else:
            kept = list_load[i]
            insert_loc = None
            for j in range(i-1, -1, -1):
                compare_time += 1
                if kept[0] == list_load[j][0]:
                    if int(kept[1:]) < int(list_load[j][1:]):
                        insert_loc = j
                    else:
                        break
                elif kept < list_load[j]:
                    insert_loc = j
                else:
                    break
            if insert_loc != None:
                list_load.pop(i)
                list_load.insert(insert_loc, kept)
        if i == 0:
            pass
        else:
            print(list_load)
    print("Comparison times: %i" % compare_time)
insertion(input(), int(input()))