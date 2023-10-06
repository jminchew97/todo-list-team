let tasks = [];
let completed_tasks= [];
function add_task(task){
   tasks.push(task);
   
}
function complete_task(complete){
 
    let index = tasks.indexOf(complete);
    completed_tasks.push(complete);
    tasks.splice(index, 1);
}
function deleted_task(deleted){
    let del = completed_tasks.indexOf(deleted);
    completed_tasks.splice(del, 1);
}
