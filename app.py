from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/tasks')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form['task_title']
    tasks.append({'title': task_title, 'completed': False})
    return redirect(url_for('index'))

def view_tasks(completed_only=False):
    sorted_tasks = sorted(todo_list, key=lambda task: (task["completed"], task["task"]))
    if completed_only:
        return [(index + 1, task["task"], task["completed"]) for index, task in enumerate(sorted_tasks) if task["completed"]]
    else:
        return [(index + 1, task["task"], task["completed"]) for index, task in enumerate(sorted_tasks)]


@app.route('/complete/<int:index>')
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)