from mapping import Mapper
from handle_content import *


def main(args):
    backpacks = list_backpacks(unload_data_from_file(args))
    run_part_one(backpacks)
    run_part_two(backpacks)


def run_part_one(backpacks=[]):
    # Read in input from a file
    mapper = Mapper()
    duplicates = []

    for backpack in backpacks:
        duplicates.append(list(search_for_duplicates(backpack)))

    for duplicate in duplicates:
        if len(duplicate) == 0:
            continue
        elif duplicate[0] == [] or duplicate[0] == None:
            continue
        mapper.inc_total_priorities(duplicate[0])

    print(mapper.get_priority_total())


def run_part_two(backpacks=[]):
    mapper = Mapper()

    # Get the grouped data
    grouped_data = make_groups_of_three(backpacks)
    common_items = find_common_items(grouped_data)

    for item in common_items:
        if len(item) == 0:
            continue

        if item[0] == [] or item[0] == None:
            continue

        mapper.inc_total_priorities(item[0])

    print(mapper.get_priority_total())

if __name__ == '__main__':
    main("resources/input_data.txt")  # Hard-coded params
