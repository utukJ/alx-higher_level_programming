#!/usr/bin/node
const argc = process.argv.length;
if (argc === 2) {
  console.log('No argument found');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
