def unload_data_from_file(file_name=''):
    if file_name == '':
        return

    file = open(file_name, "rt")
    text = file.read()
    file.close()
    return text


def list_backpacks(data=''):
    if data == '':
        return

    return data.splitlines()


def make_groups_of_three(data=[]):
    groups = 3
    grouped_data = []

    for i in range(0, len(data), groups):
        grouped_data.append(data[i:i + groups])

    return grouped_data


def check_for_even_groups(data=[]):
    return len(data) % 3 == 0

def split_string_data(data=''):
    return list(data)

# TODO: Make this function more flexible
def find_common_items(grouped_data=[]):
    common_items = []
    size_of_group = len(grouped_data)
    first_elf = set()
    second_elf = set()
    third_elf = set()


    # Take the grouped data
    for group in grouped_data:
        firstElf = set(group[0])
        secondElf = set(group[1])
        thirdElf = set(group[2])

        common_items.append(list(firstElf.intersection(secondElf, thirdElf)))

    return common_items
def search_for_duplicates(data=[]):
    # Get the pointer to the center of the string
    center_ptr = int(len(data) / 2)
    left_half = data[0:center_ptr]
    right_half = data[center_ptr:len(data)]

    set_of_left_items = set(*[left_half])
    set_of_right_items = set(*[right_half])

    # Returns duplicates
    return set_of_left_items.intersection(set_of_right_items)


def sort_data(data=[]):
    return
