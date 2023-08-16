#!/usr/bin/node

function findSecondLargest (arr) {
  if (arr.length <= 1) {
    return 0;
  }

  arr = arr.map(Number);
  arr.sort((a, b) => b - a);
  return arr[1];
}

const args = process.argv.slice(2);
const secondLargest = findSecondLargest(args);

console.log(secondLargest);
