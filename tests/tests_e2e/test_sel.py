import os,pytest,unittest,dotenv
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from todo_app.app import create_app
from todo_app.trello_requests import *


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver

@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    response = create_trello_board("DeleteMe")
    os.environ['TRELLO_BOARD_ID'] = response['id']
    os.environ['BOARD_ID'] = "DeleteMe" # Use to override default.

    # construct the new application
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    #Create test List
    test_list = add_List('Test: To Do',(os.environ['TRELLO_BOARD_ID'])) # all three lists exist already!

    #New item
    test_item = add_Item(test_list['id'],"test item","test-description")
    
    #Start item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(os.environ['TRELLO_BOARD_ID'],"Doing"))

    # Complete Item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(os.environ['TRELLO_BOARD_ID'],"Done"))

    # Incomplete item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(os.environ['TRELLO_BOARD_ID'],"Doing"))

    # Tear Down
    thread.join(1)
    board_id = get_BoardId("DeleteMe")
    delete_trello_board(board_id)

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

