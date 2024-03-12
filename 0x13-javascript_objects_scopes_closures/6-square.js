#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined || c === null) { c = 'X'; }
    const character = c.repeat(this.size);
    let i = 0;
    while (i < this.size) {
      console.log(character);
      i++;
    }
  }
}

module.exports = Square;
