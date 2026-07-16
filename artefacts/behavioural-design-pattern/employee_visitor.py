from abc import ABC, abstractmethod


# ---------- Visitor ----------
class Visitor(ABC):

    @abstractmethod
    def visit_developer(self, developer):
        pass

    @abstractmethod
    def visit_manager(self, manager):
        pass


# ---------- Employee ----------
class Employee(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Developer(Employee):

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visit_developer(self)


class Manager(Employee):

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.visit_manager(self)


# ---------- Concrete Visitor ----------
class ReportVisitor(Visitor):

    def visit_developer(self, developer):
        return f"Developer Report: {developer.name}"

    def visit_manager(self, manager):
        return f"Manager Report: {manager.name}"


# ---------- Client ----------
employees = [
    Developer("Alice"),
    Manager("John")
]

visitor = ReportVisitor()

print("Employee Reports")
print("----------------")

for employee in employees:
    print(employee.accept(visitor))
