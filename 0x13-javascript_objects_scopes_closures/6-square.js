#!/usr/bin/node
const Square_1 = require('./5-square');

class Square extends Square_1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    const character = c.repeat(this.size);
    let i = 0;
    while (i < this.size) {
	  console.log(character);
	  i++;
    }
  }
}

module.exports = Square;
