#!/usr/bin/node
// Prints the first argument passed to it.

const { argv } = require('process');
let numberOfArgs = 0;

for (const _ of argv) {
  numberOfArgs++;
}

if (numberOfArgs <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
