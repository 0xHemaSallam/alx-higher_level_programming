#!/usr/bin/node
const process = require('process');

const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg);

if (isNaN(parsedInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(parsedInt); i++) {
    console.log('X'.repeat(parseInt(parsedInt)));
  }
}
