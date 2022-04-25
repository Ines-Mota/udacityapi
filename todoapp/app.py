from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Establishes the connection between the database and the flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@127.0.0.1:5432/todos'
db = SQLAlchemy(app)

migrate = Migrate(app, db)


# Creates the tables in the databases in sqlalchemy & uses the dunder repr method to print items on TODO instead of <item1>
class Todo(db.Model):
    __tablename__= 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

class TodoList(db.Model):
    __tablename__='todolists'
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(), nullable = False)
    todos = db.relationship('Todo', backref='list', lazy=True)
#db.create_all()

@app.route('/')
def index(): # Controller controls what the program should do and what the views should show next ie. index.html file
   return render_template('index.html', data=Todo.query.order_by('id').all())


@app.route('/todo/create', methods=['POST'])
def create_todo():

   # description = request.form.get('description', '') -- to get the resquest via form  
    description = request.get_json()

    to_do = Todo(description['description'])
    print (to_do)
    db.session.add(to_do)
    db.session.commit()
    return jsonify({
        'description': to_do.description
    })

    # return redirect(url_for('index'))


@app.route('/todo/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):

    try:
        completed = request.get_json()['completed']
        todo=Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    
    return redirect(url_for('index'))

@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_task(todo_id):

    try:
        task = Todo.query.filter(Todo.id == todo_id)
        task.delete()
        db.session.commit()

    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({ 'success': True })
