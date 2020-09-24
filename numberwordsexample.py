from  numberwords import grouping_func
def main():
    number = num = None
    while True:
        number = input("Enter number : ")
        if not number.replace(',','').isdigit():
            print("Incorrect input. Try again!")
            continue
        num = number.replace(',','')
        break
    print(f"\nNumber representation : {num}\nString representation : {grouping_func(num)}")
if __name__ == "__main__":
    main()
