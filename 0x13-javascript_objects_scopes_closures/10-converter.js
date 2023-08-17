#!/usr/bin/node

/**
 * Converts a number from base 10 to another base passed as argument.
 * @param {number} base - The base to convert the number to.
 * @returns {Function} - A function that converts a number to the specified
 * base.
 */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
