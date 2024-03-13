#!/usr/bin/node
const baseSquare = require('./5-square');

class Square extends baseSquare {

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
