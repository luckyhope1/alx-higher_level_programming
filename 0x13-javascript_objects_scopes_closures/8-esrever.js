#!/usr/bin/node

/**
 * Returns the reversed version of a list.
 * @param {Array} list - The list to be reversed.
 * @returns {Array} - The reversed version of the list.
 */
exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
