import pytest

from todo_app.app import ViewModel, Lists

def test_getLists():
  viewLists = ViewModel(todo="To Do",doing="Doing",done="Done")
  assert viewLists.todo != None and viewLists.doing != None and viewLists.done != None

