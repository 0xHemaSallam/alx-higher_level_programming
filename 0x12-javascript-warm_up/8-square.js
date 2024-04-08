#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('#'.repeat(firstArg));
  }
}
