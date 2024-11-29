from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import Config
from models import db, Task, ActionLog, TaskAudit
from forms import TaskForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)


# from .views import tasks_bp
# app.register_blueprint(tasks_bp)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data,
                    due_date=form.due_date.data, completed=form.completed.data,
                    user_id=1)  # Hardcoded user_id for simplicity
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    tasks = Task.query.all()
    return render_template('tasks.html', form=form, tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_list = [{'id': task.id, 'title': task.title, 'description': task.description,
                   'due_date': task.due_date, 'completed': task.completed} for task in tasks]
    return jsonify(tasks_list)

if __name__ == '__main__':
    app.run(debug=True)