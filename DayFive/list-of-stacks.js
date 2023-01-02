const {Stack} = require('./stack');

class StackList {
    constructor() {
        this.listOfStacks = [];
    }

    add(location, item) {
        // Check if the location within the listOfStacks is defined or not null
        if (this.isEmpty(location))
            this.listOfStacks[location] = new Stack();

        this.listOfStacks[location].push(item);
    }

    move(locOfItem, newItemLoc) {
        this.listOfStacks[newItemLoc].push(this.listOfStacks[locOfItem].pop());
    }

    isEmpty(location) {
        return this.listOfStacks[location] === undefined || this.listOfStacks === null;
    }
}