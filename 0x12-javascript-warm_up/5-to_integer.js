#!/usr/bin/node
const process = require('process');

const firstArg = process.argv[2];
const parsedInt = parseInt(firstArg);

console.log(isNaN(parsedInt) ? 'Not a number' : `My number: ${parsedInt}`);
