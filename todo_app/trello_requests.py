from todo_app.flask_config import Config
import requests,json,sys

rootUrl = "https://api.trello.com/1"
headers = {
    "Accept": "application/json"}

def get_BoardId(BoardName):
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    url = rootUrl+"/members/me/boards"
    boards_response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    boards = boards_response.json()
    for board in boards:
        if board['name'] == BoardName:
            board = board['id']
            break
    else:
        board = None
    return board

def find_list(trelloBoard,listName):
    url = rootUrl+"/boards/"+trelloBoard+"/lists"
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    board_response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    lists = board_response.json()
    for list in lists:
        if list['name'] == listName:
            return list['id']
    return None

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
    output = getList.json()
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
    output = cards.json()
    return output

def add_Item(todo_list,name,desc):
    url = rootUrl+"/cards"
    query = {
        'key': Config.KEY,
        'token': Config.TOKEN}
    query['idList'] = todo_list
    query['name'] = name
    query['desc'] = desc
    newCard = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )
    output = newCard.json()
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
    output = getCard.json()
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
    output = setCard.json()
    return output
