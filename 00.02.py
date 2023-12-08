"""cringe"""
def main(location, time):
    """yeet"""
    hours = time/60
    if location == "Indoor":
        if time >= 8:
            print(True)
        else:
            print(False)
    elif location == "Outdoor": 
        if time >= 4:
            print(True)
        else:
            print(False)
main(str(input()), float(input()))
