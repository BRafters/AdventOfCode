class Stack {
    constructor() {
        this.stack = [];
        this.size = 0;
    }

    // Add to the stack
    push(item) {
        this.stack[this.size++] = item;
    }

    // Remove from the stack
    pop() {
        return this.stack[--this.size];
    }

    // Look at top item in the stack
    peek() {
        return this.stack[this.size - 1];
    }

    // Delete the entire stack
    clear() {
        this.stack.clear();
    }
}

module.exports = {Stack}