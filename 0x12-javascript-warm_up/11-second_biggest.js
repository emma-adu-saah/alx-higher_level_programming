#!/usr/bin/node

const args = process.argv;
if (args.length <= 2) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  let newArray = (args.slice(2)).map((element) => parseInt(element));
  newArray = newArray.sort((a, b) => b - a);
  console.log(newArray[1]);
}
