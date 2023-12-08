"""def"""
def convert(num):
    """tuple"""
    tmp = num.strip('()').split(', ')
    return tuple(map(float, tmp))
def swap(num):
    return num[::-1]
def main():
    var = (convert(input()))
    print(swap(var))
    
main()
