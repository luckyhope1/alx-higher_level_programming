#!/usr/bin/node

let numArgs = 0;

/**
 * Prints the number of arguments already printed and the new argument value.
 * @param {*} item - The argument to be printed.
 */
exports.logMe = function (item) {
  console.log(`${numArgs}: ${item}`);
  numArgs++;
};
