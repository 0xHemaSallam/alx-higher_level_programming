#!/usr/bin/node
const process = require('process');

const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg);
if (parsedInt) {
  for (let index = 0; index < parsedInt; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
