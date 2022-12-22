from mapping import Mapper
from handle_content import *


def main(args):
    backpacks = list_backpacks(unload_data_from_file(args))
    run_part_one(args)
    run_part_two(args)

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
    # Get the grouped data
    grouped_data = make_groups_of_three(backpacks)

    # Loop over the list of groups
    for group in grouped_data:
        # We have 3 elements in each group here
        group[0] = sorted(group[0])
        group[1] = sorted(group[1])
        group[2] = sorted(group[2])

        
if __name__ == '__main__':
    main("resources/input_data.txt")  # Hard-coded params
