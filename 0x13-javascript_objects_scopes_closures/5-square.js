#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Define a class named Square that inherits from Rectangle
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
