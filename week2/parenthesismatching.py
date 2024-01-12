"""Lab 02.04"""
class ArrayStack:
    '''ArrayStack'''
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
    def get_stack_top(self):
        """get_stack_top"""
        if self.data == []:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]
  
    def get_size(self):
        """get_size"""
        return self.size
    def print_stack(self):
        """print_stack"""
        print(self.data)
  
def is_parentheses_matching(expr):
    """is_parentheses_matching"""
    stack = ArrayStack()
    check = True
    parentheses_mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                check = False
            top_element = stack.pop()
            if parentheses_mapping[char] != top_element:
                check = False
    if not stack.is_empty():
        return False
    return check
  
exp = input()
res = is_parentheses_matching(exp)
  
if res:
    print("Parentheses in", exp, "are matched")
else:
    print("Parentheses in", exp, "are unmatched")
print(res)