// function showToDo(todo: {title: string, text: string}){
//   console.log(todo.title+': ' + todo.text);
  
// }

// let myToDo = {title:'Trash', text: 'Take out the trash later tonight'};

// showToDo(myToDo);

interface ToDo {
  title: string;
  text: string;
}

function showToDo(todo: ToDo){
  console.log(todo.title+': ' + todo.text);
}

let myToDo = {title:'Trash', text: 'Take out the trash later today around 9pm'};

showToDo(myToDo);