require('dotenv').config()
const fetch = require('node-fetch')
const express = require('express')

const port = process.env.PORT || 3000
const nbTasks = parseInt(process.env.TASKS) || 20

const randInt = (min, max) => Math.floor(Math.random() * (max - min)) + min
const taskType = () => (randInt(0, 2) ? 'mult' : 'add')
const args = () => ({ a: randInt(0, 40), b: randInt(0, 40) })

const generateTasks = (i) =>
  new Array(i).fill(1).map((_) => ({ type: taskType(), args: args() }))

let workers = [{ url: 'http://worker:8080', id: '0', mult: true, add: false},{ url: 'http://worker1:8080', id: '1', mult: true, add: false},{ url: 'http://worker2:8080', id: '2', mult: false, add: true}]
  // { url: 'http://localhost:8080', id: '' }


const app = express()
app.use(express.json())
app.use(
  express.urlencoded({
    extended: true,
  })
)

app.get('/', (req, res) => {
  res.send(JSON.stringify(workers))
})

app.post('/register', (req, res) => {
  const { url, id , mult , add } = req.body
  console.log(`Register: adding ${url} worker: ${id} mult: ${mult} add: ${add}`)
  workers.push({ url, id, mult, add })
  res.send('ok')
})

let tasks = generateTasks(nbTasks)
let taskToDo = nbTasks

const wait = (mili) =>
  new Promise((resolve, reject) => setTimeout(resolve, mili))

/*const sendTask = async (task) => {
  let worker = null;
  if (task.type === 'mult') {
    worker = workers.find((w) => w.mult === true);
  } else if (task.type === 'add') {
    worker = workers.find((w) => w.add === true);
  }
  if (!worker) {
    console.error(`No worker available for task type ${task.type}`);
    tasks = [...tasks, task];
    return;
  }
  console.log(`=> ${worker.url}/${task.type}`, task);
  workers = workers.filter((w) => w.id !== worker.id);
  tasks = tasks.filter((t) => t !== task);
  const request = fetch(`${worker.url}/${task.type}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(task.args),
  })
    .then((res) => {
      workers = [...workers, worker];
      return res.json();
    })
    .then((res) => {
      taskToDo -= 1;
      console.log('---');
      console.log(nbTasks - taskToDo, '/', nbTasks, ':');
      console.log(task, 'has res', res);
      console.log('---');
      return res;
    })
    .catch((err) => {
      console.error(task, ' failed', err.message);
      tasks = [...tasks, task];
    });
};*/
const sendTask = async (task) => {
  let worker = null;
  if (task.type === 'mult') {
    worker = workers.find((w) => w.mult === true);
  } else if (task.type === 'add') {
    worker = workers.find((w) => w.add === true);
  }
  if (!worker) {
    //console.error(`No worker available for task type ${task.type}`);
    tasks = [...tasks, task];
    return;
  }
  console.log(`=> ${worker.url}/${task.type}`, task);
  workers = workers.filter((w) => w.id !== worker.id);
  tasks = tasks.filter((t) => t !== task);
  const request = fetch(`${worker.url}/${task.type}`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(task.args),
  })
    .then((res) => {
      workers = [...workers, worker];
      return res.json();
    })
    .then((res) => {
      taskToDo -= 1;
      console.log('---');
      console.log(nbTasks - taskToDo, '/', nbTasks, ':');
      console.log(task, 'has res', res);
      console.log('---');
      return res;
    })
    .catch((err) => {
      console.error(task, ' failed', err.message);
      tasks = [...tasks, task];
    });
};


const main = async () => {
  console.log(tasks)
  while (taskToDo > 0) {
    await wait(100)
    if (workers.length === 0 || tasks.length === 0) continue
    sendTask(tasks[0])
  }
  console.log('end of tasks')
  server.close()
}

const server = app.listen(port, () => {
  console.log(`Register listening at http://localhost:${port}`)
  console.log('starting tasks...')
  main()
})
