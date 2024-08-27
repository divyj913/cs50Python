def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and s[:2].isalpha() and 2<len(s)<6:
        return True
    else:
        return False


main()
