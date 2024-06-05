var request = require('request');
console.log(request.post('https://socialpancakes-d1dad.firebaseio.com/Users/.json', {'name': 'Buddy', 'email': 'budders@buddy.com', 'comment': 'best doggy every'}));

(async () => {
  try {
    const res = await fetch("https://socialpancakes-d1dad.firebaseio.com/Users.json");
    const headerDate = res.headers && res.headers.get('date') ? res.headers.get('date') : 'no response date';
    console.log('Status Code:', res.status);
    console.log('Date in Response header:', headerDate);

    const users = await res.json();
    console.log(users);
    var keys = Object.keys(users);
    console.log(keys);
    for (var i = 0; i < keys.length; i++) {
      rec = users[keys[i]];
      console.log(rec['name']);
    }
  } catch (err) {
    console.log(err.message); //can be console.error
  }
})();let fetch = require('node-fetch');

fetch('http://localhost', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{}'
}).then(response => {
  return response.json();
}).catch(err => {console.log(err);});

/*
fetch("https://socialpancakes-d1dad.firebaseio.com/Users.json")
.then((res)=> res.json())
.then((data)=>console.log(data))
.catch((err)=>{
    console.log("error occured", err)
});
*/

