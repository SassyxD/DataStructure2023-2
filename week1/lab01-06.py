'''Lab 01.06 - Elevator'''
class Elevator:
    '''Lab 01.06'''
    def __init__(self, max_floor):
        '''Lab 01.06'''
        self.current_floor = 1
        self.max_floor = max_floor
  
    def go_to_floor(self, floor):
        '''Lab 01.06'''
        self.current_floor = floor
  
    def report_current_floor(self):
        '''Lab 01.06'''
        print(self.current_floor)
  
def start():
    '''Lab 01.06'''
    limit = int(input())
    get = Elevator(limit)
  
    while True:
        text = input()
        if text == 'Done':
            get.report_current_floor()
            break
        else:
            text = int(text)
        if text > limit:
            print("Invalid Floor!")
        else:
            get.go_to_floor(text)
  
start()