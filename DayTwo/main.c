#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define WIN 6;
#define DRAW 3;
#define LOSS 0;

bool isEqual(char player_choice, char opponent_choice);

void incrementScores(bool round_winner, char player_choice, char opponent_choice);

void read_file(char *file_name);

void determine_round_winner(char opponent_choice, char player_choice);

bool check_opponent_choice(char player_choice, char opponent_choice);

// Initialize Player and opponent scores
int player_score = 0;
int opponent_score = 0;

// argc == ARGument Count
// argv == ARGument Vector <- array of character pointers listing all arguments
int main(int argc, char **argv) {
    // If we dont have exactly two arguments, we end execution
    if (argc < 2)
        return 1;

    // Get the file
    char *file_name = argv[argc - 1];

    read_file(file_name);

    printf("Opponent score is: %d\nPlayer score is: %d\n", opponent_score, player_score);
    return 0;
}

void read_file(char file_name[]) {
    FILE *input_file;
    char buffer[255];
    // Open the file
    input_file = fopen(file_name, "r");

    // Make sure file is open
    if (input_file == NULL) {
        return;
    }

    while (fgets(buffer, sizeof(buffer), input_file) != NULL) {
        determine_round_winner(buffer[0], buffer[2]); // -2 as we need to skip the \n
    }

    fclose(input_file);
}

int get_choice_score(char choice) {
    if (choice == 'A' || choice == 'X')
        return 1;
    else if (choice == 'B' || choice == 'Y')
        return 2;
    else if (choice == 'C' || choice == 'Z')
        return 3;

    return 0;
}

void determine_round_winner(char opponent_choice, char player_choice) {
    // Determine draw
    // Set the scores
    if (isEqual(player_choice, opponent_choice)) {
        // Set both the players and the opponents score
        opponent_score += get_choice_score(opponent_choice) + DRAW;
        player_score += get_choice_score(player_choice) + DRAW;
        return;
    }

    bool round_winner = check_opponent_choice(player_choice, opponent_choice);

    incrementScores(round_winner, player_choice, opponent_choice);
}

void incrementScores(bool round_winner, char player_choice, char opponent_choice) {
    if (round_winner) {
        player_score += get_choice_score(player_choice) + WIN;
        opponent_score += get_choice_score(opponent_choice) + LOSS;
    } else {
        player_score += get_choice_score(player_choice) + LOSS;
        opponent_score += get_choice_score(opponent_choice) + WIN;
    }
}

bool isEqual(char player_choice, char opponent_choice) {
    if (player_choice == 'X' && opponent_choice == 'A' || player_choice == 'Y' && opponent_choice == 'B' ||
        player_choice == 'Z' && opponent_choice == 'C')
        return true;

    return false;
}

bool check_opponent_choice(char player_choice, char opponent_choice) {
    if (player_choice == 'X')
        return opponent_choice == 'C';
    else if (player_choice == 'Y')
        return opponent_choice == 'A';
    else if (player_choice == 'Z')
        return opponent_choice == 'B';

    return false;
}