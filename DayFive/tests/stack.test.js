const {Stack} = require('../stack.js');

test('Add 3 items to stack, expect number 3 at the top', () => {
    let myStack = new Stack;
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    expect(myStack.peek()).toBe(3);
});

test("Remove the top of the stack. Expect 2 to be at the top now", () => {
    let myStack = new Stack();

    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    expect(myStack.pop()).toBe(3);
    expect(myStack.peek()).toBe(2);
});

test('Test variable number of items in stack. Peek at result', () => {
    let myStack = new Stack();

    // For 10 entries, add to the stack
    for(let i = 1; i < 11; i++){
        myStack.push(i);
    }

    expect(myStack.peek()).toBe(10);
});