const {gitDescribe, gitDescribeSync} = require('git-describe');
const gitInfo = gitDescribeSync().raw;

const app = require('./app1');
const getUser = require('./app2').getUser;

console.log(`Start app version ${gitInfo}`);
console.log(app.sayHello());
console.log(app.addNumbers(3,5));
getUser().then((data) =>{
  console.log(data);
})

