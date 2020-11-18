class User {
  constructor(name) {
    this.name = name;
    this.tasks = [];
    this.points = 0;
  }
}

class Task {
  constructor(title, due, points){
    this.title = title
    this.due = due;
    this.points = points;
  }
}

module.exports = {
  User,
  Task
}