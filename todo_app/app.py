from flask import Flask, render_template, session, request, redirect, url_for, Markup
from flask_wtf import FlaskForm
from wtforms import validators, RadioField
from abc import ABC, abstractmethod

from todo_app.flask_config import Config
from .trello_requests import get_BoardId,find_list,get_List,get_Items,add_Item,get_Item,set_Item

# Thanks to https://stackoverflow.com/questions/25297716/how-to-make-radio-field-show-default-value-with-flask-and-wtforms
# for the wtforms Radio Buttons. Only way I could do it after a lot of Googling.

app = Flask(__name__)
app.config.from_object(Config)
trelloBoard = get_BoardId(Config.BOARD_ID)

class ListForm(FlaskForm):
    list_switcher = RadioField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('done', 'Done')],default='todo')
class Lists():
    listName = "To Do"
    list_types_forward = {"To Do":"todo","Doing":"doing","Done":"done"}
    list_types_reverse = {"todo":"To Do","doing":"Doing","done":"Done"}
    def __init__(self,listtype):
        self.listName = listtype
        self.listKey = self.list_types_forward[self.listName]
        self.listID = find_list(trelloBoard,self.listName)
        self.listItems = get_Items(self.listID)
    
    def add_items(self,name,desc):
        add_Item(self.listID,name,desc)

    """def set_Item(itemId,name,desc,idList):
        Item = self.listItems
        Item = Item[itemId]
        set_Item(self.listID,name,desc)"""

    """def remove_items(self,name,desc):
        Items = self.listItems"""

class ViewModel:
    def __init__(self, todo,doing,done):
        self._todo = todo
        self._doing = doing
        self._done = done
    @property
    def todo(self):
        return self._todo
    @property
    def doing(self):
        return self._doing
    @property
    def done(self):
        return self._done

if not trelloBoard:
    print("Board not found")
    exit()

@app.route('/',methods = ['GET'])
def index():
    viewLists = ViewModel(Lists("To Do").listItems,Lists("Doing").listItems,Lists("Done").listItems)
    return render_template('index.html',view_model=viewLists)

@app.route('/NewItem.html',methods = ['GET'])
def get_newItemPage():
    return render_template('NewItem.html')

@app.route('/NewItem.html',methods = ['POST'])
def post_newItemPage():
    Lists("To Do").add_items(request.form.get('newItem'),request.form.get('Description'))
    return redirect(url_for('index'))

@app.route('/EditItem.html',methods = ['GET'])
def get_editItemPage():
    itemId = request.args['id']
    EditItem = get_Item(itemId)
    List =  get_List(EditItem['idList'])
    listForm = ListForm()
    #listForm.list_switcher.data = "todo"
    listForm.list_switcher.data = Lists(List["name"]).listKey
    request.form.pop
    return render_template('EditItem.html',Item=EditItem, form=listForm)

@app.route('/EditItem.html',methods = ['POST'])
def post_editItemPage():
    EditItem = get_Item(request.form.get('itemId'))
    edit_name = request.form.get('Item')
    edit_desc = request.form.get('Description')
    edit_list = Lists.list_types_reverse[request.form["list_switcher"]]
    edit_listId = find_list((EditItem['idBoard']),edit_list)
    set_Item(EditItem['id'],edit_name,edit_desc,edit_listId)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
