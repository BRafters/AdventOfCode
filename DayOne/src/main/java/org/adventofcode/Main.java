package org.adventofcode;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Integer i = 1;
        MaxHeap heap = new MaxHeap();
        List<String> elves = readFile(new File(args[0]));

        for (String elf : elves) {
            heap.insertNode("Elf #" + i++, elf);
        }

        System.out.println(heap.getRoot().getNameOfElf() + ": " + heap.getRoot().getCalories());
    }

    ////
    // Reads in the file brought in from the command line
    ////
    public static List<String> readFile(File file) {
        StringBuilder resultFromFile = new StringBuilder();
        int ch;

        // Open the file, read its contents
        try (InputStream is = new FileInputStream(file); BufferedInputStream bis = new BufferedInputStream(is)) {
            while ((ch = bis.read()) != -1) {
                resultFromFile.append((char) ch);
            }
        } catch (IOException e) {
            System.out.println("Could not read file: \n" + e.getMessage());
        }

        return new ArrayList<>(Arrays.asList(resultFromFile.toString().split("\n\n")));
    }
}
