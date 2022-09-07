#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
console.log(Number.isNaN(num) ? 'Not a number' : 'My number: ' + String(num));
