import os,pytest,unittest,dotenv
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from todo_app.app import create_app
from todo_app.trello_requests import *

test_item_name = 'test-item'
test_board_name = 'DeleteMe'

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()

@pytest.fixture(scope='module')
def app_with_temp_board():
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    
    os.environ['BOARD_NAME'] = test_board_name # Use to override default.
    response = create_trello_board(os.environ['BOARD_NAME'])
    board_id = response['id']

    # construct the new application
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application
    #Get test List
    test_list_id = find_list(board_id,'To Do') # all three lists exist already!
    
@pytest.fixture(scope="module")
def app_addItem():
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    os.environ['BOARD_NAME'] = test_board_name # Use to override default.
    board_id = get_BoardId(os.environ['BOARD_NAME'])
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    #Get test List
    test_list_id = find_list(board_id,'To Do') # all three lists exist already!
    
    #New item
    test_item = add_Item(test_list_id,test_item_name,"test-description")
    #Start item
    #set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Doing"))

    # Complete Item
    #set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Done"))

    # Incomplete item
    #set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Doing"))

    # Tear Down

@pytest.fixture(scope="module")
def app_ItemIsDoing():
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    os.environ['BOARD_NAME'] = test_board_name # Use to override default.
    board_id = get_BoardId(os.environ['BOARD_NAME'])
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    #Get test List
    test_list_id = find_list(board_id,'To Do') # all three lists exist already!
    
    #Get item
    test_item = get_Items(test_list_id)[0]
        
    #Start item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Doing"))

    # Complete Item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Done"))

    # Incomplete item
    set_Item(test_item['id'],test_item['name'],test_item['desc'],find_list(board_id,"Doing"))

    # Tear Down

@pytest.fixture(scope="module")
def app_delete_temp_board():
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    # Create the new board & update the board id environment variable
    
    os.environ['BOARD_NAME'] = test_board_name # Use to override default.
    board_id = get_BoardId(os.environ['BOARD_NAME'])
    test_item_name = 'test-item'

    # construct the new application
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda:application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

def test_step1_task_createBoard(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'
    
def test_step2_task_addItem(driver, app_addItem):
    driver.get('http://localhost:5000/')
    driver.refresh()
    assert driver.find_element_by_partial_link_text(test_item_name)
    
def test_step3_task_ItemIsDoing(driver, app_ItemIsDoing):
    driver.get('http://localhost:5000/')
    driver.refresh()
    assert driver.find_element_by_partial_link_text(test_item_name)

def test_step9_delete_board(driver, app_delete_temp_board):
    driver.get('http://localhost:5000/')
