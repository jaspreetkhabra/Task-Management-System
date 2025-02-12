from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            description TEXT,
                            completed BOOLEAN NOT NULL DEFAULT 0)''')
        conn.commit()

@app.route('/')
def index():
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, 0)", (title, description))
        conn.commit()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
