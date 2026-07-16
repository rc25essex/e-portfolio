import pytest
from employee_visitor import Developer, Manager, ReportVisitor


def test_developer_report(capsys):
    developer = Developer("Alice")
    visitor = ReportVisitor()

    developer.accept(visitor)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Developer Report: Alice"


def test_manager_report(capsys):
    manager = Manager("John")
    visitor = ReportVisitor()

    manager.accept(visitor)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Manager Report: John"
