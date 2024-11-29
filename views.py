from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from models import db, Task
from forms import TaskForm

tasks_bp = Blueprint('tasks', __name__)



class TaskView:
    @tasks_bp.route('/tasks', methods=['GET', 'POST'])
    def tasks(self):
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(title=form.title.data, description=form.description.data,
                        due_date=form.due_date.data, completed=form.completed.data,
                        user_id=1)  # Hardcoded user_id for simplicity
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('tasks.tasks'))
        tasks = Task.query.all()
        return render_template('tasks.html', form=form, tasks=tasks)

    @tasks_bp.route('/api/tasks', methods=['GET'])
    def get_tasks(self):
        tasks = Task.query.all()
        tasks_list = [{'id': task.id, 'title': task.title, 'description': task.description,
                       'due_date': task.due_date, 'completed': task.completed} for task in tasks]
        return jsonify(tasks_list)

# app.register_blueprint(tasks_bp)


