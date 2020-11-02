const http = require('http');
const express = require('express');

const app = express();
const server = http.createServer(app);

app.use(express.json());
/*

[{'user1':
  [
    {
      title: 'task name',
      due: 5,
      points: 2
    }...
  ]
}...]

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

app.post('/get', async (req, res) => {
  
  let ans = data.find(e => e == req.query.name);
  console.log(req.query)
  if (ans === undefined){
    
    const name = req.query.name;
    newUser = {name: name, tasks: []}
    data.push(newUser)
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
    newTask = {
      title: req.query.title,
      due: req.query.due,
      points: req.query.points
    }
    data[index].tasks.push(newTask);

    res.send(data.find(e => e.name == req.query.name));
  }
  console.log(data.find(e => e.name == req.query.name).tasks);
});

app.post('/removetask', async (req, res) => {
  let user = data.find(e => e.name == req.query.name);
  if (user === undefined){
    res.send(null);
  } else {
    const userIndex = data.findIndex(e => e.name === req.query.name);
    if (userIndex > -1){
      const taskIndex = data[userIndex].tasks.findIndex(e => e.title === req.query.title);
      data[userIndex].tasks.splice(taskIndex, 1);
    }

    res.send(data.find(e => e.name == req.query.name));
  }
  console.log(data.find(e => e.name == req.query.name).tasks);
})

const PORT = process.env.PORT || 3001;

server.listen(PORT, () => console.log('server running on port', PORT));

