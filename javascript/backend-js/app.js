const http = require('http');
const express = require('express');
const fs = require('fs');

const app = express();
const server = http.createServer(app);

const cron = require('node-cron');

const types = require('./datatypes');

app.use(express.json());
/*
data = [
  {name: "baru",
   tasks: [
     {title: "task1",
      due: 5,
      points: 2}
   ]}
]
*/

data = []

score = []

app.post('/get', async (req, res) => {
  
  let ans = data.find(e => e.name == req.query.name);
  console.log(ans);
  //console.log(req.query)
  if (ans === undefined){
    
    const name = req.query.name;
    newUser = new types.User(name);
    data.push(newUser)
    score.push(newUser)
    res.send(newUser)
  } else {
    res.send(ans)
  }
  console.log(data)
})

app.post('/addtask', async (req, res) => {
  let user = data.find(e => e.name == req.query.name);
  if (user === undefined){
    res.send(null);
  } else {
    const index = data.findIndex(e => e.name === req.query.name);

    taskExists = data[index].tasks.findIndex(e => e.title === req.query.title);

    if (taskExists > -1){
      data[index].tasks[taskExists] = new types.Task(req.query.title, req.query.due, req.query.points);
    } else {
      newTask = new types.Task(req.query.title, req.query.due, req.query.points);
      data[index].tasks.push(newTask);
      
    }

    data[index].tasks.sort(function(a, b) {
      return a.due - b.due;
    })

    res.send(data.find(e => e.name == req.query.name));
  }
  console.log(data.find(e => e.name == req.query.name).tasks);
});

app.post('/removetask', async (req, res) => {
  let user = data.find(e => e.name == req.query.name);
  let points = null;
  if (user === undefined){
    res.send(null);
  } else {
    const userIndex = data.findIndex(e => e.name === req.query.name);
    
    if (userIndex > -1){
      const taskIndex = data[userIndex].tasks.findIndex(e => e.title === req.query.title);
      points = data[userIndex].tasks[taskIndex].points;
      data[userIndex].tasks.splice(taskIndex, 1);
    }
    let scoreIndex = score.findIndex(e => e.name === req.query.name);
    score[scoreIndex].points += parseInt(points);

    let scoreString = "";
    for (s of score){
      scoreString += `${s.name} ${s.points} \n`
    }
    fs.writeFileSync('../data.txt', scoreString)

    res.send(points);
  }
  console.log(data.find(e => e.name == req.query.name).tasks);
});

app.get('/midnight', async(req, res) => {
  decrementAllDueDates();
  res.send(data)
})

function decrementAllDueDates(){

  for(let user of data){
    for(let task of user.tasks){
      task.due = (task.due-1).toString();
    }
  }
}

cron.schedule('* 0 * * *', () => {
  decrementAllDueDates();
})

const PORT = process.env.PORT || 3001;

server.listen(PORT, () => console.log('server running on port', PORT));
