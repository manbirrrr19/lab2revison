import statistics


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input("Enter choice:")
    split_user_input = user_input.split(",")
    list_input = [int(i) for i in split_user_input]
    return list_input


def calc_average(list):
    return statistics.mean(list)


def find_min_max(list):
    min_list = min(list)
    max_list = max(list)
    return min_list, max_list


def sort_temperature(list):
    sorted_list = sorted(list)
    return sorted_list


def calc_median_temperature(sorted_list):
    return statistics.median(sorted_list)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("You entered: " + str(num_list))
    avg_list = calc_average(num_list)
    print("Average = " + str(avg_list))
    min_list, max_list = find_min_max(num_list)
    print("Min = " + str(min_list) + ", Max = " + str(max_list))
    sorted_list = sort_temperature(num_list)
    print("Sorted = " + str(sorted_list))
    median_list = calc_median_temperature(sorted_list)
    print("Median = " + str(median_list))


if __name__ == "__main__":
    main()
#To call a variable from another function, at the end of first function type "return <var>" and in 2nd function, js type function() and var will be given