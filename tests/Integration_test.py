import pytest,datetime,dotenv,json
from unittest.mock import patch,Mock
from pathlib import Path

from todo_app.app import ViewModel, Lists, create_app
from todo_app.trello_requests import get_BoardId,find_list,get_List,get_Items,add_Item,get_Item,set_Item

@pytest.fixture
def mock_request():
    with patch('requests.request') as mock_get:
        mock_get.side_effect = mock_get_lists
        yield mock_get

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = dotenv.find_dotenv('.env.test')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(mock_request,client):
    # Replace call to requests.get(url) with our own function
    mock_request.side_effect = mock_get_lists
    response = client.get('/')

def mock_get_lists(http_method,url,params,headers):
    if url == f'https://api.trello.com/1/boards/603b8faf893153146df47462/lists':
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        json_payload = [
            {
                "id":"603b8faf893153146df47463",
                "name":"To Do",
                "closed":False,
                "idBoard":"603b8faf893153146df47462"
                },
            {
                "id":"603b8faf893153146df47464",
                "name":"Doing",
                "closed":False,
                "idBoard":"603b8faf893153146df47462"
                },
            {
                "id":"603b8faf893153146df47465",
                "name":"Done",
                "closed":False,
                "idBoard":"603b8faf893153146df47462"
            }
        ]
        response.json.return_value = json_payload
        return response
    
    if url == f'https://api.trello.com/1/members/me/boards':
        response = Mock()
        json_payload = [
            {
                "name":"SqmIler01",
                "desc":"",
                "closed":False,
                "dateLastActivity":"2021-04-13T10:20:28.795Z",
                "id":"603b8faf893153146df47462",
                "url":"https://trello.com/b/6YqdMuoc/sqmiler01"
            }
        ]
        response.json.return_value = json_payload
        return response

    #To Do
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47463/cards':
        response = Mock()
        json_payload = [
            {
                "id":"603b8fd8acd0617a9083538c",
                "closed":False,
                "dateLastActivity":"2021-04-05T14:41:54.021Z",
                "desc":"Git",
                "name":"Module 01"
            },
            {
                "id":"603b8fbe7e6f76736df8f830",
                "closed":False,
                "dateLastActivity":"2021-03-06T16:14:33.349Z",
                "desc":"get new brake pads for CB1000"
            }            
        ]
        response.json.return_value = json_payload
        return response
    
    #Doing
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47464/cards':
        response = Mock()
        json_payload = [
            {
                "id":"6057626a5bcbda0de54a84aa",
                "closed":False,
                "dateLastActivity":"2021-04-10T15:08:32.682Z",
                "desc":"In Little China",
                "name":"Big Trouble"
            }]
        response.json.return_value = json_payload
        return response

    #Done
    if url == f'https://api.trello.com/1/lists/603b8faf893153146df47465/cards':
        response = Mock()
        json_payload = [
            {
                "id":"60577dc059f0e757ef88adea",
                "closed":False,
                "dateLastActivity":"2021-04-10T14:49:58.395Z",
                "desc":"In Little China",
                "idBoard":"603b8faf893153146df47462",
                "idList":"603b8faf893153146df47465",
                "name":"Trouble2"                
            },
            {
                "id":"60576cbf71386d2f67265eba",
                "closed":False,
                "dateLastActivity":"2021-04-10T14:49:59.640Z",
                "desc":"In Little China",
                "idBoard":"603b8faf893153146df47462",
                "idList":"603b8faf893153146df47465",
                "name":"Brake pads"
            },
            {
                "id":"603b8fe3a9fd0418a86ffa17",
                "closed":False,
                "dateLastActivity":"2021-04-10T14:50:00.676Z",
                "desc":"Potatoes",
                "idBoard":"603b8faf893153146df47462",
                "idList":"603b8faf893153146df47465",
                "name":"Cook dinner"
            }]
        response.json.return_value = json_payload
        return response 

    return None

def mock_edit_item(http_method,url,params,headers):
    if url == f'https://api.trello.com/1/cards/603b8fd8acd0617a9083538c':
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        json_payload = {
            "dateLastActivity": "2021-04-05T14:41:54.021Z",
            "desc": "Git",
            "name": "Module 01",
            "idList":"603b8faf893153146df47463"}
        response.json.return_value = json_payload
        return response
    
    if 'https://api.trello.com/1/lists/' in url:
        response = Mock()
        # sample_trello_lists_response should point to some test response data
        json_payload = {
            "id":"603b8faf893153146df47463",
            "name":"To Do",
            "closed":False,
            "pos":16384,
            "idBoard":"603b8faf893153146df47462"}
        response.json.return_value = json_payload
        return response

    if url == f'https://api.trello.com/1/members/me/boards':
        response = Mock()
        json_payload = [
            {"name":"SqmIler01",
            "desc":"",
            "descData":None,
            "dateLastActivity":"2021-04-13T10:20:28.795Z",
            "id":"603b8faf893153146df47462",
            "url":"https://trello.com/b/6YqdMuoc/sqmiler01"}
            ]
        response.json.return_value = json_payload
        return response

    if url == f'https://api.trello.com/1/boards/603b8faf893153146df47462/lists':
        response = Mock()
        json_payload = [
            {
                "id":"603b8faf893153146df47463",
                "name":"To Do",
                "idBoard":"603b8faf893153146df47462"},
            {
                "id":"603b8faf893153146df47464",
                "name":"Doing",
                "idBoard":"603b8faf893153146df47462"},
            {
                "id":"603b8faf893153146df47465",
                "name":"Done",
                "idBoard":"603b8faf893153146df47462"}
            ]
        response.json.return_value = json_payload
        return response
        
def test_editItem_page(mock_request,client):
    # Replace call to requests.get(url) with our own function
    mock_request.side_effect = mock_edit_item 
    #response = client.request('/')
    response = client.get('/EditItem.html?id=603b8fd8acd0617a9083538c')

