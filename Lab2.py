def display_main_menu():
    print("display_main_menu")

def get_user_input():
    nums = input("Enter some numbers separated by commas (e.g. 5,67,32): ")
    split = nums.split(",")
    print([float(x) for x in split])
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()


main()