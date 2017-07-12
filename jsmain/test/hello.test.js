const test = require('ava');
const hello = require('../src/hello');

test('hello world', t => {
  t.is(hello(), 'Hello World!!')
});
