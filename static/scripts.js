document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.textContent = `${task.title} - ${task.due_date}`;
                taskList.appendChild(li);
            });
        });
});