"""File for task 3; a function that adds the the hour, minute, and second values at a given time"""


def sum_current_time(time_str: str) -> int:
    """Adds the the hour, minute, and second values at a given time"""

    if not isinstance(time_str, str):
        raise ValueError("Input is not a string")

    list_of_nums = time_str.split(":")
    list_of_nums_int = []
    for num in list_of_nums:
        list_of_nums_int.append(int(num))
    return sum(list_of_nums_int)


if __name__ == "__main__":
    print(sum_current_time("12:12:12"))
