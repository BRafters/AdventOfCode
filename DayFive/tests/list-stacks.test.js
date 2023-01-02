const {Stack} = require('../stack');

test('Test create list of stacks. Find item at the second element.', () => {
    let listOfStacks = [];

    for (let i = 0; i < 11; i++) {
        listOfStacks.push(new Stack());
    }

    // Expect the size to be 10
    expect(listOfStacks.length).toBe(10);

    // Add items at certain areas
    
});