"""Lab 02.01"""
class ArrayStack:
    """arrystack"""
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """push"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop"""
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()
    def is_empty(self):
        """is_empty"""
        return True if self.data == [] else False
    def get_stack(self):
        """get_stack"""
        if self.data == []:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]
    def get_size(self):
        """get_size"""
        return self.size
    def print_stack(self):
        """print_stack"""
        for i, item in enumerate(self.data):
            print(item, end=", " if i < len(self.data) - 1 else "")
        print()
def distribute_students(group, num):
    """distribute_students"""
    group_list = [ArrayStack() for _ in range(group)]
    temp = ArrayStack()
    for _ in range(num):
        temp.push(input())
    for k in range(num):
        current_group = k % group
        group_list[current_group].push(temp.pop())
    return group_list
grop = int(input())
pos = int(input())
mas = distribute_students(grop, pos)
for l, stack in enumerate(mas):
    print("Group " + str(l+1) + ":", end=" ")
    stack.print_stack()