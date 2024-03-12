#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let newArray = args.sort();
  newArray = newArray.reverse();
  console.log(newArray[1]);
}
