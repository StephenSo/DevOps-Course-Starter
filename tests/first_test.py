import pytest

from todo_app.app import ViewModel, Lists

def test_getLists():
  viewLists = ViewModel(Lists("To Do").listItems,Lists("Doing").listItems,Lists("Done").listItems)
  assert viewLists.todo != None and viewLists.doing != None and viewLists.done != None

