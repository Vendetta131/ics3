const assert = require('chai').assert;
const {gitDescribe, gitDescribeSync} = require('git-describe');
const gitInfo = gitDescribeSync();

const app = require('../app1');

describe(`Test app version: ${gitInfo.raw}`, function() {
  describe('sayHello()', function() {
    it('sayHello should return string', function() {
      let result = app.sayHello();
      assert.typeOf(result, 'string');
    })

    it('sayHello should return hello', function() {
      let result = app.sayHello();
      assert.equal(result, 'hello');
    });
  })
  describe('addNumbers()', function() {
    it('addNumbers should return number', function() {
      let result = app.addNumbers(2, 3);
      assert.typeOf(result, 'number');
    })
    it('addNumbers should be above 5', function() {
      let result = app.addNumbers(3, 3);
      assert.isAbove(result, 5);
    })
  })
});