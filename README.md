# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)
```bash

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

```
 ### Poetry installation (PowerShell)
 
```powershell

(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

```
## Dependencies
  

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:
 
```bash

$ poetry install

```
You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash

$ cp .env.template .env # (first time only)

``` 


The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

  

## Running the App

  

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:

```bash

$ poetry run flask run

```
You should see output similar to the following:

```bash

* Serving Flask app "app" (lazy loading)

* Environment: development

* Debug mode: on

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

* Restarting with fsevents reloader

* Debugger is active!

* Debugger PIN: 226-556-590

```

Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


## Running Developer Tests

**Running automated tests**

To run all tests, `cd` into '''tests''' folder

`poetry run pytest`
##
**Unit tests:** 
`poetry run pytest tests/ViewModel_test.py`

 - This test validates the `ViewModel class` used in `app.py`
	 - `test_getDoneList` - Validates the "Done" list
	 - `test_getDoingList` - Validates the "Doing" list
	 - `test_getToDoList` Validates the "To Do" list 
	 - `test_show_less_than_5_done_unless_done_today` Tests if there are fewer than 5 completed tasks, show all of them otherwise, only show tasks that have been completed today
	 - `test_show_all_done_items` By setting filter_done to False, we should see all done items.
	 - `test_recent_done_items` Tests if no 'filter_done', we should get items Done today
	 - `test_older_done_items` Test if 'filter_done=False', we should be able to get items done before today.

##

**Integration Test:**
 `poetry run pytest tests/Integration_test.py`
 This tests:
 - `test_index_page` - Validates initial page load. 
 - `test_edititem_page`- Checks updates to items in a list.

##
**End to end tests:**

`poetry run pytest tests/tests_e2e/test_sel.py`
Creates a test board named `DeleteMe`

*New item*
`add_item` = Creates a test to do item, adding to the to do list

*Start Item*
`set_Item` = Takes the test item and sets it to the to doing list

*Complete Item*
`set_Item` = Takes the test item and sets it to the to done list

*Incomplete item*
`set_Item` = Takes the test item and sets it back to the to doing list

