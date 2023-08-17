#!/usr/bin/node

/**
 * Returns the number of occurrences of searchElement in list.
 * @param {Array} list - The array in which to search for occurrences.
 * @param {*} searchElement - The element to search for.
 * @returns {number} - The number of occurrences of searchElement in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
