from flask import Flask, render_template, session, request, redirect, url_for, Markup
from flask_wtf import FlaskForm
from wtforms import validators, RadioField
from abc import ABC, abstractmethod
import datetime

from todo_app.flask_config import Config
from .trello_requests import get_BoardId,find_list,get_List,get_Items,add_Item,get_Item,set_Item

# Thanks to https://stackoverflow.com/questions/25297716/how-to-make-radio-field-show-default-value-with-flask-and-wtforms
# for the wtforms Radio Buttons. Only way I could do it after a lot of Googling.


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    view_lists = ViewModel(Lists("To Do").listItems, Lists("Doing").listItems, Lists("Done").listItems)

    @app.route('/',methods = ['GET'])
    def index():
        view_lists.update_lists()
        return render_template('index.html',view_model=view_lists)

    @app.route('/',methods = ['POST'])
    def switch_done_filter():
        view_lists.switch_filter()
        view_lists.update_lists()
        return render_template('index.html',view_model=view_lists)

    @app.route('/NewItem.html',methods = ['GET'])
    def get_newItemPage():
        return render_template('NewItem.html')

    @app.route('/NewItem.html',methods = ['POST'])
    def post_newItemPage():
        Lists("To Do").add_items(request.form.get('newItem'),request.form.get('Description'))
        return redirect(url_for('index'))

    @app.route('/EditItem.html',methods = ['GET'])
    def get_editItemPage():
        item_id = request.args['id']
        item = get_Item(item_id)
        item_list =  get_List(item['idList'])
        list_form = ListForm()
        list_form.list_switcher.data = Lists(item_list["name"]).listKey
        request.form.pop
        return render_template('EditItem.html',Item=item, form=list_form)

    @app.route('/EditItem.html',methods = ['POST'])
    def post_editItemPage():
        item = get_Item(request.form.get('itemId'))
        edit_name = request.form.get('Item')
        edit_desc = request.form.get('Description')
        edit_list = Lists.list_types_reverse[request.form["list_switcher"]]
        edit_list_id = find_list((item['idBoard']),edit_list)
        set_Item(item['id'],edit_name,edit_desc,edit_list_id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run()

    return app

class ListForm(FlaskForm):
    list_switcher = RadioField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('done', 'Done')],default='todo')

class Lists():
    listName = "To Do"
    list_types_forward = {"To Do":"todo","Doing":"doing","Done":"done"}
    list_types_reverse = {"todo":"To Do","doing":"Doing","done":"Done"}
    def __init__(self,listtype):
        trelloboard = get_BoardId(Config().BOARD_ID)
        """    if not trelloBoard:
        print("Board not found")
        exit()
        """
        self.listName = listtype
        self.listKey = self.list_types_forward[self.listName]
        self.listID = find_list(trelloboard,self.listName)
        self.listItems = get_Items(self.listID)
    
    def add_items(self,name,desc):
        add_Item(self.listID,name,desc)

class ViewModel:
    def __init__(self,todo_items=[],doing_items=[],done_items=[]):
        self._todo = todo_items
        self._doing = doing_items
        self._done = done_items
        self._filter_done = True
    @property
    def todo(self):
        return self._todo
    @property
    def doing(self):
        return self._doing
    @property
    def done(self):
        if len(self._done) < 5 or self._filter_done == False:
            return self._done
        done_today = [item for item in self._done if item['dateLastActivity'].split("T")[0] == (datetime.datetime.now()).strftime("%Y-%m-%d")]
        return done_today

    def update_lists(self):
       self._todo = Lists("To Do").listItems
       self._doing = Lists("Doing").listItems
       self._done = Lists("Done").listItems

    def switch_filter(self):
        if self._filter_done == True:
            self._filter_done = False
        else:
            self._filter_done = True

app = create_app()