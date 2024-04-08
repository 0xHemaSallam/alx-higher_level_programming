#!/usr/bin/node
const process = require('process');

const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg);

if (isNaN(parsedInt) || parsedInt <= 0) {
  console.log('Missing size');
} else {
  for (let row = 0; row < parsedInt; row++) {
    for (let col = 0; col < parsedInt; col++) {
      process.stdout.write('#');
    }
    console.log();
  }
}
