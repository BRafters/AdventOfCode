#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

vector<int> get_data(std::string file_name);

void num_of_nested_pairs(int *line_of_data, int arr_size);

bool is_nan(char c);

bool contains_within(int *elf_one, int *elf_two);

bool has_one_task(int *elf);

bool is_overlapping(int *target_elf, int *other_elf);

bool is_contained(int *target_elf, int *other_elf);

bool contains_at_all(int pInt[2], int pInt1[2]);

bool is_either_overlapping(int *target_elf, int *other_elf);

int main(int argc, char **argv) {
    std::string file_name = argv[1];
    vector<int> nums = get_data(file_name);

    num_of_nested_pairs(nums.data(), nums.size());
}

// Grabs the data from the file & places it in an array of numbers
vector<int> get_data(std::string file_name) {
    std::string line;
    std::stringstream lines, tmp;
    std::ifstream in_file_stream;
    std::vector<int> numbers;

    in_file_stream.open(file_name);
    if (in_file_stream.is_open()) {
        // Attempt to get all the data in the file
        while (std::getline(in_file_stream, line))
            lines << line << '\n';

        for (int i = 0; i < lines.str().size(); i++) {
            if (is_nan(lines.str()[i])) {
                numbers.push_back(std::stoi(tmp.str()));
                tmp.str("");
                tmp.clear();
                continue;
            }

            tmp << lines.str()[i];
        }
    } else {
        return numbers;
    }

    in_file_stream.close();
    return numbers;
}

void num_of_nested_pairs(int *line_of_data, int arr_size) {
    int elf_one[2], elf_two[2];
    int count_of_pairs[2] = {0, 0};

    // e1: 0-1, e2: 2-3
    for (int i = 0; i < arr_size; i += 4) {
        elf_one[0] = line_of_data[i];
        elf_one[1] = line_of_data[i + 1];

        elf_two[0] = line_of_data[i + 2];
        elf_two[1] = line_of_data[i + 3];
        if (contains_within(elf_one, elf_two)) {
            ++count_of_pairs[0];
        }

        if (contains_at_all(elf_one, elf_two)) {
            ++count_of_pairs[1];
        }
    }

    std::cout << "Count of nested tasks: \n" << count_of_pairs[0] << std::endl;
    std::cout << "Count of ANY overlapping tasks: \n" << count_of_pairs[1] << std::endl;
}

bool contains_at_all(int *elf_one, int *elf_two) {
    return is_either_overlapping(elf_one, elf_two) || is_either_overlapping(elf_two, elf_one);
}

bool contains_within(int *elf_one, int *elf_two) {
    // We know that these arrays are of size 2
    // TODO: Clean this!
    if (is_contained(elf_one, elf_two) || is_contained(elf_two, elf_one))
        return true;
    else if (has_one_task(elf_one) && is_overlapping(elf_one, elf_two) ||
             has_one_task(elf_two) && is_overlapping(elf_two, elf_one))
        return true;

    return false;
}

bool has_one_task(int *elf) {
    // We know that the size should be 2
    return elf[0] == elf[1];
}

bool is_overlapping(int *target_elf, int *other_elf) {
    return target_elf[0] >= other_elf[0] && target_elf[0] <= other_elf[1];
}

bool is_either_overlapping(int *target_elf, int *other_elf) {
    if (target_elf[0] >= other_elf[0] && target_elf[0] <= other_elf[1])
        return true;

    return target_elf[1] <= other_elf[1] && target_elf[1] >= other_elf[0];
}

bool is_contained(int *target_elf, int *other_elf) {
    return target_elf[0] <= other_elf[0] && target_elf[1] >= other_elf[1];
}

bool is_nan(char c) {
    return c == '-' || c == ',' || c == '\n';
}