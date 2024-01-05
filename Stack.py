"""Stack Lab02-01"""
class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """stack"""
        self.data.append(input_data)
        self.size += 1
    def pop(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        elif self.size > 0:
            self.size -= 1
            return self.data.pop()
    def is_empty(self):
        if self.size == 0:
            return True
        else: 
            return False
    def get_stack_top(self):
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else: 
            return self.size
    def get_size(self):
        return self.size
    def print_stack(self):
        print(self.data)

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())
    
print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)