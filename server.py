from flask import Flask,request, redirect,render_template
from data_access import *

app = Flask('Todo App')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/list',methods=['GET'])
def list_todo():
    list_todo = getAllTodos()
    return render_template("list.html", list_todo=list_todo)

@app.route('/add',methods=['GET','POST'])
def add():   
    if request.method == 'POST':
        l = getAllTodos() 
        if len(l) != 0:
            id_t = (l[len(l)-1]._id_t)+1
        else:
            id_t = 1
        add_todo(id_t,request.form['description'])
    else:
        print("Printing the add page")
    
    return render_template('add.html',list_todo=getAllTodos())
   


@app.route('/remove_list',methods=['GET','POST'])
def remove_list():
    if request.method == 'POST':
        v = request.form.getlist('check')
        for elt in v:
            remove_todo(elt)
        return redirect('/list')
    else:
        l = getAllTodos() 
        return render_template('remove list.html',list_todo=l)



# Faire plusieurs render_templates ?
@app.route('/modify',methods=['GET','POST'])
def modify():
    if request.method == 'POST':
        #Avoir la liste des todos cochables
        todo_id = request.form.get('to_update')
        print("Hello",todo_id)
        t = get_todo(todo_id)
        print("TODO : ",t)
        return render_template("modify_todo.html", todo=t)
    else:
        list_todo = getAllTodos()
        return render_template("modify.html", list_todo=list_todo)

@app.route('/modify_todo', methods=['GET','POST'])
def modify_todo():
    if request.method == 'POST':
        id = request.form.get('id')
        print("GET ID",id)
        t = request.form.get('updated')
        print('GET T')
        modify_todo(t[0],t[1])
        return redirect('/list') 
    else:
        list_todo = getAllTodos()
        return redirect('/list')
        

"""
@app.route('/remove', methods=['GET','POST'])
def remove():
    if request.method == 'POST':
        v = request.form.get('todos')
        v = int(v)
        print(v)
        remove_todo(v)
        return redirect('/list')
    else:
        l = getAllTodos() 
        return render_template('remove.html',list_todo=l)
"""


if __name__ == "__main__":
    app.debug = True
    app.run()