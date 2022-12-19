package org.adventofcode;

public class Node {
    private String nameOfElf;
    private Integer calories;

    public Node(String nameOfElf, int[] foodItems) {
        this.calories = 0;
        for (int i = 0; i < foodItems.length; i++) {
            this.calories += foodItems[i];
        }
        this.nameOfElf = nameOfElf;
    }

    public String getNameOfElf() {
        return nameOfElf;
    }

    public Integer getCalories() {
        return calories;
    }
}
