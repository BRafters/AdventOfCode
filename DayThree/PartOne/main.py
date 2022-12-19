from mapping import Mapper
from handle_content import *


def main(args):
    # Read in input from a file
    mapper = Mapper()
    backpacks = list_backpacks(unload_data_from_file(args))
    duplicates = []

    for backpack in backpacks:
        duplicates.append(list(search_for_duplicates(backpack)))

    for duplicate in duplicates:
        if len(duplicate) == 0:
            continue
        if duplicate[0] == [] or duplicate[0] == None:
            continue
        mapper.inc_total_priorities(duplicate[0])

    print(mapper.get_priority_total())

if __name__ == '__main__':
    main("resources/input_data.txt")  # Hard-coded params
