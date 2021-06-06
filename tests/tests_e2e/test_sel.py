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

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

def test_item_journey(driver: webdriver, app_with_temp_board):
    driver.get('http://localhost:5000/NewItem.html')
    #Add new item
    elem = driver.find_element_by_id('newItem')
    elem.send_keys(test_item_name)
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()
    #Set new item to doing
    elem = driver.find_element_by_name(f'edit-{test_item_name}')
    elem.click()
    doing_radio = driver.find_element_by_xpath("//input[@value='doing']")
    doing_radio.click()
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()
    #Set new item to done
    elem = driver.find_element_by_name(f'edit-{test_item_name}')
    elem.click()
    done_radio = driver.find_element_by_xpath("//input[@value='done']")
    done_radio.click()
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()    
    assert driver.find_element_by_partial_link_text(test_item_name)

