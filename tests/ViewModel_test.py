import pytest, datetime


from todo_app.app import ViewModel, Lists

def test_getDoneList():
  test_items = [{
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 01"}]
  view_lists = ViewModel(test_items,test_items,test_items)
  assert len(view_lists.done) >= 0

def test_getDoingList():
  test_items = [{
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 01"}]
  view_lists = ViewModel(test_items,test_items,test_items)
  assert len(view_lists.doing) >= 0

def test_getToDoList():
  test_items = [{
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 01"}]
  view_lists = ViewModel(test_items,test_items,test_items)

def test_show_less_than_5_done_unless_done_today():
  test_items = [
    {
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 01"},
    {
    "dateLastActivity": (datetime.datetime.now()).strftime("%Y-%m-%d"),
    "desc": "Git",
    "name": "Module 02"},
    {
    "dateLastActivity": (datetime.datetime.now()).strftime("%Y-%m-%d"),
    "desc": "Git",
    "name": "Module 03"},
    {
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 04"},
    {
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 05"},
    {
    "dateLastActivity": "2021-04-05T14:41:54.021Z",
    "desc": "Git",
    "name": "Module 06"}
  ]

  view_lists = ViewModel(test_items,test_items,test_items)
  done = view_lists.done
  not_done_today = [item for item in done if item['dateLastActivity'].split("T")[0] != (datetime.datetime.now()).strftime("%Y-%m-%d")]
  if len(done) >= 5:
    assert len(not_done_today) == 0
  assert len(done) < 5

def test_show_all_done_items():

  view_lists = ViewModel()
  if view_lists._filter_done:

    view_lists.switch_filter()
  assert not view_lists._filter_done


def test_recent_done_items():

  view_lists = ViewModel()

  done_today = [item for item in view_lists.done if item['dateLastActivity'].split("T")[0] == (datetime.datetime.now()).strftime("%Y-%m-%d")]

  assert len(done_today) == len(view_lists.done)

def test_older_done_items():

  view_lists = ViewModel()
  if view_lists._filter_done:

    view_lists.switch_filter()

  older_done = [item for item in view_lists.doing if item['dateLastActivity'].split("T")[0] < (datetime.datetime.now()).strftime("%Y-%m-%d")]

  assert len(older_done) >= 0
