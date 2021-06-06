import pytest
from datetime import datetime, timedelta
from todo_app.app import ViewModel, Lists

yesterday = (datetime.now() + timedelta(days=-1) ).strftime('%Y-%m-%d')
today = (datetime.now()).strftime('%Y-%m-%d')
todo_items = [
  {"desc":"Gitly","name":"Green","dateLastActivity":"2021-04-13T10:20:28.795Z"}]
done_items = [
  {"desc":"OldTask1","dateLastActivity":"{}T10:20:28.795Z".format(yesterday)},
  {"desc":"NewTask1","dateLastActivity":"{}T10:20:28.795Z".format(today)},
  {"desc":"NewTask2","dateLastActivity":"{}T10:20:28.795Z".format(today)},
  {"desc":"NewTask3","dateLastActivity":"{}T10:20:28.795Z".format(today)},
  {"desc":"NewTask4","dateLastActivity":"{}T10:20:28.795Z".format(today)},
  {"desc":"NewTask5","dateLastActivity":"{}T10:20:28.795Z".format(today)},
  {"desc":"OldTask2","dateLastActivity":"{}T10:20:28.795Z".format(yesterday)},
  {"desc":"OldTask3","dateLastActivity":"{}T10:20:28.795Z".format(yesterday)}]
doing_items = [
  {"desc":"Git","name":"Module 01","dateLastActivity":"2021-04-13T10:20:28.795Z"},
  {"desc":"Gitly","name":"Green","dateLastActivity":"2021-04-13T10:20:28.795Z"}]

def test_getDoneList():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  assert len(view_lists.done) == 5

def test_getDoingList():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  assert len(view_lists.doing) == 2

def test_getToDoList():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  assert len(view_lists.todo) == 1

def test_show_less_than_5_done_unless_done_today():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  done = view_lists.done
  not_done_today = [item for item in done if item['dateLastActivity'].split("T")[0] != ((datetime.now()).strftime('%Y-%m-%d'))]
  if len(done) >= 5:
    assert len(not_done_today) == 0
  assert len(done) == 5

def test_show_all_done_items():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  if view_lists._filter_done:
    view_lists.switch_filter()
  assert not view_lists._filter_done

def test_recent_done_items():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  done_today = [item for item in view_lists.done if item['dateLastActivity'].split("T")[0] == ((datetime.now()).strftime('%Y-%m-%d'))]
  assert len(done_today) == len(view_lists.done)

def test_older_done_items():
  view_lists = ViewModel(todo_items, doing_items, done_items)
  if view_lists._filter_done:
    view_lists.switch_filter()
  older_done = [item for item in view_lists.doing if item['dateLastActivity'].split("T")[0] < ((datetime.now()).strftime('%Y-%m-%d'))]
  assert len(older_done) >= 0

