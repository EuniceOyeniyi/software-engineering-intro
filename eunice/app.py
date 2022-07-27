from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(150), nullable=False)





@app.route('/')
def home():
    output = Todo.query.all()
    return render_template('index.html', todos = output)

@app.route('/<ID>')
def delete(ID):
    todo = Todo.query.filter_by(id = ID).first()
    db.session.delete(todo)
    db.session.commit()

    # return str(todo.id)
    return redirect('/')

@app.route('/add', methods = ['POST', 'GET'])
def add():

    if request.method == 'POST':
        name = request.form.get("todo_name")
        description = request.form.get('todo_description')
        todo = Todo(name = name, description = description)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
        # return 'success'
    
    else:

        return render_template('add.html')

@app.route('/update/<ID>')
def update(ID):
    return "This is the todo " + ID

if __name__ == '__main__':
    # create database and table including column names
    db.create_all()

    # Creating rows
    # todo1 = Todo(name = 'Learn Python', description = 'pthton python ptyhon')
    # todo2 = Todo(name = 'Learn Maths', description = 'mat mtaht mahtatzt')

    # db.session.add(todo1)
    # db.session.add(todo2)
    # db.session.commit()

    # retrieving the whole table
    # output = Todo.query.all()
    # print(output)



    # Update a row
    # todo = Todo.query.filter_by(id = 2).first()
    # print(todo.name)
    # todo.name = 'Deep Learning'
    # db.session.commit()
    
    
    

   


    app.run(debug=True)