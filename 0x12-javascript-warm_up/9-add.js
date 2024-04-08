#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

const fun = add(a, b);

console.log(fun);

function add (a, b) {
  return a + b;
}
