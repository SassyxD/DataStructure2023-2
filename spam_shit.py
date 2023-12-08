"""main"""
import json
def m1nimum(my_list):
  """help"""
  current_m1n = my_list[0]
  for num in my_list:
    if num < current_m1n:
      current_m1n = num
  return current_m1n

def m4ximum(my_list):
  """help"""
  current_m4x = my_list[0]
  for num in my_list:
    if num > current_m4x:
      current_m4x = num
  return current_m4x

def avg(my_list):
    """help"""
    return sum(my_list)/len(my_list)

def main():
    """help"""
    my_list = json.loads(input())
    fi_m4x = round(m4ximum(my_list), 2)
    fi_m1n = round(m1nimum(my_list), 2)
    fi_avg = round(avg(my_list), 2)
    final_tuple = (fi_m4x, fi_m1n, fi_avg)
    print(final_tuple)
main()
