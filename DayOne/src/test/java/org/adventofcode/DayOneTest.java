package org.adventofcode;

import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.io.File;
import java.net.URL;
import java.util.List;

public class DayOneTest {
    private static URL test_file;
    private static List<String> allElvesCalories;

    @BeforeClass
    public void setup() {
        test_file = Thread.currentThread().getContextClassLoader().getResource("dayOneTestList.txt");
        allElvesCalories = Main.readFile(new File(test_file.getFile()));
    }

    @Test
    public void testIfReadFromFileWorks() {
        System.out.println("Running a pre-test");

        Assert.assertFalse(allElvesCalories.size() == 0);
        Assert.assertNotNull(allElvesCalories);
        prettyPrint(allElvesCalories);
        System.out.println("Successfully read content");
    }

    @Test
    public void testArraySize(){
        System.out.println("Test List Size");
        Assert.assertEquals(allElvesCalories.size(), 5);
    }

    @Test
    public void testMakeHeap(){
        int highestCals;
        String elfName;
        MaxHeap heap = new MaxHeap();
        System.out.println("Test Max Heap");

        int i = 1;
        for (String elfCalories : allElvesCalories) {
            heap.insertNode("Elf #" + i++, elfCalories);
        }

        // 18316 - Third element in list
        highestCals = heap.getRoot().getCalories();
        elfName = heap.getRoot().getNameOfElf();

        // Highest value should be at the root node
        Assert.assertEquals(highestCals, 18316);
        returnResults(elfName, highestCals);
    }

    private void returnResults(String elfName, Integer calories) {
        System.out.println(elfName + " has the most calories, they hold: " + calories + " calories.");
    }

    private void prettyPrint(List<String> arr) {
        for (int i = 0; i < arr.size(); i++){
            System.out.println(arr.get(i) + '\n');
        }
    }
}
