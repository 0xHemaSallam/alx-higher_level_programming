#!/usr/bin/node
const process = require('process'); // Import the process object

console.log(`${process.argv[2]} is ${process.argv[3] || "undefined"}`);
