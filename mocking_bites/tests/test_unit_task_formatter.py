from lib.task_formatter import *
from unittest.mock import Mock

def test_format_returns_formatted_string_if_not_complete():
    fake_task = Mock()
    fake_task.title = "I am a task"
    fake_task.complete = False
    formatted_task = TaskFormatter(fake_task)
    assert formatted_task.format() == "[ ] I am a task"

def test_format_returns_formatted_string_if_complete():
    fake_task = Mock()
    fake_task.title = "I am a task"
    fake_task.complete = True
    formatted_task = TaskFormatter(fake_task)
    assert formatted_task.format() == "[x] I am a task"

