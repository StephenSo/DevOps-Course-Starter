from flask import Flask, render_template, session, request, redirect, url_for, Markup
from flask_wtf import FlaskForm
from wtforms import validators, RadioField

from todo_app.flask_config import Config
from .trello_requests import *

# Thanks to https://stackoverflow.com/questions/25297716/how-to-make-radio-field-show-default-value-with-flask-and-wtforms
# for the wtforms Radio Buttons. Only way I could do it after a lot of Googling.

app = Flask(__name__)
app.config.from_object(Config)
trelloBoard = get_BoardId(Config.BOARD_ID)

class ListForm(FlaskForm):
    list_switcher = RadioField(choices=[('todo', 'To Do'), ('done', 'Done')],default='todo')

if not trelloBoard:
    print("Board not found")
    exit()

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html',
        todoItems = get_Items(find_list(trelloBoard,"To Do")),
        doneItems = get_Items(find_list(trelloBoard,"Done")))

@app.route('/NewItem.html',methods = ['POST'])
def post_newItemPage():
    if request.method == 'POST':
        name = request.form.get('newItem')
        desc = request.form.get('Description')
        add_Item(todo_list,name,desc)
        return redirect(url_for('index'))

@app.route('/NewItem.html',methods = ['GET'])
def get_newItemPage():
    return render_template('NewItem.html')

@app.route('/EditItem.html',methods = ['GET'])
def get_editItemPage():
    itemId = request.args['id']
    EditItem = get_Item(itemId)
    List =  get_List(EditItem['idList'])
    if List['name'] == "To Do":
        State = "todo"
    if List['name'] == "Done":
        State = "done"

    listForm = ListForm()
    listForm.list_switcher.data = State
    request.form.pop
    return render_template('EditItem.html',Item=EditItem, form=listForm)

@app.route('/EditItem.html',methods = ['POST'])
def post_editItemPage():
    itemId = request.form.get('itemId')
    name = request.form.get('Item')
    desc = request.form.get('Description')
    state = request.form["list_switcher"]
    if state == "todo":
        listId = find_list(trelloBoard,"To Do")
    if state == "done":
        listId = find_list(trelloBoard,"Done")
    set_Item(itemId,name,desc,listId)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
