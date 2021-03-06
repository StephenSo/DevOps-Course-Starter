from flask import Flask, render_template, session, request, redirect, url_for, Markup
from flask_wtf import Form
from wtforms import validators, RadioField

import requests,json,sys
from todo_app.flask_config import Config

# Thanks to https://stackoverflow.com/questions/25297716/how-to-make-radio-field-show-default-value-with-flask-and-wtforms
# for the wtforms Radio Buttons. Only way to do it after a lot of Googling.

app = Flask(__name__)
app.config.from_object(Config)

rootUrl = "https://api.trello.com/1"
headers = {
    "Accept": "application/json"}


def get_BoardId(BoardName):
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    url = rootUrl+"/members/me/boards"
    Boards = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    Boards = (json.loads(Boards.text))
    for Board in Boards:
        if Board['name'] == BoardName:
            Board = Board['id']
            break
    else:
        Board = None
    return Board
def find_list(trelloBoard,listName):
    url = rootUrl+"/boards/"+trelloBoard+"/lists"
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    Boards = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    Lists = (json.loads(Boards.text))
    for List in Lists:
        if List['name'] == listName:
            List = List['id']
            break
    else:
        List = None
    return List
def get_List(id):
    url = rootUrl+"/lists/"+id
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    getList = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    output = (json.loads(getList.text))
    return output   
def get_Items(todo_list):
    url = rootUrl+"/lists/"+todo_list+"/cards"
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    cards = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    output = (json.loads(cards.text))
    return output
def add_Item(todo_list,name,desc):
    url = rootUrl+"/cards"
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    query['idList'] = todo_list
    query['name'] = name
    query['desc'] = desc
    query = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )
    output = (json.loads(newCard.text))
    return output
def get_Item(id):
    url = rootUrl+"/cards/"+id
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    getCard = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    output = (json.loads(getCard.text))
    return output
def set_Item(itemId,name,desc,state):
    url = rootUrl+"/cards/"+itemId
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    query['name'] = name
    query['desc'] = desc
    query['idList'] = state
    setCard = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    output = (json.loads(setCard.text))
    return output

trelloBoard = get_BoardId("SqmIler01")
if not trelloBoard:
    print("Board not found")
    exit()
todo_list = find_list(trelloBoard,"To Do")
todoItems = get_Items(todo_list)
doneItems = get_Items(find_list(trelloBoard,"Done"))

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html',
            todoItems=get_Items(todo_list),
            doneItems = get_Items(find_list(trelloBoard,"Done")))
@app.route('/NewItem.html',methods = ['POST', 'GET'])
def newItemPage():
    if request.method == 'POST':
        name = request.form.get('newItem')
        desc = request.form.get('Description')
        add_Item(todo_list,name,desc)
        return redirect(url_for('index'))

    if request.method == 'GET':
        return render_template('NewItem.html')
@app.route('/EditItem.html',methods = ['POST', 'GET'])
def editItemPage():
    if request.method == 'GET':
        itemId = request.args['id']
        EditItem = get_Item(itemId)
        List =  get_List(EditItem['idList'])
        if List['name'] == "To Do":
            State = "todo"
        if List['name'] == "Done":
            State = "done"
        class ListForm(Form):
            list_switcher = RadioField(
                'state?',
                [validators.Required()],
                choices=[('todo', 'To Do'), ('done', 'Done')], default=State
            )            
        listForm = ListForm()
        request.form.pop
        return render_template('EditItem.html',Item=EditItem, form=listForm)

    if request.method == 'POST':
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
