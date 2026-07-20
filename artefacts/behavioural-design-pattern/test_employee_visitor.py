from employee_visitor import Developer, Manager, ReportVisitor


def test_developer_report():
    developer = Developer("Alice")
    visitor = ReportVisitor()

    result = developer.accept(visitor)

    assert result == "Developer Report: Alice"


def test_manager_report():
    manager = Manager("John")
    visitor = ReportVisitor()

    result = manager.accept(visitor)

    assert result == "Manager Report: John"
