package org.adventofcode;

// Formula:
// leftChild = idx * 2 + 1
// rightChild = idx * 2 + 2
// getParent = (idx - 1) / 2

import java.util.Arrays;

public class MaxHeap {
    private Node[] heap;
    private Integer size;

    public MaxHeap() {
        this.heap = new Node[10];
        size = 0;
    }

    public void insertNode(String elfName, String strFoodItems) {
        // Split the string
        String[] items = strFoodItems.split("\n");
        int[] foodItems = new int[items.length];

        for (int i = 0; i < items.length; i++) {
            foodItems[i] = Integer.parseInt(items[i]);
        }

        insertNode(elfName, foodItems);
    }

    public void insertNode(String elfName, int[] foodItems) {
        if (size == this.heap.length - 1)
            resize_heap();

        Node newNode = new Node(elfName, foodItems);

        this.heap[this.size++] = newNode;
        Integer idx = this.size - 1;

        // Check to see if the new node is greater than all the other nodes
        while(this.heap[idx].getCalories() > this.heap[getParent(idx)].getCalories() && idx > 0) {
            bubble(idx, getParent(idx));
            idx = getParent(idx);
        }
    }

    private void bubble(int idxOne, int idxTwo) {
        Node temp = this.heap[idxTwo];
        this.heap[idxTwo] = this.heap[idxOne];
        this.heap[idxOne] = temp;
    }

    private void resize_heap() {
        Node[] newHeap = new Node[this.heap.length + 10];
        for (int i = 0; i < this.heap.length; i++) {
            newHeap[i] = this.heap[i];
        }

        this.heap = newHeap;
    }

    public Node getRoot() {
        return this.heap[0];
    }

    public Integer getSize() {
        return this.size;
    }

    private Integer getParent(Integer idx) {
        return (idx - 1) / 2;
    }

    private Integer getLeft(Integer idx) {
        return (idx * 2) + 1;
    }

    private Integer getRight(Integer idx) {
        return (idx * 2) + 2;
    }

    private boolean hasLeftChild(Integer idx) {
        return getLeft(idx) <= this.size;
    }

    private boolean hasRightChild(Integer idx) {
        return getRight(idx) <= this.size;
    }
}
