from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_add_function_adds_an_instance_task():
    task_list = TaskList()
    task_list.add(task1)
    assert task_list.tasks == [task1]

class task1:
    pass

def test_all_function_returns_all_instances_of_task_mock():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all() == [task1, task2]


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_all_complete_function_mock():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all_complete() == True
    
# Unit test `#tasks` and `#all_complete` behaviour
