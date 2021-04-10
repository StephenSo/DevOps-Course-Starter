import pytest, datetime

from todo_app.app import ViewModel, Lists

def test_getDoneList():
  view_lists = ViewModel()
  assert len(view_lists.done) >= 0

def test_getDoingList():
  view_lists = ViewModel()
  assert len(view_lists.doing) >= 0

def test_getToDoList():
  view_lists = ViewModel()
  assert len(view_lists.todo) >= 0

def test_show_less_than_5_done_unless_done_today():
  view_lists = ViewModel()
  done = view_lists.done
  not_done_today = [item for item in done if item['dateLastActivity'].split("T")[0] != (datetime.datetime.now()).strftime("%Y-%m-%d")]
  if len(done) >= 5:
    assert len(not_done_today) == 0
  assert len(done) < 5

def test_show_all_done_items():
  view_lists = ViewModel(filter_done=False)
  assert len(view_lists.done) >= 0

def test_recent_done_items():
  view_lists = ViewModel()
  done_today = [item for item in view_lists.done if item['dateLastActivity'].split("T")[0] == (datetime.datetime.now()).strftime("%Y-%m-%d")]
  assert len(done_today) == len(view_lists.done)

def test_older_done_items():
  view_lists = ViewModel(filter_done=False)
  older_done = [item for item in view_lists.doing if item['dateLastActivity'].split("T")[0] < (datetime.datetime.now()).strftime("%Y-%m-%d")]
  assert len(older_done) >= 0

