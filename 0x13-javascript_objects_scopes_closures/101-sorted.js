#!/usr/bin/node

const dict = require('./101-data').dict;

const usersByOccurrence = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!usersByOccurrence[occurrences]) {
    usersByOccurrence[occurrences] = [];
  }
  usersByOccurrence[occurrences].push(userId);
}

console.log(usersByOccurrence);
