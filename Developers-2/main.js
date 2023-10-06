const prompt = require("prompt-sync")();

let tasks = [];
let completed_tasks= [];

function add_task(task){
   tasks.push(task);
   console.log(tasks)
   
}
function complete_task(complete){
    let index = tasks.indexOf(complete);
    completed_tasks.push(complete);
    tasks.splice(index, 1);
    console.log(completed_tasks)
}

function deleted_task(deleted){
    let del = completed_tasks.indexOf(deleted);
    completed_tasks.splice(del, 1);
    console.log(tasks)
}


function getInput(){
    console.log('Type add, delete or complete to manage your tasks. Type exit to exit')
    let userInput = prompt()
    if (userInput === 'add') {
        console.log('What do you want to add?')
        task = prompt()
        add_task(task)
        getInput()
    } else if (userInput === 'delete') {
        console.log('What do you want to delete?')
        deleted = prompt()
        deleted_task(deleted)
        getInput()
    } else if (userInput === 'complete') {
        console.log('What did to complete?') 
        complete = prompt()
        complete_task(complete)
        getInput()
        } else if (userInput === 'exit') {
        return
    } else {
        console.log('Please enter a valid command.')
        getInput()
    }
}

console.log('Hello welcome to Task Manager')
getInput()